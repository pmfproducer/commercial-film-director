"use strict";
const $ = id => document.getElementById(id);
const app = {csrf:"",projects:[],project:null,phase:null,tab:"documents",document:null,editing:false,runner:{},chatKey:"",busy:false,poll:false,fileKey:"",teamKey:""};
const phaseCopy = {
  "01_BRIEF_STRATEGY":["Briefing","O problema, a ideia inicial, o público e as condições do filme."],
  "02_CREATIVE_DIRECTION":["Rotas criativas","Mecanismos de história, papel da marca e a direção escolhida."],
  "03_SCRIPT":["Roteiro","A história em ação, seguida do roteiro de imagem, som e tempo."],
  "04_DIRECTOR_TREATMENT":["Tratamento","Ponto de vista, encenação, performance e a experiência do filme."],
  "05_VISUAL_SOUND_SYSTEM":["Imagem, arte e som","As escolhas de fotografia, arte, montagem e som discutidas pela equipe."],
  "06_DECOUPAGE":["Decupagem","Roteiro técnico e shot list com função, ação e duração de cada plano."],
  "07_ASSETS_CONTINUITY":["Assets e continuidade","Personagens, objetos, ambientes e os estados que precisam continuar coerentes."],
  "08_STORYBOARD_PREVIS":["Storyboard","Quadros, geografia, movimento e tempo para enxergar o filme antes da execução."],
  "09_AI_EXECUTION_PLAN":["Plano de produção","Recursos, pessoas, captação e uso de IA quando fizer sentido para o filme."],
  "10_SHOT_PACKETS":["Pacotes por plano","Instruções e referências reunidas para executar cada plano."],
  "11_POST_DELIVERY":["Montagem e pós","Estrutura da edição, desenho sonoro, cor, versões e entrega."],
  "12_QA_VERSIONS":["Revisão e versões","Conferência dos materiais e distinção entre o planejado, o testado e o produzido."]
};
const statusCopy={PENDING:["A iniciar","pending"],IN_PROGRESS:["Em desenvolvimento","progress"],COMPLETE_DRAFT:["Rascunho concluído","draft"],APPROVED:["Aprovada","approved"],REVISE:["Revisão necessária","revise"]};
const roleCopy={RESEARCHER:"Pesquisa",CREATIVE_DIRECTOR:"Direção criativa",SCREENWRITER:"Roteiro",CRITIC:"Revisão independente",PERFORMANCE_DIRECTOR:"Direção de performance",DP:"Fotografia",PRODUCTION_DESIGNER:"Direção de arte",EDITOR:"Montagem",SOUND_DESIGNER:"Som",PRODUCER_AD:"Produção e assistência",CONTINUITY_SUPERVISOR:"Continuidade",STORYBOARD_ARTIST:"Storyboard",VFX_AI_SUPERVISOR:"VFX e IA",POST_QA:"Revisão de pós"};
const taskCopy={ASSIGNED:"Tarefa atribuída",SUBMITTED:"Parecer entregue",ACCEPTED_BY_DIRECTOR:"Integrado pela direção",REVISION_REQUIRED:"Rodada em revisão",CANCELLED_BY_DIRECTOR:"Interrompida pela direção"};
const verdictCopy={ACCEPT:"Decisão aceita",REVISE:"Revisão solicitada",MORE_RESEARCH:"Pesquisa adicional",CROSS_DEPARTMENT_REVIEW:"Discussão entre áreas",REJECT:"Proposta recusada"};
const documentCopy={"00_SOURCE_MANIFEST":"Fontes e materiais recebidos","02_ROTAS_E_DIRECAO":"Rotas criativas e direção","00_DIRECTION_LOCK":"Decisões travadas pela direção","03_ROTEIRO_LITERARIO":"Roteiro literário","03_ROTEIRO_AV":"Roteiro audiovisual","04_TRATAMENTO_DIRECAO":"Tratamento de direção","04_MAPA_CENA_PERFORMANCE":"Mapa de cena e performance","05_DIRECAO_FOTOGRAFIA":"Direção de fotografia","05_DIRECAO_ARTE":"Direção de arte","05_ARQUITETURA_MONTAGEM_SOM":"Montagem e desenho de som","05_BIBLIA_VISUAL_SONORA":"Bíblia visual e sonora","06_ROTEIRO_TECNICO":"Roteiro técnico","06_SHOT_LIST":"Lista de planos","07_ASSET_BIBLE":"Bíblia de elementos e continuidade","07_ASSET_MANIFEST":"Manifesto de elementos","08_STORYBOARD_PREVIS":"Storyboard e pré-visualização","09_PLANO_PRODUCAO_HIBRIDA":"Plano de produção","09_PLANO_GERACAO_IA":"Plano de geração com IA","10_SHOT_PACKETS_PROMPTS":"Pacotes de execução por plano","11_MONTAGEM_SOM_POS":"Montagem, som e pós-produção","12_QA_MASTER_VERSOES":"Controle de qualidade e versões"};
function esc(value){return String(value??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}
function filename(path){return String(path).split("/").pop();}
function textLabel(path){const base=filename(path).replace(/\.(md|json)$/i,"");return documentCopy[base]||base.replace(/^\d+_/,"").replaceAll("_"," ").replace(/\b\w/g,c=>c.toUpperCase());}
function humanize(text){
  let value=String(text??"");
  const phases={CREATIVE_DIRECTION:"direção criativa",BRIEF_STRATEGY:"briefing",SCRIPT:"roteiro",DIRECTOR_TREATMENT:"tratamento",VISUAL_SOUND_SYSTEM:"imagem, arte e som",DECOUPAGE:"decupagem",ASSETS_CONTINUITY:"elementos e continuidade",STORYBOARD_PREVIS:"storyboard",AI_EXECUTION_PLAN:"plano de produção",SHOT_PACKETS:"pacotes por plano",POST_DELIVERY:"montagem e pós",QA_VERSIONS:"controle de qualidade"};
  value=value.replace(/\bCYCLE-(\d+)_([A-Z_]+)-(\d+)\b/g,(_,round,phase,version)=>`rodada ${Number(round)} de ${phases[phase]||phase.toLowerCase().replaceAll("_"," ")} ${version}`);
  value=value.replace(/\bROUGH-v(\d+)\b/gi,(_,version)=>`rascunho ${Number(version)}`);
  value=value.replace(/\bREVIEW-v(\d+)\b/gi,(_,version)=>`versão de revisão ${Number(version)}`);
  value=value.replace(/\bMASTER-(\d+)\b/g,"master final $1");
  value=value.replace(/\bPOST-QC-REPORT-(\d+)\b/g,"relatório de controle de qualidade $1");
  value=value.replace(/\bTEST-R(\d+)-(\d+)\b/g,"teste de roteiro $2");
  value=value.replace(/\bTEST-DP-(\d+)\b/g,"teste de fotografia $1");
  value=value.replace(/\bTEST-SND-(\d+)\b/g,"teste de som $1");
  value=value.replace(/\b(?:SRC|TASK|REVIEW)-(\d+)\b/g,(_,number)=>`registro ${number}`);
  value=value.replace(/\bACCEPTED_BY_DIRECTOR\b/g,"integrado pela direção");
  value=value.replace(/\bNOT_CONFIRMED\b/g,"ainda não confirmado");
  value=value.replace(/\bPASS_MASTER\b/g,"aprovação do master final");
  value=value.replace(/\bWORK\b/g,"em trabalho");
  value=value.replace(/\bQA_DOCUMENTAL_DRAFT\b/g,"rascunho documental de controle de qualidade");
  value=value.replace(/\bROUGH_DOCUMENTAL_REVIEW\b/g,"revisão documental do rascunho");
  value=value.replace(/\bCOMPLETE_DRAFT\b/g,"rascunho concluído");
  value=value.replace(/\bIN_PROGRESS\b/g,"em desenvolvimento");
  value=value.replace(/\bPENDING\b/g,"a iniciar");
  value=value.replace(/\bAPPROVED\b/g,"aprovado");
  value=value.replace(/\bREVISE\b/g,"em revisão");
  value=value.replace(/\bSUBMITTED\b/g,"entregue para revisão");
  value=value.replace(/\bR([1-3])\b/g,"rota $1");
  return value;
}
function projectBase(){return `/api/projects/${encodeURIComponent(app.project.id)}`;}
function currentJob(){return app.project?.job?.active_job || app.project?.job?.last_job || null;}
function runningJob(){return !!app.project?.job?.busy;}
function toast(message,error=false){$("toast").textContent=message;$("toast").className=error?"error":"";$("toast").hidden=false;clearTimeout(toast.timer);toast.timer=setTimeout(()=>$("toast").hidden=true,6500);}
async function api(path,options={}){
  const config={...options,headers:{...(options.body?{"Content-Type":"application/json"}:{}),...(options.method&&options.method!=="GET"?{"X-CSRF-Token":app.csrf}:{}),...options.headers}};
  if(options.body&&typeof options.body!=="string")config.body=JSON.stringify(options.body);
  const response=await fetch(path,config);const result=await response.json().catch(()=>({error:"O painel recebeu uma resposta inesperada."}));
  if(!response.ok){const error=new Error(result.error||"Não foi possível concluir esta ação.");error.status=response.status;throw error;}return result;
}
function relativePath(path){const parts=path.startsWith("/")?[]:(app.document?.path?.split("/").slice(0,-1)||[]);for(const part of path.split("/")){if(part==="..")parts.pop();else if(part!=="."&&part)parts.push(part);}return parts.join("/");}
function inline(text){
  text=humanize(text);
  let safe=esc(text);safe=safe.replace(/`([^`]+)`/g,"<code>$1</code>").replace(/\*\*([^*]+)\*\*/g,"<strong>$1</strong>");
  safe=safe.replace(/\[([^\]]+)\]\(([^)]+)\)/g,(_,label,target)=>{target=target.replace(/^&lt;|&gt;$/g,"");if(/^https?:\/\//i.test(target))return `<a href="${target}" target="_blank" rel="noopener noreferrer">${label}</a>`;if(/^[a-z]+:/i.test(target)||target.startsWith("//")||target.startsWith("#"))return label;return `<a href="#" data-document="${esc(relativePath(target))}">${label}</a>`;});
  return safe.replace(/&lt;&lt;PREENCHER[^&]*&gt;&gt;/g,"<span class=\"draft-placeholder\">A desenvolver</span>");
}
function markdown(text){
  const lines=String(text).split("\n");let out="",code=false,list=false,table=false;
  const endList=()=>{if(list){out+="</ul>";list=false;}};const endTable=()=>{if(table){out+="</tbody></table></div>";table=false;}};
  for(const line of lines){
    if(line.startsWith("```")){endList();endTable();out+=code?"</code></pre>":"<pre><code>";code=!code;continue;}if(code){out+=esc(line)+"\n";continue;}
    if(line.trim().startsWith("|")&&line.includes("|")){endList();const cells=line.trim().replace(/^\||\|$/g,"").split("|");if(cells.every(c=>/^\s*:?-+:?\s*$/.test(c)))continue;if(!table){out+='<div class="table-scroll"><table><thead><tr>'+cells.map(c=>`<th>${inline(c.trim())}</th>`).join("")+"</tr></thead><tbody>";table=true;}else out+="<tr>"+cells.map(c=>`<td>${inline(c.trim())}</td>`).join("")+"</tr>";continue;}endTable();
    const item=line.match(/^\s*(?:[-*]|\d+[.)])\s+(.+)/);if(item){if(!list){out+="<ul>";list=true;}out+=`<li>${inline(item[1])}</li>`;continue;}endList();if(!line.trim())continue;
    const heading=line.match(/^(#{1,4})\s+(.+)/);if(heading){out+=`<h${heading[1].length}>${inline(heading[2])}</h${heading[1].length}>`;continue;}
    if(/^\s*---+\s*$/.test(line)){out+="<hr>";continue;}if(/^>/.test(line)){out+=`<blockquote>${inline(line.replace(/^>\s?/,""))}</blockquote>`;continue;}out+=`<p>${inline(line)}</p>`;
  }endList();endTable();if(code)out+="</code></pre>";return out;
}
function renderProjects(){const selected=app.project?.id||"";$("project-select").innerHTML='<option value="">Escolha um projeto</option>'+app.projects.map(p=>`<option value="${esc(p.id)}">${esc(p.name||p.project_name)}</option>`).join("");$("project-select").value=selected;}
function renderChrome(){
  const p=app.project;$("welcome").hidden=!!p;$("project-view").hidden=!p;if(!p){$("stage-nav").innerHTML="";return;}
  const phases=p.phases||[],selected=phases.find(x=>x.id===app.phase)||phases[0];if(!selected)return;app.phase=selected.id;
  $("project-title").textContent=p.state.project_name||p.name;$("project-client").textContent=p.state.client||"";$("project-eyebrow").textContent=`PROJETO / ${selected.id.slice(0,2)}`;
  $("stage-nav").innerHTML=phases.map(ph=>{const status=statusCopy[ph.status]||statusCopy.PENDING;return `<button class="stage-link ${ph.id===app.phase?"active":""}" data-phase="${esc(ph.id)}" ${ph.id===app.phase?'aria-current="step"':""}><span class="stage-number">${esc(ph.id.slice(0,2))}</span><span class="stage-name">${esc(phaseCopy[ph.id]?.[0]||ph.title)}</span><span class="status-dot status-${status[1]}" title="${status[0]}"></span></button>`;}).join("");
  const complete=phases.filter(x=>["COMPLETE_DRAFT","APPROVED"].includes(x.status)).length;$("progress-count").textContent=`${complete} / ${phases.length}`;$("progress-fill").style.width=`${complete/phases.length*100}%`;$("progress-bar").setAttribute("aria-valuenow",complete);$("progress-bar").setAttribute("aria-valuemax",phases.length);$("team-count").textContent=(p.tasks||[]).length;
  const current=phases.find(x=>x.id===p.state.current_phase);$("next-action").textContent=complete===phases.length?"Revisar o pacote e preparar a execução":`Desenvolver ${phaseCopy[current?.id]?.[0]?.toLowerCase()||"a próxima etapa"}`;
  $("stage-number").textContent=`ETAPA ${selected.id.slice(0,2)}`;$("stage-title").textContent=phaseCopy[selected.id]?.[0]||selected.title;$("stage-description").textContent=phaseCopy[selected.id]?.[1]||"";
  const st=statusCopy[selected.status]||statusCopy.PENDING;$("stage-status").textContent=st[0];$("stage-status").className=`status-pill status-${st[1]}`;
  const active=runningJob();$("approve-stage").disabled=selected.status!=="COMPLETE_DRAFT"||active||app.editing;$("approve-stage").textContent=selected.status==="APPROVED"?"Etapa aprovada":"Aprovar etapa";$("revise-stage").disabled=active||app.editing;$("edit-document").disabled=!app.document?.editable||active||app.editing;$("export-project").disabled=active;
  $("gate-description").textContent=selected.status==="COMPLETE_DRAFT"?"O rascunho está pronto para sua revisão.":selected.status==="APPROVED"?"Sua aprovação está registrada nesta versão.":"A aprovação fica disponível após a revisão da equipe.";
  $("project-location").textContent="Projeto local · arquivos preservados";$("project-location").title=p.path;$("refresh-status").textContent="Atualizado com os arquivos do projeto";
  app.runner=p.job?.capability||app.runner;$("runner-status").textContent=app.runner.authenticated?"Codex conectado neste computador":app.runner.available?"Codex precisa de login":"Conectar Codex para desenvolver";
  $("job-status").hidden=!active;$("job-label").textContent=currentJob()?.status==="cancelling"?"Interrompendo…":"Equipe trabalhando no projeto";$("send-message").disabled=active||app.busy||app.editing;
}
async function loadProject(id,reset=true){
  if(app.editing)throw new Error("Salve ou cancele a edição antes de trocar de projeto.");if(!id){app.project=null;renderChrome();return;}
  const p=await api(`/api/projects/${encodeURIComponent(id)}`);app.project=p;if(reset){app.phase=p.state.current_phase||p.phases[0].id;app.document=null;app.chatKey="";app.fileKey="";app.teamKey="";const url=new URL(location.href);url.searchParams.set("project",id);history.replaceState(null,"",url);}
  renderProjects();renderChrome();renderChat();renderTeam();renderVisual();await loadPhaseDocuments(reset);
}
async function loadPhaseDocuments(reset=false){
  const phase=app.project.phases.find(x=>x.id===app.phase),docs=[...(phase?.docs||[])],old=app.document?.path;
  if(app.phase==="01_BRIEF_STRATEGY" && app.project.files.some(f=>f.path==="inputs/briefing.md"))docs.unshift({path:"inputs/briefing.md",exists:true,label:"Ideia e briefing inicial"});
  $("document-select").innerHTML=docs.map(d=>`<option value="${esc(d.path)}" ${!d.exists?"disabled":""}>${esc(textLabel(d.label||d.path))}${d.exists?"":" · a desenvolver"}</option>`).join("");
  const choice=(!reset&&docs.some(d=>d.path===old&&d.exists))?old:docs.find(d=>d.exists)?.path;
  if(choice){$("document-select").value=choice;if(reset||!app.document||app.document.path!==choice)await loadDocument(choice);$("document-select").disabled=false;}
  else{app.document=null;$("document-empty").hidden=false;$("document-content").hidden=true;$("document-select").disabled=true;$("edit-document").disabled=true;}
}
async function loadDocument(path){
  if(app.editing)throw new Error("Salve ou cancele a edição antes de abrir outro documento.");const result=await api(`${projectBase()}/document?path=${encodeURIComponent(path)}`);app.document=result;$("document-empty").hidden=true;$("document-content").hidden=false;
  if(!Array.from($("document-select").options).some(o=>o.value===path))$("document-select").add(new Option(textLabel(path),path));$("document-select").value=path;
  $("document-content").innerHTML=path.endsWith(".json")?`<pre><code>${esc(result.content)}</code></pre>`:markdown(result.content);$("edit-document").disabled=!result.editable||runningJob();
}
function setTab(tab){app.tab=tab;for(const name of ["documents","team","visual"]){$(name+"-view").hidden=name!==tab;$("tab-"+name).setAttribute("aria-selected",String(name===tab));}}
function renderTeam(){
  if(!app.project)return;const all=$("all-team").checked,tasks=(app.project.tasks||[]).filter(t=>all||t.cycle_id?.startsWith("CYCLE-"+app.phase+"-")),decisions=(app.project.state.director_reviews||[]).filter(r=>all||r.phase===app.phase),key=JSON.stringify([tasks,decisions,all,app.phase]);if(key===app.teamKey)return;app.teamKey=key;
  $("team-cards").innerHTML=tasks.length?tasks.map(t=>`<article class="team-card"><header><h3>${esc(roleCopy[t.role]||t.role)}</h3><span class="small muted">${esc(taskCopy[t.status]||t.status)}</span></header><p>${t.actor_type==="ROLE_SIMULATION"?"Passe de papel simulado, sem um agente independente.":"Especialista temporário convocado para esta decisão."}</p><details class="technical-details"><summary>Registro técnico</summary><code>${esc(t.actor_id||"Especialista temporário")}</code></details>${t.submission_path?`<button class="quiet-button" data-document="${esc(t.submission_path)}">Ler parecer ↗</button>`:""}</article>`).join(""):'<div class="empty-state"><h3>A equipe aparece aqui quando trabalhar.</h3><p>Cada participação mostra seu parecer e a decisão da direção, conforme os registros reais do projeto.</p></div>';
  $("director-decisions").innerHTML=decisions.length?'<h3 class="section-title">Decisões da direção</h3>'+decisions.map(d=>`<article class="decision-card"><strong>${esc(verdictCopy[d.verdict]||d.verdict)}</strong><p>${esc(d.reason)}</p></article>`).join(""):"";
}
function visualFiles(){return(app.project?.files||[]).filter(f=>/\.(html|svg|png|jpe?g|webp|gif|pdf|mp4|webm|mov|mp3|wav|m4a)$/i.test(f.path)).sort((a,b)=>{const score=f=>/ROUGHBOARD\.html$/.test(f.path)?0:/\.html$/.test(f.path)?1:2;return score(a)-score(b)||a.path.localeCompare(b.path);});}
function artifactURL(path){return `/artifacts/${encodeURIComponent(app.project.id)}/${path.split("/").map(encodeURIComponent).join("/")}`;}
function renderVisual(){
  if(!app.project)return;const files=visualFiles(),key=JSON.stringify(files);if(key===app.fileKey)return;app.fileKey=key;const previous=$("visual-select").value;$("visual-select").innerHTML=files.map(f=>`<option value="${esc(f.path)}">${esc(filename(f.path))}</option>`).join("");$("visual-empty").hidden=files.length>0;$("visual-select").disabled=!files.length;$("open-visual").hidden=!files.length;
  if(files.length){$("visual-select").value=files.some(f=>f.path===previous)?previous:files[0].path;showVisual();}else $("visual-frame").replaceChildren();
}
function showVisual(){
  const path=$("visual-select").value;if(!path)return;const url=artifactURL(path);$("open-visual").href=url;let element;
  if(/\.(html|pdf)$/i.test(path)){element=document.createElement("iframe");element.setAttribute("sandbox","allow-scripts");element.title=textLabel(path);element.src=url;}
  else if(/\.(mp4|webm|mov)$/i.test(path)){element=document.createElement("video");element.controls=true;element.src=url;}
  else if(/\.(mp3|wav|m4a)$/i.test(path)){element=document.createElement("audio");element.controls=true;element.src=url;}
  else{element=document.createElement("img");element.src=url;element.alt=textLabel(path);}$("visual-frame").replaceChildren(element);
}
function renderChat(){
  const messages=app.project?.chat||[],job=currentJob(),key=JSON.stringify([messages,job?.status,job?.progress]);if(key===app.chatKey)return;app.chatKey=key;
  $("chat-messages").innerHTML=messages.length?messages.map(m=>`<div class="chat-bubble ${m.role==="user"?"user":""}"><small>${m.role==="user"?"Você":m.role==="system"?"Execução":"Diretor e equipe"}</small>${esc(m.content||m.text||m.message||"")}</div>`).join(""):'<div class="chat-intro">Conte a ideia ou escolha uma etapa. O diretor consulta o projeto, convoca os especialistas e registra o trabalho nos arquivos que você acompanha neste painel.</div>';
  if(runningJob()&&job?.progress?.length){const p=document.createElement("div");p.className="chat-bubble";p.textContent=job.progress.slice(-3).map(x=>x.text||"").join("\n");$("chat-messages").append(p);}$("chat-messages").scrollTop=$("chat-messages").scrollHeight;
}
function showExample(){$("example-frame").src="/example";$("example-dialog").showModal();}
function formDialog({title,description,fields,submit="Salvar",action}){
  $("dialog-title").textContent=title;$("dialog-description").textContent=description;$("dialog-error").hidden=true;$("dialog-submit").textContent=submit;
  $("dialog-fields").innerHTML=fields.map(f=>`<label for="field-${esc(f.name)}">${esc(f.label)}</label>${f.multiline?`<textarea id="field-${esc(f.name)}" name="${esc(f.name)}" ${f.required?"required":""} placeholder="${esc(f.placeholder||"")}">${esc(f.value||"")}</textarea>`:`<input id="field-${esc(f.name)}" name="${esc(f.name)}" ${f.required?"required":""} value="${esc(f.value||"")}" placeholder="${esc(f.placeholder||"")}" autocomplete="off">`}`).join("");
  $("dialog-form").onsubmit=async event=>{event.preventDefault();$("dialog-submit").disabled=true;$("dialog-error").hidden=true;try{await action(Object.fromEntries(new FormData(event.target)));$("form-dialog").close();}catch(error){$("dialog-error").textContent=error.message;$("dialog-error").hidden=false;}finally{$("dialog-submit").disabled=false;}};$("form-dialog").showModal();
}
function newProject(){if(app.editing){toast("Salve ou cancele a edição antes de criar outro projeto.",true);return;}formDialog({title:"Vamos começar seu filme",description:"A ideia pode estar no começo. O diretor ajuda a desenvolver o que faltar.",submit:"Criar projeto",fields:[{name:"name",label:"Nome do projeto",required:true,placeholder:"Ex.: Filme de lançamento"},{name:"client",label:"Marca ou cliente",placeholder:"Pode ficar a confirmar"},{name:"brief",label:"Conte sua ideia e o que já sabe",multiline:true,required:true,placeholder:"O que o filme precisa provocar? Público, duração, formato e recursos, se já souber."}],action:async values=>{const result=await api("/api/projects",{method:"POST",body:values});await refreshList();await loadProject(result.id||result.project.id);toast("Projeto criado. Sua ideia foi salva nos arquivos.");}});}
function openProject(){formDialog({title:"Abrir um projeto existente",description:"Cole o caminho da pasta que contém o arquivo 00_PROJECT_STATE.json. O painel vai acompanhar os arquivos que já existem.",submit:"Abrir projeto",fields:[{name:"path",label:"Pasta do projeto",required:true,placeholder:"/caminho/para/meu-filme"}],action:async values=>{const result=await api("/api/projects/register",{method:"POST",body:values});await refreshList();await loadProject(result.id||result.project.id);}});}
async function refreshList(){const data=await api("/api/projects");app.projects=data.projects;renderProjects();}
async function sendMessage(text,mode="phase"){
  if(mode==="phase" && app.phase!==app.project.state.current_phase)throw new Error("Selecione a etapa atual para trabalhar com a equipe. Para mudar uma etapa anterior, use Pedir alteração.");
  if(app.editing)throw new Error("Salve ou cancele a edição antes de chamar a equipe.");if(!app.runner.available||app.runner.authenticated===false){showRunnerHelp();return;}app.busy=true;renderChrome();
  try{await api(projectBase()+"/message",{method:"POST",body:{text,mode}});$("message").value="";await loadProject(app.project.id,false);toast("Pedido enviado ao diretor.");}finally{app.busy=false;renderChrome();}
}
function showRunnerHelp(){formDialog({title:"Conectar o diretor ao Codex",description:(app.runner.message||"O painel usa o Codex CLI instalado e conectado neste computador.")+" Com o Codex disponível no terminal, execute codex login e reabra o painel. Os documentos e a revisão manual funcionam enquanto isso.",submit:"Conferir conexão",fields:[],action:async()=>{const b=await api("/api/bootstrap");app.runner=b.runner||{};app.csrf=b.csrf;renderChrome();toast(app.runner.authenticated?"Codex conectado.":app.runner.message||"Conexão ainda não disponível.");}});}
async function pollProject(){
  if(app.poll||!app.project||document.hidden)return;app.poll=true;try{const id=app.project.id,p=await api(projectBase());if(id!==app.project?.id)return;const previous=app.document;app.project=p;renderChrome();renderChat();renderTeam();renderVisual();if(!app.editing&&previous){const doc=p.phases.flatMap(ph=>ph.docs).find(d=>d.path===previous.path);if(doc?.sha256&&doc.sha256!==previous.sha256)await loadDocument(previous.path);}if(!app.editing&&!app.document)await loadPhaseDocuments();$("connection-banner").hidden=true;}catch(error){$("connection-banner").textContent="Não consegui atualizar os arquivos. Verifique se o painel local continua aberto. "+error.message;$("connection-banner").hidden=false;}finally{app.poll=false;}
}
document.addEventListener("click",async event=>{const button=event.target.closest("[data-phase],[data-tab],[data-document],[data-suggestion]");if(!button)return;try{if(button.dataset.phase){if(app.editing)throw new Error("Salve ou cancele a edição antes de trocar de etapa.");app.phase=button.dataset.phase;app.document=null;renderChrome();renderTeam();await loadPhaseDocuments(true);}if(button.dataset.tab)setTab(button.dataset.tab);if(button.dataset.document){event.preventDefault();setTab("documents");await loadDocument(button.dataset.document);}if(button.dataset.suggestion){$("message").value=button.dataset.suggestion;$("message").focus();}}catch(error){toast(error.message,true);}});
$("new-project").onclick=newProject;$("welcome-new").onclick=newProject;$("open-project").onclick=openProject;
for(const id of ["show-example","welcome-example","visual-example"])$(id).onclick=showExample;
$("example-close").onclick=()=>{$("example-dialog").close();$("example-frame").removeAttribute("src");};$("dialog-close").onclick=$("dialog-cancel").onclick=()=>$("form-dialog").close();
$("project-select").onchange=event=>loadProject(event.target.value).catch(error=>{renderProjects();toast(error.message,true);});$("document-select").onchange=event=>loadDocument(event.target.value).catch(error=>toast(error.message,true));$("visual-select").onchange=showVisual;$("all-team").onchange=renderTeam;
$("edit-document").onclick=()=>{if(!app.document?.editable)return;app.editing=true;$("document-editor").value=app.document.content;$("edit-reason").value="";$("editor-form").hidden=false;$("document-content").hidden=true;$("document-select").disabled=true;renderChrome();$("document-editor").focus();};
$("cancel-edit").onclick=()=>{app.editing=false;$("editor-form").hidden=true;$("document-content").hidden=false;$("document-select").disabled=false;renderChrome();};
$("editor-form").onsubmit=async event=>{event.preventDefault();const button=event.submitter;button.disabled=true;try{await api(projectBase()+"/document",{method:"POST",body:{path:app.document.path,content:$("document-editor").value,sha256:app.document.sha256,reason:$("edit-reason").value||"Alteração registrada pelo usuário no painel."}});app.editing=false;$("editor-form").hidden=true;$("document-content").hidden=false;$("document-select").disabled=false;await loadDocument(app.document.path);await loadProject(app.project.id,false);toast("Alteração salva e registrada no projeto.");}catch(error){toast(error.status===409?"O arquivo mudou ou a equipe está trabalhando. Sua edição foi preservada; confira a versão atual antes de salvar.":error.message,true);}finally{button.disabled=false;}};
$("message-form").onsubmit=async event=>{event.preventDefault();const text=$("message").value.trim();if(text)try{await sendMessage(text,$("message-mode").value);}catch(error){toast(error.message,true);}};
$("develop-empty").onclick=()=>{$("message").value="Desenvolva a etapa atual com os especialistas necessários, usando o briefing e o repertório. Registre os materiais e a revisão no projeto.";$("message").focus();};
$("approve-stage").onclick=()=>formDialog({title:"Aprovar esta etapa",description:"Registra sua aprovação sobre a versão atual dos documentos. O desenvolvimento da equipe e a aprovação humana são registros distintos.",submit:"Registrar aprovação",fields:[{name:"by",label:"Seu nome",required:true,value:localStorage.getItem("cfd-reviewer")||""},{name:"note",label:"Observação",placeholder:"Opcional"}],action:async values=>{await api(projectBase()+"/approve",{method:"POST",body:{...values,phase:app.phase}});localStorage.setItem("cfd-reviewer",values.by);await loadProject(app.project.id,false);toast("Aprovação registrada.");}});
$("revise-stage").onclick=()=>formDialog({title:"Pedir uma alteração",description:"A revisão fica registrada no projeto. Etapas que dependem desta decisão serão reabertas quando necessário.",submit:"Registrar revisão",fields:[{name:"reason",label:"O que precisa mudar e por quê?",required:true,multiline:true}],action:async values=>{const phase=app.phase;await api(projectBase()+"/revise",{method:"POST",body:{...values,phase}});await loadProject(app.project.id,false);if(app.runner.authenticated)await sendMessage(`Revise a etapa ${phase}. Pedido do usuário: ${values.reason}`,"phase");else toast("Revisão registrada nos arquivos do projeto.");}});
$("cancel-job").onclick=async()=>{try{await api(projectBase()+"/cancel",{method:"POST",body:{}});await loadProject(app.project.id,false);toast("Interrupção solicitada. Os arquivos produzidos ficam preservados.");}catch(error){toast(error.message,true);}};$("runner-help").onclick=showRunnerHelp;
$("export-project").onclick=async()=>{try{const response=await fetch(projectBase()+"/export");if(!response.ok){const data=await response.json();throw new Error(data.error||"Não foi possível exportar.");}const blob=await response.blob(),url=URL.createObjectURL(blob),a=document.createElement("a");a.href=url;a.download=(app.project.state.project_name||"filme").replace(/[^\p{L}\p{N} _-]/gu,"")+".zip";a.click();setTimeout(()=>URL.revokeObjectURL(url),30000);toast("Pacote exportado com os arquivos reais do projeto.");}catch(error){toast(error.message,true);}};
$("copy-link").onclick=async()=>{try{await navigator.clipboard.writeText(location.href);toast("Link copiado. Ele abre neste computador enquanto o painel estiver rodando.");}catch{toast("Copie o endereço do navegador. O link é local a este computador.");}};
window.addEventListener("beforeunload",event=>{if(app.editing){event.preventDefault();event.returnValue="";}});
(async()=>{try{const b=await api("/api/bootstrap");app.csrf=b.csrf;app.runner=b.runner||{};app.projects=b.projects||[];renderProjects();const requested=new URL(location.href).searchParams.get("project"),id=requested||b.initial_project_id||app.projects[0]?.id;if(id)await loadProject(id);else renderChrome();setInterval(pollProject,2500);}catch(error){$("connection-banner").textContent=error.message;$("connection-banner").hidden=false;$("welcome").hidden=false;}})();
