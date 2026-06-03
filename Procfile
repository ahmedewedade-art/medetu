import { useState, useRef, useEffect, useCallback } from "react";
import { sendChat, uploadPDF, getFiles, deleteFile } from "./api";
import "./App.css";

// ── DATA ──
const YEARS = ["PCEM1","PCEM2","DCEM1","DCEM2","DCEM3","DCEM4"];

const SUBJECTS = {
  PCEM1: [
    { icon:"🔬", ar:"بيولوجيا الخلية",  fr:"Biologie Cellulaire", prof:"Pr. Diagana",    color:"#4a90ff", tag:"UE1" },
    { icon:"🧬", ar:"بيوكيميا",          fr:"Biochimie",           prof:"Pr. Sow",        color:"#4ecb8d", tag:"UE2" },
    { icon:"🫀", ar:"فيزيولوجيا",        fr:"Physiologie",         prof:"Pr. Mint Ahmed", color:"#e8c97a", tag:"UE3" },
    { icon:"⚗️", ar:"كيمياء عامة",       fr:"Chimie Générale",     prof:"Pr. Ba",         color:"#a78bfa", tag:"UE1" },
    { icon:"🦴", ar:"تشريح",             fr:"Anatomie",            prof:"Pr. Diallo",     color:"#ff6b7a", tag:"UE4" },
    { icon:"🧪", ar:"بيوفيزياء",         fr:"Biophysique",         prof:"Pr. Cheikh",     color:"#38bdf8", tag:"UE2" },
    { icon:"📊", ar:"إحصاء طبي",         fr:"Biostatistiques",     prof:"Pr. Ndiaye",     color:"#fb923c", tag:"UE5" },
    { icon:"🌍", ar:"علم الأوبئة",       fr:"Épidémiologie",       prof:"Pr. Ould Bah",   color:"#34d399", tag:"UE5" },
  ],
  PCEM2: [
    { icon:"🧠", ar:"علم الأعصاب",       fr:"Neurologie",          prof:"Pr. Diallo",     color:"#a78bfa", tag:"UE1" },
    { icon:"🩸", ar:"أمراض الدم",        fr:"Hématologie",         prof:"Pr. Sow",        color:"#ff6b7a", tag:"UE2" },
    { icon:"💊", ar:"صيدلة",             fr:"Pharmacologie",       prof:"Pr. Ba",         color:"#4ecb8d", tag:"UE3" },
    { icon:"🔭", ar:"هيستولوجيا",        fr:"Histologie",          prof:"Pr. Cheikh",     color:"#e8c97a", tag:"UE1" },
    { icon:"🫁", ar:"أمراض التنفس",      fr:"Pneumologie",         prof:"Pr. Mint Ahmed", color:"#4a90ff", tag:"UE4" },
  ],
  DCEM1: [
    { icon:"🏥", ar:"طب داخلي",          fr:"Médecine Interne",    prof:"Pr. Diagana",    color:"#4a90ff", tag:"UE1" },
    { icon:"🔪", ar:"جراحة عامة",        fr:"Chirurgie Générale",  prof:"Pr. Ba",         color:"#ff6b7a", tag:"UE2" },
    { icon:"👶", ar:"طب الأطفال",        fr:"Pédiatrie",           prof:"Pr. Sow",        color:"#4ecb8d", tag:"UE3" },
    { icon:"🤰", ar:"أمراض النساء",      fr:"Gynécologie",         prof:"Pr. Mint Ahmed", color:"#e8c97a", tag:"UE4" },
  ],
};
["DCEM2","DCEM3","DCEM4"].forEach(y => { SUBJECTS[y] = SUBJECTS.DCEM1; });

const QUICK = {
  ar: ["📝 أنشئ QCM","📖 اشرح مفهوماً","🔍 أهم النقاط","🧠 اختبرني","📋 ملخص الدرس"],
  fr: ["📝 Générer QCM","📖 Expliquer concept","🔍 Points clés","🧠 Me tester","📋 Résumé du cours"],
};

// ── QCM ──
function QCMCard({ data }) {
  const [sel, setSel] = useState(null);
  const opts = ["A","B","C","D"];
  return (
    <div className="qcm">
      <div className="qcm-q">❓ {data.question}</div>
      <div className="qcm-opts">
        {data.options.map((o,i) => {
          let cls = "qcm-opt";
          if (sel !== null) {
            if (i === data.correct) cls += " correct";
            else if (i === sel)     cls += " wrong";
          }
          return (
            <div key={i} className={cls} onClick={() => sel===null && setSel(i)}>
              <span className="opt-letter">{opts[i]}</span>{o}
            </div>
          );
        })}
      </div>
      {sel !== null && (
        <div className={`qcm-result ${sel===data.correct?"ok":"no"}`}>
          {sel===data.correct ? "✅ إجابة صحيحة!" : `❌ الصواب: ${opts[data.correct]}`}
          {data.explanation && <div className="qcm-exp">💡 {data.explanation}</div>}
        </div>
      )}
    </div>
  );
}

// ── Message ──
function Msg({ m }) {
  const isUser = m.role === "user";
  let qcm = null;
  const trimmed = m.content.trim();
  if (!isUser && trimmed.startsWith("{") && trimmed.includes('"question"')) {
    try { qcm = JSON.parse(trimmed); } catch(e) {}
  }
  const fmt = s => s.split("\n").map((l,i,arr) => (
    <span key={i}>
      {l.split(/(\*\*[^*]+\*\*)/g).map((p,j) =>
        p.startsWith("**") ? <strong key={j}>{p.slice(2,-2)}</strong> : p)}
      {i < arr.length-1 && <br/>}
    </span>
  ));
  return (
    <div className={`msg ${isUser?"user":"ai"}`}>
      <div className="msg-av">{isUser ? "👤" : "🩺"}</div>
      <div className="msg-wrap">
        <div className="msg-bubble">{qcm ? <QCMCard data={qcm}/> : fmt(m.content)}</div>
        {m.source && <div className="msg-src">📚 {m.source}</div>}
      </div>
    </div>
  );
}

// ── Upload Modal ──
function UploadModal({ open, onClose, year, subjects, lang, onUploaded }) {
  const [file,       setFile]       = useState(null);
  const [subject,    setSubject]    = useState("");
  const [uploading,  setUploading]  = useState(false);
  const [progress,   setProgress]   = useState(0);
  const [error,      setError]      = useState("");
  const [success,    setSuccess]    = useState(false);
  const dropRef = useRef(null);
  const t = (a,f) => lang==="ar" ? a : f;

  useEffect(() => { if (open) { setFile(null); setError(""); setSuccess(false); setProgress(0); }}, [open]);

  const handleDrop = useCallback(e => {
    e.preventDefault();
    const f = e.dataTransfer.files[0];
    if (f?.name.endsWith(".pdf")) setFile(f);
    else setError(t("يُسمح بملفات PDF فقط","Fichiers PDF uniquement"));
  }, [lang]);

  const doUpload = async () => {
    if (!file || !subject) { setError(t("اختر الملف والمادة","Choisissez le fichier et la matière")); return; }
    setUploading(true); setError(""); setProgress(10);
    try {
      const interval = setInterval(() => setProgress(p => Math.min(p+8, 85)), 300);
      const result = await uploadPDF(file, year, subject);
      clearInterval(interval); setProgress(100); setSuccess(true);
      setTimeout(() => { onUploaded(result); onClose(); }, 1200);
    } catch(e) {
      setError(e.message);
    }
    setUploading(false);
  };

  if (!open) return null;
  return (
    <div className="overlay" onClick={e=>e.target===e.currentTarget&&onClose()}>
      <div className="modal upload-modal">
        <div className="modal-head">
          <div>
            <div className="modal-title">📤 {t("رفع ملف PDF","Téléverser un PDF")}</div>
            <div className="modal-sub">{year}</div>
          </div>
          <button className="modal-close" onClick={onClose}>✕</button>
        </div>

        {/* Drop zone */}
        <div
          ref={dropRef}
          className={`drop-zone ${file?"has-file":""}`}
          onDrop={handleDrop}
          onDragOver={e=>e.preventDefault()}
          onClick={() => !file && document.getElementById("pdf-input").click()}
        >
          <input id="pdf-input" type="file" accept=".pdf" style={{display:"none"}}
            onChange={e => setFile(e.target.files[0])}/>
          {file ? (
            <div className="drop-file">
              <span className="drop-file-icon">📄</span>
              <div>
                <div className="drop-file-name">{file.name}</div>
                <div className="drop-file-size">{(file.size/1024/1024).toFixed(2)} MB</div>
              </div>
              <button className="drop-remove" onClick={e=>{e.stopPropagation();setFile(null);}}>✕</button>
            </div>
          ) : (
            <div className="drop-hint">
              <div className="drop-icon">📂</div>
              <div>{t("اسحب PDF هنا أو اضغط للاختيار","Glissez un PDF ici ou cliquez")}</div>
              <div className="drop-sub">{t("الحد الأقصى: 20 MB","Max: 20 MB")}</div>
            </div>
          )}
        </div>

        {/* Subject select */}
        <div className="upload-field">
          <label className="field-label">{t("المادة","Matière")}</label>
          <select className="field-select" value={subject} onChange={e=>setSubject(e.target.value)}>
            <option value="">{t("— اختر المادة —","— Choisir la matière —")}</option>
            {subjects.map((s,i) => (
              <option key={i} value={s.ar}>{lang==="ar" ? s.ar : s.fr}</option>
            ))}
            <option value="عام">{t("عام","Général")}</option>
          </select>
        </div>

        {/* Progress */}
        {uploading && (
          <div className="progress-wrap">
            <div className="progress-bar" style={{width:`${progress}%`}}/>
            <div className="progress-label">{progress < 100 ? t("جاري الرفع...","Téléversement...") : t("تم! ✅","Fait! ✅")}</div>
          </div>
        )}

        {success && <div className="upload-success">✅ {t("تم رفع الملف بنجاح!","Fichier uploadé avec succès!")}</div>}
        {error   && <div className="upload-error">⚠️ {error}</div>}

        <div className="modal-actions">
          <button className="btn-cancel" onClick={onClose} disabled={uploading}>
            {t("إلغاء","Annuler")}
          </button>
          <button className="btn-upload" onClick={doUpload} disabled={uploading||!file||!subject}>
            {uploading ? t("جاري الرفع...","En cours...") : t("رفع الملف ⬆","Téléverser ⬆")}
          </button>
        </div>
      </div>
    </div>
  );
}

// ── Files Panel ──
function FilesPanel({ year, subjects, lang, onAskAbout }) {
  const [files,    setFiles]    = useState([]);
  const [loading,  setLoading]  = useState(false);
  const [filterS,  setFilterS]  = useState("");
  const [selected, setSelected] = useState([]);
  const t = (a,f) => lang==="ar" ? a : f;

  const load = useCallback(async () => {
    setLoading(true);
    try {
      const data = await getFiles(year, filterS || null);
      setFiles(data.files || []);
    } catch(e) { setFiles([]); }
    setLoading(false);
  }, [year, filterS]);

  useEffect(() => { load(); }, [load]);

  const handleDelete = async (id) => {
    if (!window.confirm(t("هل تريد حذف هذا الملف؟","Supprimer ce fichier?"))) return;
    try {
      await deleteFile(id);
      setFiles(f => f.filter(x => x.id !== id));
      setSelected(s => s.filter(x => x !== id));
    } catch(e) { alert(e.message); }
  };

  const toggleSelect = (id) =>
    setSelected(s => s.includes(id) ? s.filter(x=>x!==id) : [...s,id]);

  const fmt = (bytes) => bytes > 1024*1024
    ? `${(bytes/1024/1024).toFixed(1)} MB`
    : `${(bytes/1024).toFixed(0)} KB`;

  return (
    <div className="files-panel">
      <div className="files-toolbar">
        <select className="field-select sm" value={filterS} onChange={e=>setFilterS(e.target.value)}>
          <option value="">{t("كل المواد","Toutes")}</option>
          {subjects.map((s,i) => (
            <option key={i} value={s.ar}>{lang==="ar"?s.ar:s.fr}</option>
          ))}
        </select>
        <button className="btn-refresh" onClick={load}>🔄</button>
        {selected.length > 0 && (
          <button className="btn-ask-files"
            onClick={() => onAskAbout(selected, files.filter(f=>selected.includes(f.id)).map(f=>f.name))}>
            🤖 {t(`اسأل Ahmed Wedad عن ${selected.length} ملف`,`Demander à Ahmed Wedad (${selected.length})`)}
          </button>
        )}
      </div>

      {loading && <div className="files-loading">⏳ {t("جاري التحميل...","Chargement...")}</div>}

      {!loading && files.length === 0 && (
        <div className="files-empty">
          <div className="empty-icon">📭</div>
          <div>{t("لا توجد ملفات مرفوعة بعد","Aucun fichier téléversé")}</div>
          <div className="empty-sub">{t("ارفع أول PDF باستخدام الزر أعلاه","Uploadez votre premier PDF")}</div>
        </div>
      )}

      <div className="files-list">
        {files.map(f => (
          <div key={f.id} className={`file-row ${selected.includes(f.id)?"selected":""}`}>
            <div className="file-check" onClick={() => toggleSelect(f.id)}>
              <div className={`check-box ${selected.includes(f.id)?"checked":""}`}>
                {selected.includes(f.id) && "✓"}
              </div>
            </div>
            <div className="file-icon-wrap">📄</div>
            <div className="file-info">
              <div className="file-name">{f.name}</div>
              <div className="file-meta">
                <span className="file-subject">{f.subject}</span>
                <span>·</span>
                <span>{fmt(f.size)}</span>
                <span>·</span>
                <span>{new Date(f.created_at).toLocaleDateString(lang==="ar"?"ar-SA":"fr-FR")}</span>
              </div>
            </div>
            <div className="file-actions">
              <a href={f.url} target="_blank" rel="noreferrer" className="btn-file-dl"
                title={t("تحميل","Télécharger")}>⬇</a>
              <button className="btn-file-del" onClick={() => handleDelete(f.id)}
                title={t("حذف","Supprimer")}>🗑</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

// ── App ──
export default function App() {
  const [lang,        setLang]        = useState("ar");
  const [year,        setYear]        = useState("PCEM1");
  const [tab,         setTab]         = useState("subjects");
  const [msgs,        setMsgs]        = useState([]);
  const [input,       setInput]       = useState("");
  const [loading,     setLoading]     = useState(false);
  const [modal,       setModal]       = useState(null);
  const [uploadOpen,  setUploadOpen]  = useState(false);
  const [history,     setHistory]     = useState([]);
  const [activeFiles, setActiveFiles] = useState([]);  // file IDs للـ AI
  const [activeNames, setActiveNames] = useState([]);
  const msgsRef = useRef(null);
  const taRef   = useRef(null);

  const t = (a,f) => lang==="ar" ? a : f;
  const subjects = SUBJECTS[year] || SUBJECTS.PCEM1;

  // Welcome
  useEffect(() => {
    setMsgs([{ role:"assistant", content:
      t(`مرحباً! أنا **Ahmed Wedad** 🩺\nمساعدك الطبي الذكي لـ **${year}**\n\n• 📝 إنشاء QCM تفاعلية\n• 📖 شرح المفاهيم الطبية\n• 🔍 استخراج أهم النقاط\n• 📄 قراءة والإجابة من ملفاتك المرفوعة\n\nكيف أساعدك اليوم؟`,
        `Bonjour! Je suis **Ahmed Wedad** 🩺\nVotre assistant médical pour **${year}**\n\n• 📝 Générer des QCM interactifs\n• 📖 Expliquer les concepts médicaux\n• 🔍 Extraire les points essentiels\n• 📄 Lire et répondre depuis vos fichiers uploadés\n\nComment puis-je vous aider?`),
      source: null
    }]);
    setHistory([]); setActiveFiles([]); setActiveNames([]);
  }, [lang, year]);

  useEffect(() => {
    if (msgsRef.current) msgsRef.current.scrollTop = msgsRef.current.scrollHeight;
  }, [msgs, loading]);

  const sendMessage = async (overrideInput) => {
    const text = (overrideInput ?? input).trim();
    if (!text || loading) return;
    setInput(""); if (taRef.current) taRef.current.style.height = "38px";

    const newHistory = [...history, { role:"user", content:text }];
    setHistory(newHistory);
    setMsgs(prev => [...prev, { role:"user", content:text }]);
    setLoading(true);

    try {
      const data = await sendChat(newHistory, lang, year, null, activeFiles);
      const reply = data.content;
      setHistory(prev => [...prev, { role:"assistant", content:reply }]);
      const src = activeNames.length
        ? activeNames.join(" + ")
        : t(`قاعدة بيانات ${year}`, `Base ${year}`);
      setMsgs(prev => [...prev, { role:"assistant", content:reply, source:src }]);
    } catch(e) {
      setMsgs(prev => [...prev, {
        role:"assistant",
        content: t(`⚠️ خطأ: ${e.message}`,`⚠️ Erreur: ${e.message}`)
      }]);
    }
    setLoading(false);
  };

  const handleAskAbout = (ids, names) => {
    setActiveFiles(ids); setActiveNames(names);
    setTab("chat");
    const msg = lang==="ar"
      ? `اشرح لي محتوى الملفات التالية: ${names.join("، ")}`
      : `Explique-moi le contenu de ces fichiers: ${names.join(", ")}`;
    setTimeout(() => sendMessage(msg), 100);
  };

  return (
    <div className="app" dir={lang==="ar"?"rtl":"ltr"}>

      {/* Header */}
      <header>
        <div className="logo">
          <div className="logo-icon">🏥</div>
          <div>
            <div className="logo-name">MedEtu</div>
            <div className="logo-sub">FACULTÉ DE MÉDECINE</div>
          </div>
        </div>
        <div className="header-years">
          {YEARS.map(y => (
            <button key={y} className={`year-btn ${year===y?"active":""}`} onClick={()=>setYear(y)}>{y}</button>
          ))}
        </div>
        <div className="header-right">
          <button className="upload-header-btn" onClick={()=>setUploadOpen(true)}>
            📤 {t("رفع PDF","Upload PDF")}
          </button>
          <div className="lang-toggle">
            {["ar","fr"].map(l => (
              <button key={l} className={`lang-btn ${lang===l?"active":""}`} onClick={()=>setLang(l)}>
                {l.toUpperCase()}
              </button>
            ))}
          </div>
        </div>
      </header>

      {/* Banner */}
      <div className="banner">
        <div className="banner-ghost">{year}</div>
        <div className="year-badge">📅 {t("السنة الدراسية","Année")} 2024–2025</div>
        <div className="banner-title">{t("السنة","Année")} — <span>{year}</span></div>
        <div className="banner-desc">{t("كلية الطب · موريتانيا · مساعد Ahmed Wedad","Faculté de Médecine · Mauritanie · Ahmed Wedad")}</div>
        <div className="stats-row">
          {[[subjects.length, t("مادة","Matières")],[subjects.length,t("أستاذ","Profs")],["PDF",t("مكتبة","Bibliothèque")],["Ahmed Wedad","AI"]].map(([v,l],i)=>(
            <div key={i} className="stat">
              <div className="stat-val">{v}</div>
              <div className="stat-label">{l}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Main */}
      <div className="main-grid">
        <div className="left">
          <div className="tabs">
            {[
              [t("📚 المواد","📚 Matières"),"subjects"],
              [t("👨‍🏫 الأساتذة","👨‍🏫 Profs"),"profs"],
              [t("📝 الامتحانات","📝 Examens"),"exams"],
              [t("📂 الملفات","📂 Fichiers"),"files"],
            ].map(([lbl,id])=>(
              <button key={id} className={`tab ${tab===id?"active":""}`} onClick={()=>setTab(id)}>{lbl}</button>
            ))}
          </div>

          {tab==="subjects" && (
            <div className="sub-grid">
              {subjects.map((s,i)=>(
                <div key={i} className="sub-card" style={{"--c":s.color}} onClick={()=>setModal(i)}>
                  <div className="sub-glow"/>
                  <div className="sub-icon">{s.icon}</div>
                  <div className="sub-name">{s.ar}</div>
                  <div className="sub-fr">{s.fr}</div>
                  <div className="sub-meta"><span>👤 {s.prof.split(" ")[1]}</span></div>
                  <div className="sub-tag" style={{color:s.color,borderColor:s.color+"50",background:s.color+"15"}}>{s.tag}</div>
                </div>
              ))}
            </div>
          )}

          {tab==="profs" && subjects.map((s,i)=>(
            <div key={i} className="prof-card">
              <div className="prof-av">{s.icon}</div>
              <div className="prof-info">
                <div className="prof-name">{s.prof}</div>
                <div className="prof-sub">{lang==="ar"?s.ar:s.fr}</div>
              </div>
            </div>
          ))}

          {tab==="exams" && [2023,2022,2021].map(yr=>subjects.slice(0,4).map((s,i)=>(
            <div key={`${yr}-${i}`} className="exam-item">
              <div className="exam-year">{yr}</div>
              <div className="exam-name">{lang==="ar"?`امتحان ${s.ar}`:`Examen ${s.fr}`}</div>
              <div className="exam-badges">
                <span className="badge-pdf">PDF</span>
                {i%2===0 && <span className="badge-sol">{t("حل","Sol.")}</span>}
                <span className="badge-ai">AI</span>
              </div>
            </div>
          )))}

          {tab==="files" && (
            <FilesPanel
              year={year} subjects={subjects} lang={lang}
              onAskAbout={handleAskAbout}
            />
          )}
        </div>

        {/* AI Panel — Ahmed Wedad */}
        <div className="ai-panel">
          <div className="ai-head">
            <div className="ai-orb">🩺</div>
            <div>
              <div className="ai-name">Ahmed Wedad</div>
              <div className="ai-status">
                <span className="status-dot"/>
                {t(`متصل · ${year}`,"Connecté · "+year)}
              </div>
            </div>
            {activeFiles.length > 0 && (
              <div className="active-files-badge">
                📄 {activeFiles.length} {t("ملف نشط","fichier(s))")}
                <button onClick={()=>{setActiveFiles([]);setActiveNames([]);}}>✕</button>
              </div>
            )}
          </div>

          <div className="quick-row">
            {QUICK[lang].map((q,i)=>(
              <button key={i} className="q-btn"
                onClick={()=>{ setInput(q.replace(/^[^\s]+\s/,"")); taRef.current?.focus(); }}>
                {q}
              </button>
            ))}
          </div>

          <div className="msgs" ref={msgsRef}>
            {msgs.map((m,i)=><Msg key={i} m={m}/>)}
            {loading && (
              <div className="msg ai">
                <div className="msg-av">🩺</div>
                <div className="msg-bubble typing"><span/><span/><span/></div>
              </div>
            )}
          </div>

          <div className="input-area">
            <div className="input-row">
              <textarea ref={taRef} value={input}
                placeholder={t("اسأل Ahmed Wedad...","Demandez à Ahmed Wedad...")}
                onChange={e=>{
                  setInput(e.target.value);
                  e.target.style.height="38px";
                  e.target.style.height=Math.min(e.target.scrollHeight,110)+"px";
                }}
                onKeyDown={e=>{ if(e.key==="Enter"&&!e.shiftKey){e.preventDefault();sendMessage();}}}
              />
              <button className="send-btn" onClick={()=>sendMessage()}
                disabled={loading||!input.trim()}>➤</button>
            </div>
          </div>
        </div>
      </div>

      {/* Upload Modal */}
      <UploadModal
        open={uploadOpen} onClose={()=>setUploadOpen(false)}
        year={year} subjects={subjects} lang={lang}
        onUploaded={(f)=>{ if(tab!=="files") setTab("files"); }}
      />

      {/* Subject Modal */}
      {modal !== null && (
        <div className="overlay" onClick={e=>e.target===e.currentTarget&&setModal(null)}>
          <div className="modal">
            <div className="modal-head">
              <div>
                <div className="modal-title">{subjects[modal].icon} {subjects[modal].ar}</div>
                <div className="modal-sub">{subjects[modal].fr} · {subjects[modal].prof}</div>
              </div>
              <button className="modal-close" onClick={()=>setModal(null)}>✕</button>
            </div>
            <div className="files-empty" style={{padding:"2rem",textAlign:"center"}}>
              <div className="empty-icon">📂</div>
              <div>{t("ارفع ملفات هذه المادة باستخدام زر PDF","Uploadez les fichiers de cette matière")}</div>
              <button className="btn-upload" style={{marginTop:"1rem"}}
                onClick={()=>{setModal(null);setUploadOpen(true);}}>
                📤 {t("رفع PDF","Upload PDF")}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
