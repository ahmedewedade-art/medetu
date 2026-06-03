// src/api.js
const BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

/** إرسال رسالة لـ Ahmed Wedad */
export async function sendChat(messages, lang = "ar", year = "PCEM1", docContext = null, fileIds = []) {
  const res = await fetch(`${BASE_URL}/api/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      messages,
      lang,
      year,
      doc_context: docContext,
      file_ids: fileIds.length ? fileIds : null,
    }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

/** رفع PDF */
export async function uploadPDF(file, year, subject) {
  const form = new FormData();
  form.append("file", file);
  form.append("year", year);
  form.append("subject", subject);

  const res = await fetch(`${BASE_URL}/api/upload`, {
    method: "POST",
    body: form,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

/** جلب قائمة الملفات */
export async function getFiles(year = null, subject = null) {
  const params = new URLSearchParams();
  if (year)    params.set("year", year);
  if (subject) params.set("subject", subject);
  const res = await fetch(`${BASE_URL}/api/files?${params}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

/** حذف ملف */
export async function deleteFile(fileId) {
  const res = await fetch(`${BASE_URL}/api/files/${fileId}`, { method: "DELETE" });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

export async function checkHealth() {
  const res = await fetch(`${BASE_URL}/health`);
  return res.ok;
}
