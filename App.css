/* App.css */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:       #080c18;
  --bg2:      #0d1220;
  --surface:  #111827;
  --surface2: #161e30;
  --border:   rgba(74,144,255,0.12);
  --border2:  rgba(74,144,255,0.24);
  --accent:   #4a90ff;
  --accent2:  #7eb8ff;
  --gold:     #e8c97a;
  --green:    #4ecb8d;
  --red:      #ff6b7a;
  --purple:   #a78bfa;
  --text:     #e2e8f8;
  --text2:    #8a9bbf;
  --text3:    #4a5a7a;
  --r:        13px;
}

body { background: var(--bg); color: var(--text); font-family: 'Segoe UI', Tahoma, sans-serif; }

/* ── App ── */
.app { min-height: 100vh; display: flex; flex-direction: column; }

/* ── Header ── */
header {
  height: 58px; display: flex; align-items: center;
  justify-content: space-between; padding: 0 18px; gap: 12px;
  background: rgba(8,12,24,0.92); border-bottom: 1px solid var(--border);
  position: sticky; top: 0; z-index: 50; backdrop-filter: blur(16px);
}
.logo { display: flex; align-items: center; gap: 10px; flex-shrink: 0; }
.logo-icon { width: 34px; height: 34px; border-radius: 8px; font-size: 15px;
  background: linear-gradient(135deg, var(--accent), var(--purple));
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 3px 12px rgba(74,144,255,0.4); }
.logo-name { font-size: 16px; font-weight: 700; }
.logo-sub  { font-size: 9px; color: var(--text3); font-family: monospace; letter-spacing: 1.5px; }

.header-center { display: flex; gap: 4px; flex-wrap: wrap; justify-content: center; flex: 1; }
.year-btn { font-size: 11px; font-family: monospace; padding: 5px 10px; border-radius: 7px;
  border: 1px solid var(--border); background: transparent; color: var(--text3); cursor: pointer;
  transition: all .18s; }
.year-btn.active { background: var(--accent); color: #fff; border-color: var(--accent);
  box-shadow: 0 2px 10px rgba(74,144,255,0.35); }
.year-btn:hover:not(.active) { border-color: var(--border2); color: var(--text2); }

.lang-toggle { display: flex; gap: 3px; background: var(--surface); border-radius: 8px; padding: 3px; flex-shrink: 0; }
.lang-btn { font-size: 11px; font-family: monospace; letter-spacing: 1px; padding: 4px 9px;
  border-radius: 6px; border: none; cursor: pointer; transition: all .18s; }
.lang-btn.active  { background: var(--accent); color: #fff; }
.lang-btn:not(.active) { background: transparent; color: var(--text3); }

/* ── Banner ── */
.banner { margin: 16px 16px 0; padding: 18px 22px;
  background: linear-gradient(135deg,rgba(74,144,255,0.09),rgba(167,139,250,0.06));
  border: 1px solid var(--border2); border-radius: var(--r); position: relative; overflow: hidden; }
.banner-ghost { position: absolute; right: -8px; top: 50%; transform: translateY(-50%);
  font-size: 64px; font-weight: 900; color: rgba(74,144,255,0.05); pointer-events: none;
  white-space: nowrap; font-family: monospace; }
.year-badge { display: inline-flex; align-items: center; gap: 5px;
  background: rgba(74,144,255,0.15); border: 1px solid rgba(74,144,255,0.3);
  border-radius: 20px; padding: 3px 11px; font-size: 11px; color: var(--accent2);
  font-family: monospace; margin-bottom: 8px; }
.banner-title { font-size: 20px; font-weight: 700; margin-bottom: 3px; }
.banner-title span { color: var(--accent); }
.banner-desc { font-size: 12px; color: var(--text3); }
.stats-row { display: flex; gap: 22px; margin-top: 12px; flex-wrap: wrap; }
.stat-val   { font-size: 20px; font-weight: 700; color: var(--gold); }
.stat-label { font-size: 9px; color: var(--text3); font-family: monospace; letter-spacing: 1px; }

/* ── Main Grid ── */
.main-grid { display: grid; grid-template-columns: 1fr 350px; gap: 14px; padding: 14px 16px; flex: 1; }
@media (max-width: 820px) { .main-grid { grid-template-columns: 1fr; } }

/* ── Tabs ── */
.tabs { display: flex; gap: 4px; background: var(--surface); border-radius: 10px;
  padding: 4px; border: 1px solid var(--border); margin-bottom: 12px; flex-wrap: wrap; }
.tab { padding: 6px 15px; border-radius: 7px; border: none; cursor: pointer;
  font-family: inherit; font-size: 13px; transition: all .18s; }
.tab.active { background: var(--accent); color: #fff; box-shadow: 0 2px 10px rgba(74,144,255,0.35); }
.tab:not(.active) { background: transparent; color: var(--text3); }

/* ── Subject cards ── */
.sub-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px; }
.sub-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--r);
  padding: 13px 15px; cursor: pointer; transition: all .22s; position: relative; overflow: hidden; }
.sub-card:hover { border-color: var(--border2); transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(0,0,0,0.35); }
.sub-glow { position: absolute; top: 0; right: 0; width: 52px; height: 52px;
  background: radial-gradient(circle, var(--c,rgba(74,144,255,0.15)) 0%, transparent 70%); }
.sub-icon { font-size: 20px; margin-bottom: 7px; }
.sub-name { font-size: 13px; color: var(--text); margin-bottom: 2px; }
.sub-fr   { font-size: 10px; color: var(--text3); font-family: monospace; margin-bottom: 7px; }
.sub-meta { display: flex; gap: 10px; font-size: 10px; color: var(--text3); font-family: monospace; }
.sub-tag  { display: inline-block; font-size: 9px; font-family: monospace; padding: 2px 7px;
  border-radius: 4px; margin-top: 6px; border: 1px solid; }

/* ── Prof cards ── */
.prof-card { display: flex; align-items: center; gap: 11px; background: var(--surface);
  border: 1px solid var(--border); border-radius: 10px; padding: 11px 13px; margin-bottom: 7px;
  transition: border-color .18s; }
.prof-card:hover { border-color: var(--border2); }
.prof-av   { width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center;
  justify-content: center; font-size: 17px; border: 2px solid var(--border2); flex-shrink: 0; }
.prof-info { flex: 1; }
.prof-name { font-size: 13px; color: var(--text); }
.prof-sub  { font-size: 10px; color: var(--text3); font-family: monospace; }
.prof-docs { font-size: 10px; font-family: monospace; padding: 3px 8px; border-radius: 5px;
  background: rgba(78,203,141,0.1); color: var(--green); border: 1px solid rgba(78,203,141,0.2); }

/* ── Exam items ── */
.exam-item { display: flex; align-items: center; gap: 10px; background: var(--surface);
  border: 1px solid var(--border); border-radius: 10px; padding: 9px 13px; margin-bottom: 6px;
  cursor: pointer; transition: border-color .18s; }
.exam-item:hover { border-color: var(--border2); }
.exam-year { font-size: 10px; font-family: monospace; padding: 3px 7px; border-radius: 5px;
  background: rgba(232,201,122,0.1); color: var(--gold); border: 1px solid rgba(232,201,122,0.2); flex-shrink: 0; }
.exam-name { flex: 1; font-size: 12px; color: var(--text2); }
.exam-badges { display: flex; gap: 4px; }
.badge-pdf { font-size: 9px; font-family: monospace; padding: 2px 5px; border-radius: 4px;
  background: rgba(255,107,122,0.1); color: var(--red); border: 1px solid rgba(255,107,122,0.2); }
.badge-sol { font-size: 9px; font-family: monospace; padding: 2px 5px; border-radius: 4px;
  background: rgba(78,203,141,0.1); color: var(--green); border: 1px solid rgba(78,203,141,0.2); }
.badge-ai  { font-size: 9px; font-family: monospace; padding: 2px 5px; border-radius: 4px;
  background: rgba(167,139,250,0.1); color: var(--purple); border: 1px solid rgba(167,139,250,0.2); }

/* ── AI Panel ── */
.ai-panel { background: var(--bg2); border: 1px solid var(--border); border-radius: var(--r);
  display: flex; flex-direction: column;
  height: calc(100vh - 58px - 28px); position: sticky; top: 70px; overflow: hidden; }

.ai-head { display: flex; align-items: center; gap: 10px; padding: 13px 15px;
  border-bottom: 1px solid var(--border);
  background: linear-gradient(135deg,rgba(74,144,255,0.07),rgba(167,139,250,0.05)); }
.ai-orb  { width: 30px; height: 30px; border-radius: 50%; font-size: 12px; flex-shrink: 0;
  background: linear-gradient(135deg, var(--accent), var(--purple));
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 0 14px rgba(74,144,255,0.55); animation: pulse 2.5s ease-in-out infinite; }
.ai-name   { font-size: 14px; font-weight: 600; color: var(--text); }
.ai-status { font-size: 10px; color: var(--green); font-family: monospace;
  display: flex; align-items: center; gap: 4px; }
.status-dot { width: 5px; height: 5px; border-radius: 50%; background: var(--green);
  animation: blink 1.5s ease-in-out infinite; display: inline-block; }

.quick-row { display: flex; gap: 5px; padding: 7px 10px;
  border-bottom: 1px solid var(--border); flex-wrap: wrap; }
.q-btn { font-size: 11px; font-family: inherit; padding: 4px 8px; border-radius: 6px;
  border: 1px solid var(--border); background: var(--surface); color: var(--text2);
  cursor: pointer; transition: all .15s; white-space: nowrap; }
.q-btn:hover { border-color: var(--accent); color: var(--accent2); background: rgba(74,144,255,0.07); }

/* Messages */
.msgs { flex: 1; overflow-y: auto; padding: 10px 11px; display: flex;
  flex-direction: column; gap: 8px; scroll-behavior: smooth; }
.msgs::-webkit-scrollbar { width: 3px; }
.msgs::-webkit-scrollbar-thumb { background: var(--surface2); border-radius: 3px; }

.msg { display: flex; gap: 7px; align-items: flex-start; animation: msgIn .28s ease; }
.msg.user { flex-direction: row-reverse; }
@keyframes msgIn { from { opacity:0; transform:translateY(6px); } to { opacity:1; transform:none; } }

.msg-av { width: 26px; height: 26px; border-radius: 50%; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center; font-size: 11px; }
.msg.ai .msg-av { background: linear-gradient(135deg,var(--accent),var(--purple));
  box-shadow: 0 2px 8px rgba(74,144,255,0.35); }
.msg.user .msg-av { background: var(--surface2); border: 1px solid var(--border2); }

.msg-wrap { max-width: 87%; }
.msg-bubble { padding: 8px 11px; border-radius: 11px; font-size: 13px; line-height: 1.6; }
.msg.ai .msg-bubble { background: var(--surface2); border: 1px solid var(--border);
  border-radius: 3px 11px 11px 11px; }
.msg.user .msg-bubble { background: linear-gradient(135deg,rgba(74,144,255,0.22),rgba(74,144,255,0.13));
  border: 1px solid rgba(74,144,255,0.28); border-radius: 11px 3px 11px 11px; text-align: right; direction: rtl; }
.msg-src { font-size: 9px; color: var(--text3); font-family: monospace; margin-top: 3px; }

/* Typing */
.typing { display: flex; gap: 4px; align-items: center; }
.typing span { width: 6px; height: 6px; border-radius: 50%; background: var(--accent2);
  opacity: .5; animation: bounce 1.2s ease-in-out infinite; }
.typing span:nth-child(2) { animation-delay: .2s; }
.typing span:nth-child(3) { animation-delay: .4s; }

/* Input */
.input-area { padding: 9px 11px; border-top: 1px solid var(--border); }
.upload-row { display: flex; gap: 6px; margin-bottom: 6px; align-items: center; }
.upload-btn { display: flex; align-items: center; gap: 4px; font-size: 11px; font-family: monospace;
  padding: 4px 9px; border-radius: 7px; border: 1px solid var(--border);
  background: var(--surface); color: var(--text3); cursor: pointer; transition: all .15s; }
.upload-btn:hover { border-color: var(--border2); color: var(--text2); }
.doc-tag { display: flex; align-items: center; gap: 5px; font-size: 10px; font-family: monospace;
  padding: 3px 8px; border-radius: 5px; background: rgba(255,107,122,0.1);
  color: var(--red); border: 1px solid rgba(255,107,122,0.2); }
.doc-tag span { cursor: pointer; opacity: .7; margin-right: 2px; }
.doc-tag span:hover { opacity: 1; }

.input-row { display: flex; gap: 6px; align-items: flex-end; }
textarea { flex: 1; background: var(--surface); border: 1px solid var(--border);
  border-radius: 10px; color: var(--text); font-family: inherit; font-size: 13px;
  padding: 8px 11px; resize: none; outline: none; min-height: 38px; max-height: 110px;
  line-height: 1.5; transition: border .2s; direction: rtl; }
textarea:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(74,144,255,0.1); }
textarea::placeholder { color: var(--text3); }
.send-btn { width: 38px; height: 38px; border-radius: 9px; border: none; cursor: pointer;
  background: linear-gradient(135deg,var(--accent),var(--purple)); color: #fff;
  font-size: 14px; transition: all .18s; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center; }
.send-btn:hover:not(:disabled) { transform: scale(1.05); box-shadow: 0 3px 14px rgba(74,144,255,0.4); }
.send-btn:disabled { opacity: .45; cursor: not-allowed; }

/* ── QCM ── */
.qcm { font-size: 13px; }
.qcm-q { color: var(--gold); margin-bottom: 8px; font-weight: 600; }
.qcm-opts { display: flex; flex-direction: column; gap: 5px; }
.qcm-opt { display: flex; align-items: center; gap: 7px; padding: 6px 9px;
  border-radius: 7px; border: 1px solid var(--border);
  background: rgba(74,144,255,0.05); cursor: pointer; transition: all .15s; }
.qcm-opt:hover:not(.correct):not(.wrong) { border-color: var(--accent2); }
.qcm-opt.correct { border-color: var(--green); background: rgba(78,203,141,0.1); color: var(--green); }
.qcm-opt.wrong   { border-color: var(--red);   background: rgba(255,107,122,0.1); color: var(--red); }
.opt-letter { width: 18px; height: 18px; border-radius: 4px; font-size: 10px;
  background: rgba(74,144,255,0.12); display: flex; align-items: center;
  justify-content: center; flex-shrink: 0; color: var(--accent2); font-family: monospace; }
.qcm-result { margin-top: 8px; font-size: 12px; font-weight: 600; }
.qcm-result.ok { color: var(--green); }
.qcm-result.no { color: var(--red); }
.qcm-exp { margin-top: 5px; font-size: 11px; color: var(--text2); font-weight: 400;
  padding: 5px 8px; background: var(--surface2); border-radius: 6px; }

/* ── Modal ── */
.overlay { position: fixed; inset: 0; z-index: 200; background: rgba(0,0,0,0.72);
  backdrop-filter: blur(6px); display: flex; align-items: center; justify-content: center; }
.modal { background: var(--bg2); border: 1px solid var(--border2); border-radius: 16px;
  padding: 20px; width: 90%; max-width: 480px; max-height: 80vh; overflow-y: auto; }
.modal-head { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 16px; }
.modal-title { font-size: 16px; font-weight: 700; }
.modal-sub   { font-size: 10px; color: var(--text3); font-family: monospace; margin-top: 2px; }
.modal-close { width: 28px; height: 28px; border-radius: 7px; border: 1px solid var(--border);
  background: var(--surface); color: var(--text2); cursor: pointer; font-size: 12px; }
.file-item { display: flex; align-items: center; gap: 10px; background: var(--surface);
  border: 1px solid var(--border); border-radius: 9px; padding: 9px 12px; margin-bottom: 6px;
  cursor: pointer; transition: border-color .18s; }
.file-item:hover { border-color: var(--border2); }
.file-info { flex: 1; font-size: 12px; }
.file-meta { font-size: 9px; color: var(--text3); font-family: monospace; margin-top: 2px; }
.file-dl   { font-size: 10px; font-family: monospace; padding: 3px 8px; border-radius: 5px;
  background: rgba(74,144,255,0.1); color: var(--accent2); border: 1px solid rgba(74,144,255,0.2); }

/* ── Animations ── */
@keyframes pulse { 0%,100%{box-shadow:0 0 14px rgba(74,144,255,0.5)} 50%{box-shadow:0 0 22px rgba(74,144,255,0.8)} }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:.3} }
@keyframes bounce { 0%,80%,100%{transform:scale(.85);opacity:.4} 40%{transform:scale(1.1);opacity:1} }

/* ── Upload Modal ── */
.upload-modal { max-width: 480px; }
.drop-zone {
  border: 2px dashed rgba(74,144,255,0.3); border-radius: 12px;
  padding: 28px 20px; text-align: center; cursor: pointer;
  transition: all .2s; margin-bottom: 14px; background: rgba(74,144,255,0.03);
}
.drop-zone:hover, .drop-zone.has-file { border-color: rgba(74,144,255,0.6); background: rgba(74,144,255,0.07); }
.drop-icon  { font-size: 2.2rem; margin-bottom: 8px; }
.drop-hint  { color: var(--text2); font-size: 13px; }
.drop-sub   { font-size: 11px; color: var(--text3); margin-top: 4px; }
.drop-file  { display: flex; align-items: center; gap: 12px; text-align: right; }
.drop-file-icon { font-size: 2rem; flex-shrink: 0; }
.drop-file-name { font-size: 13px; color: var(--text); }
.drop-file-size { font-size: 10px; color: var(--text3); font-family: monospace; }
.drop-remove { margin-right: auto; background: none; border: none; color: var(--text3);
  cursor: pointer; font-size: 14px; padding: 4px 8px; }
.drop-remove:hover { color: var(--red); }

.upload-field { margin-bottom: 14px; }
.field-label  { display: block; font-size: 11px; color: var(--text3); font-family: monospace;
  letter-spacing: 1px; margin-bottom: 5px; }
.field-select {
  width: 100%; background: var(--surface); border: 1px solid var(--border);
  border-radius: 8px; color: var(--text); font-family: inherit; font-size: 13px;
  padding: 8px 11px; outline: none; cursor: pointer;
}
.field-select.sm { width: auto; min-width: 140px; padding: 5px 9px; font-size: 12px; }
.field-select:focus { border-color: var(--accent); }
.field-select option { background: var(--bg2); }

.progress-wrap  { margin-bottom: 10px; }
.progress-bar   { height: 4px; background: var(--accent); border-radius: 2px;
  transition: width .3s ease; }
.progress-label { font-size: 11px; color: var(--text3); font-family: monospace;
  margin-top: 4px; }

.upload-success { font-size: 13px; color: var(--green); margin-bottom: 10px;
  background: rgba(78,203,141,0.08); border: 1px solid rgba(78,203,141,0.2);
  border-radius: 8px; padding: 8px 12px; }
.upload-error   { font-size: 13px; color: var(--red); margin-bottom: 10px;
  background: rgba(255,107,122,0.08); border: 1px solid rgba(255,107,122,0.2);
  border-radius: 8px; padding: 8px 12px; }

.modal-actions { display: flex; gap: 8px; justify-content: flex-end; margin-top: 4px; }
.btn-cancel { padding: 8px 18px; border-radius: 8px; border: 1px solid var(--border);
  background: var(--surface); color: var(--text2); cursor: pointer; font-family: inherit;
  font-size: 13px; transition: all .18s; }
.btn-cancel:hover { border-color: var(--border2); }
.btn-upload { padding: 8px 18px; border-radius: 8px; border: none;
  background: linear-gradient(135deg, var(--accent), var(--purple));
  color: #fff; cursor: pointer; font-family: inherit; font-size: 13px;
  transition: all .18s; }
.btn-upload:hover:not(:disabled) { transform: scale(1.02); box-shadow: 0 3px 14px rgba(74,144,255,0.4); }
.btn-upload:disabled { opacity: .45; cursor: not-allowed; }

/* ── Header extras ── */
.header-years  { display: flex; gap: 4px; flex-wrap: wrap; justify-content: center; flex: 1; }
.header-right  { display: flex; align-items: center; gap: 8px; flex-shrink: 0; }
.upload-header-btn {
  font-size: 12px; font-family: inherit; padding: 6px 12px; border-radius: 8px;
  border: 1px solid rgba(74,144,255,0.3); background: rgba(74,144,255,0.1);
  color: var(--accent2); cursor: pointer; transition: all .18s; white-space: nowrap;
}
.upload-header-btn:hover { background: rgba(74,144,255,0.2); border-color: var(--accent); }

/* ── Files Panel ── */
.files-panel   { display: flex; flex-direction: column; gap: 10px; }
.files-toolbar { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 4px; }
.btn-refresh   { padding: 5px 9px; border-radius: 7px; border: 1px solid var(--border);
  background: var(--surface); color: var(--text3); cursor: pointer; font-size: 13px;
  transition: all .18s; }
.btn-refresh:hover { border-color: var(--border2); }
.btn-ask-files {
  padding: 5px 12px; border-radius: 7px; border: 1px solid rgba(167,139,250,0.3);
  background: rgba(167,139,250,0.1); color: var(--purple); cursor: pointer;
  font-family: inherit; font-size: 12px; transition: all .18s;
}
.btn-ask-files:hover { background: rgba(167,139,250,0.2); }

.files-loading { font-size: 13px; color: var(--text3); padding: 20px; text-align: center; }
.files-empty   { text-align: center; padding: 28px 16px; }
.empty-icon    { font-size: 2.5rem; margin-bottom: 10px; }
.empty-sub     { font-size: 11px; color: var(--text3); margin-top: 4px; }
.files-list    { display: flex; flex-direction: column; gap: 6px; }

.file-row {
  display: flex; align-items: center; gap: 10px; background: var(--surface);
  border: 1px solid var(--border); border-radius: 10px; padding: 9px 12px;
  transition: all .18s;
}
.file-row:hover    { border-color: var(--border2); }
.file-row.selected { border-color: rgba(167,139,250,0.4); background: rgba(167,139,250,0.06); }

.file-check  { cursor: pointer; flex-shrink: 0; }
.check-box   { width: 18px; height: 18px; border-radius: 5px; border: 1.5px solid var(--border2);
  display: flex; align-items: center; justify-content: center; font-size: 11px;
  transition: all .15s; color: #fff; }
.check-box.checked { background: var(--purple); border-color: var(--purple); }

.file-icon-wrap { font-size: 1.3rem; flex-shrink: 0; }
.file-info      { flex: 1; min-width: 0; }
.file-name      { font-size: 12px; color: var(--text); white-space: nowrap;
  overflow: hidden; text-overflow: ellipsis; }
.file-meta      { display: flex; gap: 6px; font-size: 10px; color: var(--text3);
  font-family: monospace; margin-top: 2px; flex-wrap: wrap; }
.file-subject   { background: rgba(74,144,255,0.1); color: var(--accent2);
  border: 1px solid rgba(74,144,255,0.2); padding: 1px 5px; border-radius: 4px; }
.file-actions   { display: flex; gap: 5px; flex-shrink: 0; }
.btn-file-dl, .btn-file-del {
  width: 28px; height: 28px; border-radius: 7px; border: 1px solid var(--border);
  background: var(--surface2); cursor: pointer; font-size: 13px; transition: all .15s;
  display: flex; align-items: center; justify-content: center; text-decoration: none; color: inherit;
}
.btn-file-dl:hover  { border-color: var(--accent); color: var(--accent2); }
.btn-file-del:hover { border-color: var(--red); color: var(--red); }

/* Active files badge in AI panel */
.active-files-badge {
  margin-right: auto; display: flex; align-items: center; gap: 5px;
  font-size: 10px; font-family: monospace; padding: 3px 8px; border-radius: 5px;
  background: rgba(167,139,250,0.1); color: var(--purple);
  border: 1px solid rgba(167,139,250,0.2);
}
.active-files-badge button { background: none; border: none; color: var(--purple);
  cursor: pointer; font-size: 11px; padding: 0 2px; }
