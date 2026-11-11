/* Explorador do MITRE Ecosystem Atlas. Escrito à mão; dados em assets/ecosystem.js (gerado).
   Sem dependências e sem servidor: funciona abrindo index.html direto do clone. */
(() => {
  "use strict";
  const DATA = window.ECOSYSTEM;
  if (!DATA) {
    document.querySelector("main").innerHTML = '<p class="empty">Não encontrei assets/ecosystem.js. Rode <code>python3 -m atlas build</code>.</p>';
    return;
  }
  const C = DATA.catalog, V = C.vocab, E = C.entries, UI = DATA.ui;
  const BY = Object.fromEntries(E.map(e => [e.id, e]));
  const ORDER = UI.order;
  const FLOW = ["adversario", "modelagem", "telemetria", "deteccao", "validacao", "resposta", "maturidade"];
  const SIDE = ["defesa", "engano"];
  const BASE = ["vulnerabilidade", "cti", "dados", "conformidade", "padrao", "formacao"];
  const STATUS_ICON = {"ativo": "●", "baixa-atividade": "◐", "parado": "○", "n/v": "?"};
  const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const $ = s => document.querySelector(s);
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c]));
  const icon = k => `<svg class="i" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${UI.layers[k].icon}</svg>`;
  const brDate = iso => iso ? iso.slice(0, 10).split("-").reverse().join("/") : "";
  const store = {
    get(k, d) { try { const v = localStorage.getItem("mitre-atlas:" + k); return v === null ? d : JSON.parse(v); } catch { return d; } },
    set(k, v) { try { localStorage.setItem("mitre-atlas:" + k, JSON.stringify(v)); } catch { /* sem armazenamento */ } }
  };
  const smooth = () => (REDUCED ? "auto" : "smooth");
  const docLink = p => `${UI.repo_url}/blob/main/${p}`;

  /* tema */
  const isDark = () => (document.documentElement.dataset.theme || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light")) === "dark";
  const themeLabel = () => { $("#theme-label").textContent = isDark() ? "Claro" : "Escuro"; };
  $("#theme").onclick = () => {
    const next = isDark() ? "light" : "dark";
    document.documentElement.dataset.theme = next; store.set("theme", next); themeLabel();
  };
  themeLabel();

  /* números e faixa de camadas */
  const cnt = (k, v) => E.filter(e => e[k] === v).length;
  const rels = E.reduce((a, e) => a + (e.relations || []).length, 0);
  $("#stats").innerHTML = [
    [E.length, "recursos"], [cnt("owner_type", "mitre"), "MITRE oficial"], [cnt("owner_type", "ctid"), "CTID"],
    [cnt("owner_type", "comunidade") + cnt("owner_type", "fornecedor"), "comunidade e fornecedores"],
    [rels, "relações"], [cnt("status", "ativo"), "ativos"], [C.historical.length, "históricos"]
  ].map(([n, l]) => `<div class="stat"><b>${n}</b><small>${l}</small></div>`).join("");
  $("#spectrum").innerHTML = ORDER.map(k => `<i class="l-${k}" style="flex:${Math.max(1, cnt("layer", k))}" title="${esc(UI.layers[k].title)}: ${cnt("layer", k)}"></i>`).join("");
  $("#foot").innerHTML = `<img src="assets/mark.svg" alt=""> <span>Revisão ${brDate(C.reviewed_on)} · ${E.length} recursos · schema ${esc(C.schema_version)}</span>
    <a href="${UI.repo_url}">Repositório</a><a href="${docLink("docs/catalogo.md")}">Catálogo</a>
    <a href="data/ecosystem.json">JSON</a><a href="data/ecosystem.csv">CSV</a><a href="${docLink("CONTRIBUTING.md")}">Contribuir</a>
    <span>${esc(UI.disclaimer[0].toUpperCase() + UI.disclaimer.slice(1))}.</span>`;

  /* filtros: estado espelhado na URL (#explorar?camada=deteccao&q=sigma) */
  const fill = (sel, label, dict, key, many) => {
    const counts = {};
    E.forEach(e => (many ? e[key] : [e[key]]).forEach(v => { counts[v] = (counts[v] || 0) + 1; }));
    $(sel).innerHTML = `<option value="">${label}</option>` + Object.entries(dict).filter(([k]) => counts[k])
      .map(([k, v]) => `<option value="${k}">${esc(v)} (${counts[k]})</option>`).join("");
  };
  fill("#f-owner", "Toda origem", V.owner_type, "owner_type");
  fill("#f-status", "Todo status", V.status, "status");
  fill("#f-domain", "Todo domínio", V.domains, "domains", true);
  const FIELDS = {q: "#q", owner: "#f-owner", status: "#f-status", domain: "#f-domain", prio: "#f-prio", sort: "#f-sort"};
  const PARAM = {q: "q", owner: "origem", status: "status", domain: "dominio", prio: "prio", sort: "ordem", layers: "camada"};
  const state = {layers: new Set(), q: "", owner: "", status: "", domain: "", prio: "", sort: "", focus: null};

  $("#layers").innerHTML = ORDER.filter(k => cnt("layer", k)).map(k =>
    `<button class="chip l-${k}" type="button" data-layer="${k}" aria-pressed="false" title="${esc(V.layer[k])}">${icon(k)}${esc(UI.layers[k].title)} <span class="n">${cnt("layer", k)}</span></button>`).join("");

  function syncControls() {
    Object.entries(FIELDS).forEach(([k, sel]) => { $(sel).value = state[k]; });
    document.querySelectorAll("#layers .chip").forEach(c => c.setAttribute("aria-pressed", state.layers.has(c.dataset.layer)));
  }
  function writeUrl() {
    const qs = new URLSearchParams();
    Object.keys(FIELDS).forEach(k => { if (state[k]) qs.set(PARAM[k], state[k]); });
    if (state.layers.size) qs.set(PARAM.layers, [...state.layers].join(","));
    const h = state.focus ? `#e/${state.focus}` : "#explorar" + (qs.toString() ? "?" + qs : "");
    if (location.hash !== h) history.replaceState(null, "", h);
  }
  function readUrl(query) {
    const qs = new URLSearchParams(query || "");
    Object.keys(FIELDS).forEach(k => { state[k] = qs.get(PARAM[k]) || ""; });
    state.layers = new Set((qs.get(PARAM.layers) || "").split(",").filter(k => ORDER.includes(k)));
  }
  const changed = () => { state.focus = null; writeUrl(); render(); };

  $("#layers").addEventListener("click", ev => {
    const b = ev.target.closest(".chip"); if (!b) return;
    const k = b.dataset.layer;
    if (state.layers.has(k)) state.layers.delete(k); else state.layers.add(k);
    b.setAttribute("aria-pressed", state.layers.has(k)); changed();
  });
  Object.entries(FIELDS).forEach(([k, sel]) => $(sel).addEventListener("input", ev => { state[k] = ev.target.value; changed(); }));
  $("#clear").onclick = () => {
    Object.keys(FIELDS).forEach(k => { state[k] = ""; }); state.layers.clear(); syncControls(); changed();
  };
  addEventListener("keydown", ev => {
    const typing = /^(INPUT|SELECT|TEXTAREA)$/.test(document.activeElement?.tagName);
    if (ev.key === "/" && !typing) { ev.preventDefault(); location.hash.startsWith("#explorar") || (location.hash = "#explorar"); $("#q").focus(); }
    if (ev.key === "Escape" && document.activeElement === $("#q") && state.q) { state.q = ""; $("#q").value = ""; changed(); }
  });

  const norm = s => String(s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  const hay = e => norm([e.id, e.name, e.origin, e.purpose, e.output, e.notes, e.version, (e.formats || []).join(" "),
    V.layer[e.layer], UI.layers[e.layer].title, e.domains.map(d => V.domains[d]).join(" ")].join(" "));
  const HAY = Object.fromEntries(E.map(e => [e.id, hay(e)]));
  const recentCut = (() => { const d = new Date(C.reviewed_on + "T12:00:00"); d.setDate(d.getDate() - 14); return d.toISOString().slice(0, 10); })();

  function card(e) {
    const st = e.status === "n/v" ? "nv" : e.status;
    const rel = (e.relations || []).filter(r => BY[r]).map(r => `<button class="rel" type="button" data-go="${r}" title="${esc(BY[r].purpose)}">${esc(BY[r].name)}</button>`).join("");
    const extra = [e.notes ? `<p>${esc(e.notes)}</p>` : "", e.formats ? `<p><b>Formatos:</b> ${esc(e.formats.join(" · "))}</p>` : "",
      e.license_api ? `<p><b>Licença (API):</b> ${esc(e.license_api)}</p>` : "", e.pushed_at ? `<p><b>Último push:</b> ${brDate(e.pushed_at)}</p>` : "",
      `<p><b>Revisado em:</b> ${brDate(e.reviewed_on)} · ${esc(e.verification)}</p>`].join("");
    const isNew = e.reviewed_on >= recentCut;
    return `<article class="card l-${e.layer}${state.focus === e.id ? " focus" : ""}" id="${e.id}">
      <div class="top-line"><span class="id">${icon(e.layer)}${e.id} · ${esc(UI.layers[e.layer].title)}</span><button class="copy" type="button" data-copy="${e.id}" title="Copiar link para ${esc(e.name)}">copiar link</button></div>
      <h3><a href="${esc(e.url)}" target="_blank" rel="noopener">${esc(e.name)}</a></h3>
      <div class="badges"><span class="b${e.priority === "P1" ? " p1" : ""}">${e.priority}</span>${isNew ? `<span class="b new">revisado ${brDate(e.reviewed_on).slice(0, 5)}</span>` : ""}<span class="b">${esc(V.owner_type[e.owner_type])}</span><span class="b st-${st}">${STATUS_ICON[e.status]} ${esc(V.status[e.status])}</span>${e.domains.map(d => `<span class="b">${esc(V.domains[d])}</span>`).join("")}</div>
      ${e.version ? `<div class="ver">${esc(e.version)}</div>` : ""}
      <p>${esc(e.purpose)}</p>
      <p class="out">→ ${esc(e.output)}</p>
      <details><summary>detalhes${rel ? " e relações" : ""}</summary>${extra}${rel ? `<div class="rels">${rel}</div>` : ""}</details>
    </article>`;
  }

  const SORTS = {
    "": (a, b) => ORDER.indexOf(a.layer) - ORDER.indexOf(b.layer) || a.priority.localeCompare(b.priority) || a.name.localeCompare(b.name, "pt"),
    recentes: (a, b) => b.reviewed_on.localeCompare(a.reviewed_on) || a.name.localeCompare(b.name, "pt"),
    nome: (a, b) => a.name.localeCompare(b.name, "pt")
  };
  function render() {
    let list;
    if (state.focus) {
      const f = BY[state.focus], ids = new Set([f.id, ...(f.relations || [])]);
      E.forEach(e => { if ((e.relations || []).includes(f.id)) ids.add(e.id); });
      list = E.filter(e => ids.has(e.id));
    } else {
      const terms = norm(state.q).split(/\s+/).filter(Boolean);
      list = E.filter(e => (!state.layers.size || state.layers.has(e.layer)) && (!state.owner || e.owner_type === state.owner)
        && (!state.status || e.status === state.status) && (!state.domain || e.domains.includes(state.domain))
        && (!state.prio || e.priority === state.prio) && terms.every(t => HAY[e.id].includes(t)));
    }
    const sort = SORTS[state.sort] || SORTS[""];
    list = [...list].sort((a, b) => (a.id === state.focus ? -1 : b.id === state.focus ? 1 : 0) || sort(a, b));
    $("#count").innerHTML = state.focus
      ? `<b>${esc(BY[state.focus].name)}</b> e ${list.length - 1} recursos relacionados · <button class="linkbtn" type="button" id="unfocus">ver todos</button>`
      : `${list.length} de ${E.length} recursos`;
    $("#grid").innerHTML = list.length ? list.map(card).join("") : `<div class="empty">Nada encontrado. Tente outro termo ou limpe os filtros.</div>`;
    const u = $("#unfocus"); if (u) u.onclick = () => { state.focus = null; writeUrl(); render(); };
  }
  $("#grid").addEventListener("click", async ev => {
    const go = ev.target.closest("[data-go]");
    if (go) {
      state.focus = go.dataset.go; writeUrl(); render();
      document.getElementById(state.focus)?.scrollIntoView({behavior: smooth(), block: "center"});
      return;
    }
    const cp = ev.target.closest("[data-copy]");
    if (cp) {
      const url = location.href.split("#")[0] + "#e/" + cp.dataset.copy;
      try { await navigator.clipboard.writeText(url); cp.textContent = "copiado ✓"; } catch { cp.textContent = "#e/" + cp.dataset.copy; }
      setTimeout(() => { cp.textContent = "copiar link"; }, 1600);
    }
  });

  /* mapa */
  function layerBox(k) {
    const items = E.filter(e => e.layer === k).sort((a, b) => a.priority.localeCompare(b.priority) || a.name.localeCompare(b.name, "pt"));
    return `<button class="layer l-${k}" type="button" data-layer="${k}"><span class="hd"><b>${icon(k)}${esc(UI.layers[k].title)}</b><span class="n">${items.length}</span></span>
      <small class="out">${esc(V.layer[k])}</small><ul>${items.slice(0, 4).map(e => `<li>${esc(e.name)}</li>`).join("")}</ul></button>`;
  }
  $("#map-main").innerHTML = FLOW.map(layerBox).join("");
  $("#map-side").innerHTML = SIDE.map(layerBox).join("");
  $("#map-base").innerHTML = BASE.map(layerBox).join("");
  $("#tab-mapa").addEventListener("click", ev => {
    const b = ev.target.closest(".layer"); if (!b) return;
    Object.keys(FIELDS).forEach(k => { state[k] = ""; });
    state.layers = new Set([b.dataset.layer]); state.focus = null;
    location.hash = "#explorar?" + PARAM.layers + "=" + b.dataset.layer;
  });

  /* trilha: uma ação por vez */
  const T = DATA.trilha, STEPS = T.semanas.flatMap(s => s.acoes.map(a => ({...a, semana: s})));
  let done = new Set(store.get("done", []));
  let cur = store.get("cur", null);
  const firstOpen = () => (STEPS.find(s => !done.has(s.id)) || STEPS[STEPS.length - 1]).id;
  if (!STEPS.some(s => s.id === cur)) cur = firstOpen();
  const save = () => { store.set("done", [...done]); store.set("cur", cur); };
  function renderTrilha() {
    const i = STEPS.findIndex(s => s.id === cur), s = STEPS[i], pct = Math.round(100 * done.size / STEPS.length);
    const refs = (s.ref || []).filter(r => BY[r]).map(r => `<a href="${esc(BY[r].url)}" target="_blank" rel="noopener">${esc(BY[r].name)}</a>`).join(" · ");
    const all = done.size === STEPS.length;
    $("#now").innerHTML = `
      <div class="week">Semana ${s.semana.n} de ${T.semanas.length} · ${esc(s.semana.tema)} · ação ${esc(s.id)}</div>
      <h2>${all ? "Trilha concluída. " : ""}${esc(s.texto)}</h2>
      <p class="deliv">Entrega da semana: ${esc(s.semana.entrega)}</p>
      ${s.cmd ? `<div class="cmd"><code>${esc(s.cmd)}</code><button class="btn" type="button" id="copy">Copiar</button></div>` : ""}
      ${refs ? `<p>Use: ${refs}</p>` : ""}
      <div class="bar" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${pct}" aria-label="Progresso da trilha"><i style="width:${pct}%"></i></div><small>${done.size} de ${STEPS.length} ações feitas (${pct}%)</small>
      <div class="actions">
        <button class="btn primary" type="button" id="ok">${done.has(s.id) ? "Feita · ir para a próxima" : "Feito · próxima"}</button>
        <button class="btn" type="button" id="skip">Pular por agora</button>
        <button class="btn" type="button" id="back" ${i === 0 ? "disabled" : ""}>Anterior</button>
        <button class="btn" type="button" id="reset">Recomeçar</button>
      </div>`;
    $("#weeks").innerHTML = T.semanas.map(w => `<div class="wk"><h4>${w.n}. ${esc(w.tema)}</h4><ol>${w.acoes.map(a =>
      `<li class="${done.has(a.id) ? "done" : ""} ${a.id === cur ? "cur" : ""}"><button type="button" data-step="${a.id}">${esc(a.texto.length > 70 ? a.texto.slice(0, 68) + "…" : a.texto)}</button></li>`).join("")}</ol></div>`).join("");
    const go = j => { cur = STEPS[Math.max(0, Math.min(STEPS.length - 1, j))].id; save(); renderTrilha(); };
    $("#ok").onclick = () => { done.add(s.id); const nx = STEPS.findIndex((x, k) => k > i && !done.has(x.id)); cur = nx >= 0 ? STEPS[nx].id : firstOpen(); save(); renderTrilha(); };
    $("#skip").onclick = () => go(i + 1);
    $("#back").onclick = () => go(i - 1);
    $("#reset").onclick = () => { if (confirm("Apagar o progresso salvo neste navegador?")) { done = new Set(); cur = STEPS[0].id; save(); renderTrilha(); } };
    const cp = $("#copy");
    if (cp) cp.onclick = async () => { try { await navigator.clipboard.writeText(s.cmd); cp.textContent = "Copiado"; } catch { cp.textContent = "Selecione e copie"; } };
  }
  $("#weeks").addEventListener("click", ev => {
    const b = ev.target.closest("[data-step]");
    if (b) { cur = b.dataset.step; save(); renderTrilha(); scrollTo({top: 0, behavior: smooth()}); }
  });

  /* migração */
  function renderMig() {
    const q = norm($("#mq").value);
    const rows = DATA.substituicoes.filter(r => !q || norm(Object.values(r).join(" ")).includes(q));
    const link = id => id ? `<a href="https://attack.mitre.org/techniques/${id.replace(".", "/")}/" target="_blank" rel="noopener"><code>${esc(id)}</code></a>` : "—";
    $("#mig").innerHTML = rows.map(r => `<tr><td>${link(r.id_antigo)}</td><td>${esc(r.nome_antigo)}</td><td>${link(r.id_novo)}</td><td>${esc(r.nome_novo)}</td></tr>`).join("")
      || `<tr><td colspan="4">Nada encontrado.</td></tr>`;
  }
  $("#mq").addEventListener("input", renderMig);

  /* rotas: #explorar[?filtros] · #e/E001 · #mapa · #trilha · #migracao */
  function route() {
    const h = location.hash.slice(1) || "explorar";
    const [path, query] = h.split("?");
    let tab = path.split("/")[0];
    if (tab === "e") { const id = path.split("/")[1]; state.focus = BY[id] ? id : null; tab = "explorar"; }
    else if (tab === "explorar") { state.focus = null; readUrl(query); }
    if (!["explorar", "mapa", "trilha", "migracao"].includes(tab)) tab = "explorar";
    document.querySelectorAll("main > section").forEach(s => { s.hidden = s.id !== "tab-" + tab; });
    document.querySelectorAll("nav.tabs a").forEach(a => {
      if (a.dataset.tab === tab) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
    });
    if (tab === "explorar") {
      syncControls(); render();
      document.querySelector("#layers .chip[aria-pressed=true]")?.scrollIntoView({inline: "center", block: "nearest"});
      if (state.focus) setTimeout(() => document.getElementById(state.focus)?.scrollIntoView({block: "center"}), 30);
    }
    if (tab === "trilha") renderTrilha();
    if (tab === "migracao") renderMig();
  }
  addEventListener("hashchange", route);
  route();
})();
