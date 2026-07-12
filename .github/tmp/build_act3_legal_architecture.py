from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

css_marker = '/* ---- MINIMALIST ACT II END ---- */'
css_start = '/* ---- MINIMALIST ACT III START ---- */'
if css_start in text:
    raise SystemExit('Act III minimalist CSS already exists')
if css_marker not in text:
    raise SystemExit('Act II CSS marker not found')

css = r'''

/* ---- MINIMALIST ACT III START ---- */
.act3-minimal{max-width:100%;}
.act3-opening-copy{max-width:61rem;margin:.7rem 0 0;color:rgba(229,229,229,.68);font-size:.82rem;line-height:1.68;}
.act3-operation-shell{margin-top:1.35rem;border-top:1px solid rgba(197,160,89,.22);border-bottom:1px solid rgba(229,229,229,.08);}
.act3-operation-nav{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));border-bottom:1px solid rgba(229,229,229,.08);}
.act3-operation-step{position:relative;min-width:0;padding:.78rem .65rem .82rem;border:0;border-right:1px solid rgba(229,229,229,.07);background:transparent;color:rgba(229,229,229,.42);text-align:left;cursor:pointer;transition:color .2s,background .2s;}
.act3-operation-step:last-child{border-right:0;}
.act3-operation-step::after{content:"";position:absolute;left:.65rem;right:.65rem;bottom:-1px;height:1px;background:transparent;}
.act3-operation-step:hover,.act3-operation-step:focus,.act3-operation-step.active{outline:none;color:var(--gold);background:rgba(197,160,89,.03);}
.act3-operation-step.active::after{background:var(--gold);box-shadow:0 0 10px rgba(197,160,89,.55);}
.act3-operation-step .n{display:block;margin-bottom:.22rem;color:rgba(197,160,89,.68);font-size:.52rem;font-weight:800;letter-spacing:.13em;}
.act3-operation-step .t{display:block;font-family:"Cormorant Garamond",Georgia,serif;font-size:1.02rem;line-height:1.05;color:inherit;}
.act3-operation-panel{display:grid;grid-template-columns:170px minmax(0,1.25fr) minmax(0,.9fr);gap:1.1rem;align-items:start;padding:1.05rem 0 1.15rem;min-height:165px;}
.act3-operation-id span{display:block;color:var(--gold);font-size:.54rem;font-weight:800;letter-spacing:.13em;text-transform:uppercase;}
.act3-operation-id h3{margin:.32rem 0 0;font-family:"Cormorant Garamond",Georgia,serif;color:#f4efe7;font-size:1.6rem;line-height:1.02;font-weight:500;}
.act3-operation-block{padding-left:1rem;border-left:1px solid rgba(197,160,89,.22);}
.act3-operation-block strong{display:block;color:var(--gold);font-size:.54rem;font-weight:800;letter-spacing:.13em;text-transform:uppercase;}
.act3-operation-block p{margin:.35rem 0 0;color:rgba(229,229,229,.62);font-size:.75rem;line-height:1.6;}
.act3-trace{margin-top:1.55rem;padding-top:1.2rem;border-top:1px solid rgba(229,229,229,.08);}
.act3-trace-head{max-width:59rem;}
.act3-trace-head h3{margin:.3rem 0 0;font-family:"Cormorant Garamond",Georgia,serif;color:#f3eee6;font-size:1.75rem;line-height:1.04;font-weight:500;}
.act3-trace-head p{margin:.5rem 0 0;color:rgba(229,229,229,.57);font-size:.76rem;line-height:1.6;}
.act3-trace-tabs{display:flex;gap:1rem;overflow-x:auto;margin-top:.85rem;border-bottom:1px solid rgba(229,229,229,.09);}
.act3-trace-tab{position:relative;flex:0 0 auto;padding:.58rem 0 .68rem;border:0;background:transparent;color:rgba(229,229,229,.42);font-size:.6rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;cursor:pointer;}
.act3-trace-tab::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:1px;background:transparent;}
.act3-trace-tab:hover,.act3-trace-tab:focus,.act3-trace-tab.active{outline:none;color:var(--gold);}
.act3-trace-tab.active::after{background:var(--gold);box-shadow:0 0 9px rgba(197,160,89,.5);}
.act3-trace-panel{margin-top:.25rem;border-top:1px solid rgba(197,160,89,.18);}
.act3-trace-row{display:grid;grid-template-columns:180px minmax(0,1fr);gap:1rem;padding:.67rem 0;border-bottom:1px solid rgba(229,229,229,.07);}
.act3-trace-row strong{color:var(--gold);font-size:.54rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;}
.act3-trace-row span{color:rgba(229,229,229,.64);font-size:.74rem;line-height:1.58;}
.act3-controls{margin-top:1.5rem;border-top:1px solid rgba(197,160,89,.22);}
.act3-control-line{display:grid;grid-template-columns:minmax(190px,.7fr) minmax(0,1.3fr);gap:1rem;padding:.78rem 0;border-bottom:1px solid rgba(229,229,229,.07);}
.act3-control-line strong{color:#eee8df;font-family:"Cormorant Garamond",Georgia,serif;font-size:1.08rem;font-weight:500;line-height:1.1;}
.act3-control-line span{color:rgba(229,229,229,.56);font-size:.73rem;line-height:1.58;}
.act3-regulatory-loop{display:grid;grid-template-columns:auto minmax(0,1fr);gap:.85rem;align-items:start;margin-top:1.15rem;padding:.85rem .95rem;border:1px solid rgba(197,160,89,.25);border-left:2px solid var(--gold);border-radius:.85rem;background:linear-gradient(90deg,rgba(197,160,89,.08),rgba(255,255,255,.012));}
.act3-regulatory-loop .loop{color:var(--gold);font-family:"Cormorant Garamond",Georgia,serif;font-size:1.65rem;line-height:1;}
.act3-regulatory-loop strong{display:block;color:var(--gold);font-size:.56rem;letter-spacing:.13em;text-transform:uppercase;margin-bottom:.25rem;}
.act3-regulatory-loop p{margin:0;color:rgba(229,229,229,.62);font-size:.74rem;line-height:1.55;}
.act3-supporting-system{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:1.25rem;align-items:center;margin-top:1.25rem;padding-top:1rem;border-top:1px solid rgba(229,229,229,.08);}
.act3-supporting-system h3{margin:.28rem 0 0;font-family:"Cormorant Garamond",Georgia,serif;color:#f4efe7;font-size:1.65rem;line-height:1.04;font-weight:500;}
.act3-supporting-system p{max-width:56rem;margin:.5rem 0 0;color:rgba(229,229,229,.58);font-size:.75rem;line-height:1.62;}
.act3-capstone-bridge{display:flex;align-items:center;justify-content:space-between;gap:1rem;margin-top:1rem;padding-top:.9rem;border-top:1px solid rgba(229,229,229,.07);}
.act3-capstone-bridge p{margin:0;max-width:50rem;color:rgba(229,229,229,.66);font-family:"Cormorant Garamond",Georgia,serif;font-size:1.07rem;line-height:1.38;}
.act3-capstone-bridge a{flex:0 0 auto;color:var(--gold);font-size:.59rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;border-bottom:1px solid rgba(197,160,89,.45);padding-bottom:.23rem;}
@media(max-width:900px){.act3-operation-nav{display:flex;overflow-x:auto;}.act3-operation-step{flex:0 0 170px;}.act3-operation-panel{grid-template-columns:145px 1fr;}.act3-operation-panel .act3-operation-block:last-child{grid-column:2;}.act3-supporting-system{grid-template-columns:1fr;align-items:start;}}
@media(max-width:640px){.act3-operation-panel{grid-template-columns:1fr;gap:.75rem;}.act3-operation-panel .act3-operation-block:last-child{grid-column:auto;}.act3-operation-block{padding:.7rem 0 0;border-left:0;border-top:1px solid rgba(197,160,89,.2);}.act3-trace-row,.act3-control-line{grid-template-columns:1fr;gap:.22rem;}.act3-capstone-bridge{align-items:flex-start;flex-direction:column;}}
/* ---- MINIMALIST ACT III END ---- */
'''
text = text.replace(css_marker, css_marker + css, 1)

start_marker = '  // ---------- ACT III ----------'
end_marker = '  // ---------- CAPSTONE ----------'
start = text.find(start_marker)
end = text.find(end_marker)
if start < 0 or end < 0 or end <= start:
    raise SystemExit('Act III block markers not found')

new_block = r'''  // ---------- ACT III ----------
  (function(){
    var liveUrl='https://sandbox.lexnovahq.com/interface-diligence/diligence-system/';
    var workflow=[
      {title:'Evidence',purpose:'Preserve the underlying source before any legal conclusion is applied. Capture the factual statement, date, context, limitation and what cannot be verified.',principle:'A classification is not evidence. The source remains controlling.'},
      {title:'Matter Structure',purpose:'Organise the evidence according to the activities, roles, data, assets, decisions, transactions, dependencies and jurisdictions identified by the lawyer.',principle:'The system reflects the lawyer’s matter structure. It does not invent one.'},
      {title:'Legal Testing',purpose:'Apply the controlled questions already defined: authority, trigger, exclusion, evidence requirement, consequence and limitation.',principle:'Technology applies the test consistently. The lawyer owns the test.'},
      {title:'Qualified Review',purpose:'Route missing private facts, conflicting evidence, jurisdiction-specific questions and unresolved responsibility to human judgment.',principle:'Uncertainty is escalated, not automated away.'},
      {title:'Review-Ready Handoff',purpose:'Prepare the position, evidence basis, limitations, open questions, proposed instrument, proposed control and counsel route for review.',principle:'The output is structured legal work for review—not an autonomous legal opinion.'}
    ];
    var traces={
      payment:{
        label:'Payment Perimeter',
        rows:[
          ['Source evidence','AsterPay presents itself as a technology layer that routes payment activity through regulated partners and does not publicly describe itself as the holder of customer funds.'],
          ['Structured fact','AsterPay may initiate or orchestrate payment instructions while settlement, custody and safeguarding are performed by a licensed partner.'],
          ['Legal test','Who initiates the transaction, who controls or holds funds, who can retry, redirect, reverse or settle activity, and which entity bears the customer-facing obligation?'],
          ['Evidence gap','Public materials do not establish the complete funds flow, actual operational control or the private contractual allocation with the regulated partner.'],
          ['Qualified review question','Which entity receives, holds and settles funds in practice, and can AsterPay direct, interrupt or reverse the transaction after initiation?'],
          ['Handoff route','Payments-perimeter review · funds-flow evidence · safeguarding allocation · partner-agreement review · local payments counsel.']
        ]
      },
      credit:{
        label:'Credit Scoring',
        rows:[
          ['Source evidence','AsterPay states that an automated score supports customer eligibility assessment.'],
          ['Structured fact','Automated scoring may materially influence access to a financial product.'],
          ['Legal test','Does the score determine or constrain the outcome? Is human review independent? Are specific reasons produced and capable of being communicated?'],
          ['Evidence gap','Public materials do not establish actual override authority, reviewer independence or the frequency with which the score is displaced in practice.'],
          ['Qualified review question','Who retains final authority, what evidence is reconsidered independently, and how often is the automated score overridden?'],
          ['Handoff route','Fair-lending review · automated-decision governance · reason-generation control · contractual allocation · local-counsel confirmation.']
        ]
      },
      identity:{
        label:'Identity & KYC',
        rows:[
          ['Source evidence','AsterPay describes identity verification and onboarding checks supported by external verification capabilities.'],
          ['Structured fact','The onboarding flow processes identity data and may determine whether a person can access the financial service.'],
          ['Legal test','What data is collected, is biometric inference used, who determines the match threshold, what retention applies, and what manual exception route exists?'],
          ['Evidence gap','Public materials do not establish the provider’s full processing instructions, threshold logic, retention schedule or actual human exception process.'],
          ['Qualified review question','Who controls the verification outcome, what happens when the provider returns an uncertain match, and who can approve an exception?'],
          ['Handoff route','AML/KYC review · privacy and biometric review · vendor allocation · retention and exception controls · local-counsel confirmation.']
        ]
      }
    };
    var workflowButtons=workflow.map(function(s,i){return '<button class="act3-operation-step'+(i===0?' active':'')+'" type="button" data-act3-operation="'+i+'" aria-selected="'+(i===0?'true':'false')+'"><span class="n">0'+(i+1)+'</span><span class="t">'+esc(s.title)+'</span></button>';}).join('');
    var traceButtons=Object.keys(traces).map(function(k,i){return '<button class="act3-trace-tab'+(i===0?' active':'')+'" type="button" data-act3-trace="'+k+'" aria-selected="'+(i===0?'true':'false')+'">'+esc(traces[k].label)+'</button>';}).join('');

    main.appendChild(el(
      '<section id="delivery-system" class="act" data-rail="3">'
      +'<span id="tooling-layer" class="anchor-point" aria-hidden="true"></span>'
      +'<span id="systems-layer" class="anchor-point" aria-hidden="true"></span>'
      +'<div class="card-shell act3-minimal">'
        +'<header id="act3-orientation" class="reveal"><p class="eyebrow">ACT III · LEGAL ARCHITECTURE IN OPERATION</p><h2 class="font-display section-title text-white mt-2">How I use technology to preserve legal judgment through execution.</h2><p class="act3-opening-copy">Once the legal architecture is defined, technology can preserve the evidence path, apply the agreed structure consistently, expose missing proof and prepare the matter for qualified review.</p><p class="act3-opening-copy">The system does not determine what the law means. It preserves how the lawyer’s conclusion was reached, where it is limited and what must happen next.</p></header>'
        +'<section id="project-walkthrough" class="reveal act3-operation-shell"><nav class="act3-operation-nav" aria-label="Supporting workflow">'+workflowButtons+'</nav><div id="act3-operation-panel" class="act3-operation-panel" aria-live="polite"></div></section>'
        +'<section class="reveal act3-trace"><div class="act3-trace-head"><p class="eyebrow">Trace one legal conclusion</p><h3>From source evidence to review-ready handoff.</h3><p>The selected AsterPay thread shows what the system preserves at each point. The legal characterisation and test come from the lawyer; the technology maintains the source, limitation and review route.</p></div><div class="act3-trace-tabs" role="tablist">'+traceButtons+'</div><div id="act3-trace-panel" class="act3-trace-panel" aria-live="polite"></div></section>'
        +'<section id="prompt-agent-proof" class="reveal act3-controls" aria-label="System controls">'
          +'<div class="act3-control-line"><strong>Evidence remains attached.</strong><span>Every finding retains the source, context and limitation supporting it.</span></div>'
          +'<div class="act3-control-line"><strong>Unsupported conclusions cannot silently pass.</strong><span>Missing, contradictory or insufficient proof becomes a review question rather than a fabricated answer.</span></div>'
          +'<div class="act3-control-line"><strong>Human judgment controls the final position.</strong><span>The system structures, checks and routes the work. It does not replace legal interpretation or drafting judgment.</span></div>'
        +'</section>'
        +'<div id="workflow-automation-proof" class="reveal act3-regulatory-loop"><span class="loop">↺</span><div><strong>Regulatory update loop</strong><p>Regulatory changes reopen the relevant authority, trigger, consequence and instrument route. They do not silently rewrite the legal conclusion.</p></div></div>'
        +'<section id="act3-interface-diligence-engine" class="reveal act3-supporting-system"><div><p class="eyebrow">Supporting system</p><h3>The diligence engine preserves the architecture.</h3><p>I built the diligence engine to preserve evidence, structure factual profiles, apply controlled legal tests and prepare review-ready handoffs. It demonstrates how legal architecture can operate at scale. It is not presented as a substitute for qualified legal judgment.</p></div><a id="sandbox-os" class="btn" data-interface-os-gate="true" href="'+esc(liveUrl)+'" target="_blank" rel="noopener">Open the live diligence system →</a></section>'
        +'<div class="reveal act3-capstone-bridge"><p>The lawyer authors the architecture. Technology preserves it through execution.</p><a href="#capstone">Continue to Capstone →</a></div>'
      +'</div></section>'
    ));

    function renderOperation(i){
      var idx=(i+workflow.length)%workflow.length,s=workflow[idx];
      document.querySelectorAll('[data-act3-operation]').forEach(function(btn,n){var active=n===idx;btn.classList.toggle('active',active);btn.setAttribute('aria-selected',active?'true':'false');});
      document.getElementById('act3-operation-panel').innerHTML='<div class="act3-operation-id"><span>0'+(idx+1)+' / 05</span><h3>'+esc(s.title)+'</h3></div><div class="act3-operation-block"><strong>Purpose</strong><p>'+esc(s.purpose)+'</p></div><div class="act3-operation-block"><strong>Governing principle</strong><p>'+esc(s.principle)+'</p></div>';
    }
    function renderTrace(key){
      var t=traces[key]||traces.payment;
      document.querySelectorAll('[data-act3-trace]').forEach(function(btn){var active=btn.getAttribute('data-act3-trace')===key;btn.classList.toggle('active',active);btn.setAttribute('aria-selected',active?'true':'false');});
      document.getElementById('act3-trace-panel').innerHTML=t.rows.map(function(r){return '<div class="act3-trace-row"><strong>'+esc(r[0])+'</strong><span>'+esc(r[1])+'</span></div>';}).join('');
    }
    document.querySelectorAll('[data-act3-operation]').forEach(function(btn){btn.addEventListener('click',function(){renderOperation(parseInt(btn.getAttribute('data-act3-operation'),10));});});
    document.querySelectorAll('[data-act3-trace]').forEach(function(btn){btn.addEventListener('click',function(){renderTrace(btn.getAttribute('data-act3-trace'));});});
    renderOperation(0);
    renderTrace('payment');
  })();

'''
text = text[:start] + new_block + text[end:]

old_flow = "capstoneFlow(['Doctrine','Taxonomy','Diligence Architecture','Review-bound Runtime'])"
new_flow = "capstoneFlow(['Legal Grammar','Applied Legal Architecture','Supporting Workflow'])"
if old_flow not in text:
    raise SystemExit('Capstone flow source not found')
text = text.replace(old_flow, new_flow, 1)

path.write_text(text, encoding='utf-8')
print('Act III rebuilt as Legal Architecture in Operation.')
