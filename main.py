from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os, io, uuid
import google.generativeai as genai

try:
    from supabase import create_client, Client
    SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
    SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_KEY", "")
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL else None
except:
    supabase = None

try:
    import pdfplumber
    HAS_PDF = True
except:
    HAS_PDF = False

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI(title="MedEtu API", version="2.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    lang: str = "ar"
    year: str = "PCEM1"
    doc_context: Optional[str] = None
    file_ids: Optional[List[str]] = None

SYSTEM_AR = """اسمك Ahmed Wedad، مساعد طبي ذكي لطلاب كلية الطب في موريتانيا.
السنة: {year}
مهامك:
1. الإجابة من مقررات {year} فقط.
2. عند طلب QCM أجب بـ JSON فقط: {{"question":"...","options":["A","B","C","D"],"correct":0,"explanation":"..."}}
3. شرح المفاهيم الطبية بدقة.
4. إذا رُفع PDF اعتمد عليه أساساً.
قواعد: أجب بالعربية دائماً. JSON فقط للـ QCM بدون أي نص إضافي."""

SYSTEM_FR = """Tu t'appelles Ahmed Wedad, assistant médical pour les étudiants de médecine en Mauritanie.
Année: {year}
Missions:
1. Répondre depuis les cours de {year} uniquement.
2. Pour QCM réponds UNIQUEMENT en JSON: {{"question":"...","options":["A","B","C","D"],"correct":0,"explanation":"..."}}
3. Expliquer les concepts médicaux avec précision.
4. Si un PDF est fourni, base-toi dessus.
Règles: Réponds en français. JSON uniquement pour les QCM."""

def extract_pdf_text(content: bytes) -> str:
    if not HAS_PDF:
        return ""
    try:
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            pages = [p.extract_text() for p in pdf.pages[:30] if p.extract_text()]
            return "\n\n".join(pages)
    except:
        return ""

def upload_to_supabase(content, filename, year, subject):
    if not supabase:
        raise HTTPException(status_code=503, detail="Supabase غير مُعدّ")
    file_id = str(uuid.uuid4())
    path = f"{year}/{subject}/{file_id}_{filename.replace(' ','_')}"
    supabase.storage.from_("medetu-files").upload(path, content, {"content-type":"application/pdf"})
    url = supabase.storage.from_("medetu-files").get_public_url(path)
    supabase.table("files").insert({"id":file_id,"name":filename,"path":path,"url":url,"year":year,"subject":subject,"size":len(content)}).execute()
    return {"id":file_id,"name":filename,"url":url,"path":path}

@app.get("/")
def root():
    return {"status":"ok","app":"MedEtu API","version":"2.0.0","agent":"Ahmed Wedad"}

@app.get("/health")
def health():
    return {"status":"healthy","supabase":supabase is not None,"pdf_support":HAS_PDF}

@app.post("/api/chat")
async def chat(req: ChatRequest):
    base = SYSTEM_AR if req.lang=="ar" else SYSTEM_FR
    system = base.format(year=req.year)

    if req.file_ids and supabase:
        try:
            rows = supabase.table("files").select("name,extracted_text").in_("id",req.file_ids).execute()
            for r in rows.data:
                if r.get("extracted_text"):
                    system += f"\n\n--- {r['name']} ---\n{r['extracted_text'][:4000]}"
        except:
            pass

    if req.doc_context:
        system += f"\n\n--- محتوى الملف ---\n{req.doc_context[:8000]}"

    # بناء تاريخ المحادثة لـ Gemini
    history = []
    messages = req.messages
    for i, m in enumerate(messages[:-1]):
        role = "user" if m.role == "user" else "model"
        history.append({"role": role, "parts": [m.content]})

    last_msg = messages[-1].content if messages else ""
    full_prompt = f"{system}\n\n{last_msg}"

    try:
        if history:
            chat_session = model.start_chat(history=history)
            response = chat_session.send_message(full_prompt)
        else:
            response = model.generate_content(full_prompt)

        return {"content": response.text, "usage": {}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/upload")
async def upload_pdf(
    file: UploadFile = File(...),
    year: str = Form("PCEM1"),
    subject: str = Form("عام"),
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="يُسمح بملفات PDF فقط")
    content = await file.read()
    if len(content) > 20 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="الحجم يتجاوز 20MB")
    extracted = extract_pdf_text(content)
    result = upload_to_supabase(content, file.filename, year, subject)
    if extracted and supabase:
        supabase.table("files").update({"extracted_text":extracted[:50000]}).eq("id",result["id"]).execute()
    return {"id":result["id"],"name":file.filename,"url":result["url"],"year":year,"subject":subject,"size":len(content),"text_extracted":bool(extracted)}

@app.get("/api/files")
def get_files(year: Optional[str]=None, subject: Optional[str]=None):
    if not supabase:
        return {"files":[],"note":"Supabase غير مُعدّ"}
    try:
        q = supabase.table("files").select("id,name,url,year,subject,size,created_at")
        if year: q = q.eq("year",year)
        if subject: q = q.eq("subject",subject)
        return {"files": q.order("created_at",desc=True).execute().data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/files/{file_id}")
def delete_file(file_id: str):
    if not supabase:
        raise HTTPException(status_code=503, detail="Supabase غير مُعدّ")
    try:
        row = supabase.table("files").select("path").eq("id",file_id).single().execute()
        supabase.storage.from_("medetu-files").remove([row.data["path"]])
        supabase.table("files").delete().eq("id",file_id).execute()
        return {"deleted":True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
