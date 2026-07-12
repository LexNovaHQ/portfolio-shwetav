from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Reposition Act I as the legal grammar rather than the complete matter journey.
replacements = {
    'From facts to legal position.': 'How I determine what legally matters.',
    'Complex technology matters do not begin with a list of laws. They begin with characterising the conduct, identifying the legally relevant role and context, testing the governing rule against evidence, and reaching a position that can be drafted, controlled or escalated for review.': 'Commercial labels do not determine legal consequences. The lawyer must identify the conduct, role, context and terminal harm; select the governing authority; test the factual trigger and exclusion; and determine the consequence and appropriate response.',
    'What the method produces': 'What the grammar establishes',
    '<span>Reasoned Position</span><span>Evidence Basis</span><span>Applicable Authority</span><span>Limitations</span><span>Legal Instrument</span><span>Review Route</span>': '<span>Material Conduct</span><span>Duty-Bearing Role</span><span>Relevant Context</span><span>Terminal Harm</span><span>Governing Authority</span><span>Trigger / Exclusion</span><span>Consequence</span><span>Response Direction</span>',
    'A legal position that states what is supported, what is excluded, what remains uncertain, and what instrument or review route is capable of addressing it.': 'A disciplined legal frame that identifies what must be characterised, proved, excluded, prioritised and routed before a complex matter can be reconstructed.',
    'The method is only valuable if it survives contact with a complex matter. Act II applies it to an integrated product and its legally distinct activities.': 'These dimensions identify the legally material parts. Act II shows how I use them to dismantle a complex commercial matter, test the consequences of its facts and reconstruct the result into one coherent legal architecture.'
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'Act I source text not found: {old[:80]}')
    text = text.replace(old, new, 1)

css_marker = '/* ---- MINIMALIST ACT II START ---- */'
css = r'''
/* ---- MINIMALIST ACT II START ---- */
.act2-matter{padding-bottom:1.55rem;}
.act2-opening{max-width:62rem;}
.act2-opening h2{max-width:54rem;}
.act2-opening-copy{max-width:58rem;margin:.85rem 0 0;color:rgba(229,229,229,.67);font-size:.86rem;line-height:1.7;}
.act2-matter-brief{display:grid;grid-template-columns:minmax(0,.82fr) minmax(0,1.18fr);gap:1.2rem;margin-top:1.55rem;padding:1rem 0;border-top:1px solid rgba(197,160,89,.25);border-bottom:1px solid rgba(229,229,229,.08);}
.act2-brief-kicker{color:var(--gold);font-size:.55rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;}
.act2-brief-title{margin:.25rem 0 0;font-family:"Cormorant Garamond",Georgia,serif;color:#f4efe7;font-size:1.55rem;line-height:1.05;font-weight:500;}
.act2-brief-copy{margin:.45rem 0 0;color:rgba(229,229,229,.58);font-size:.76rem;line-height:1.62;}
.act2-brief-question{padding-left:1rem;border-left:1px solid rgba(197,160,89,.24);}
.act2-brief-question strong{display:block;margin-bottom:.35rem;color:var(--gold);font-size:.55rem;font-weight:800;letter-spacing:.13em;text-transform:uppercase;}
.act2-brief-question p{margin:0;color:rgba(229,229,229,.72);font-family:"Cormorant Garamond",Georgia,serif;font-size:1.08rem;line-height:1.4;}
.act2-movement-shell{margin-top:1.5rem;border-top:1px solid rgba(229,229,229,.08);}
.act2-movement-nav{display:grid;grid-template-columns:repeat(3,1fr);border-bottom:1px solid rgba(229,229,229,.09);}
.act2-movement-tab{position:relative;padding:.78rem .65rem .82rem;border:0;border-right:1px solid rgba(229,229,229,.07);background:transparent;color:rgba(229,229,229,.42);text-align:left;cursor:pointer;transition:color .2s,background .2s;}
.act2-movement-tab:last-child{border-right:0;}
.act2-movement-tab::after{content:"";position:absolute;left:.65rem;right:.65rem;bottom:-1px;height:1px;background:transparent;}
.act2-movement-tab:hover,.act2-movement-tab:focus,.act2-movement-tab.active{outline:none;color:var(--gold);background:rgba(197,160,89,.03);}
.act2-movement-tab.active::after{background:var(--gold);box-shadow:0 0 10px rgba(197,160,89,.55);}
.act2-movement-tab .n{display:block;margin-bottom:.22rem;color:rgba(197,160,89,.66);font-size:.52rem;font-weight:800;letter-spacing:.13em;}
.act2-movement-tab .t{display:block;font-family:"Cormorant Garamond",Georgia,serif;font-size:1.08rem;line-height:1;color:inherit;}
.act2-movement-panel{padding:1.15rem 0 1.25rem;min-height:365px;}
.act2-movement-head{max-width:55rem;}
.act2-movement-head h3{margin:.28rem 0 0;font-family:"Cormorant Garamond",Georgia,serif;color:#f4efe7;font-size:1.8rem;line-height:1.02;font-weight:500;}
.act2-movement-head p{margin:.55rem 0 0;color:rgba(229,229,229,.6);font-size:.77rem;line-height:1.62;}
.act2-component-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:1rem;border-top:1px solid rgba(197,160,89,.22);border-bottom:1px solid rgba(229,229,229,.075);}
.act2-component{padding:.8rem .75rem;border-right:1px solid rgba(229,229,229,.075);}
.act2-component:nth-child(4n){border-right:0;}
.act2-component:nth-child(-n+4){border-bottom:1px solid rgba(229,229,229,.075);}
.act2-component strong{display:block;color:#eee8df;font-family:"Cormorant Garamond",Georgia,serif;font-size:1.02rem;font-weight:500;line-height:1.05;}
.act2-component span{display:block;margin-top:.28rem;color:rgba(229,229,229,.5);font-size:.68rem;line-height:1.5;}
.act2-thread-summary{margin:.8rem 0 0;color:rgba(229,229,229,.48);font-size:.7rem;line-height:1.55;}
.act2-thread-tabs{display:flex;gap:1rem;overflow-x:auto;margin-top:.9rem;border-bottom:1px solid rgba(229,229,229,.09);}
.act2-thread-tab{position:relative;flex:0 0 auto;padding:.55rem 0 .65rem;border:0;background:transparent;color:rgba(229,229,229,.42);font-size:.6rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;cursor:pointer;}
.act2-thread-tab::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:1px;background:transparent;}
.act2-thread-tab:hover,.act2-thread-tab:focus,.act2-thread-tab.active{outline:none;color:var(--gold);}
.act2-thread-tab.active::after{background:var(--gold);box-shadow:0 0 9px rgba(197,160,89,.5);}
.act2-test-grid{margin-top:.8rem;border-top:1px solid rgba(197,160,89,.2);}
.act2-test-row{display:grid;grid-template-columns:165px minmax(0,1fr);gap:1rem;padding:.64rem 0;border-bottom:1px solid rgba(229,229,229,.07);}
.act2-test-row strong{color:var(--gold);font-size:.54rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;}
.act2-test-row span{color:rgba(229,229,229,.63);font-size:.72rem;line-height:1.55;}
.act2-architecture{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:1rem;border-top:1px solid rgba(197,160,89,.22);border-bottom:1px solid rgba(229,229,229,.075);}
.act2-architecture-col{padding:.82rem .8rem;border-right:1px solid rgba(229,229,229,.075);}
.act2-architecture-col:last-child{border-right:0;}
.act2-architecture-col strong{display:block;color:var(--gold);font-size:.54rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;}
.act2-architecture-col p{margin:.38rem 0 0;color:rgba(229,229,229,.58);font-size:.7rem;line-height:1.55;}
.act2-reconstruction-note{margin:.85rem 0 0;padding-left:.85rem;border-left:1px solid rgba(197,160,89,.35);color:rgba(229,229,229,.68);font-family:"Cormorant Garamond",Georgia,serif;font-size:1.08rem;line-height:1.4;}
.act2-output{padding-top:1.15rem;border-top:1px solid rgba(197,160,89,.22);}
.act2-output p{max-width:54rem;margin:.35rem 0 0;color:rgba(229,229,229,.55);font-size:.73rem;line-height:1.55;}
.act2-output-strip{display:flex;flex-wrap:wrap;gap:.35rem 1rem;margin-top:.8rem;color:rgba(229,229,229,.7);font-size:.58rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;}
.act2-output-strip span+span::before{content:"";display:inline-block;width:14px;height:1px;margin:0 .62rem .2rem 0;background:rgba(197,160,89,.46);}
.act2-boundary{display:grid;grid-template-columns:1fr 1fr;gap:1.15rem;margin-top:1.35rem;padding-top:1rem;border-top:1px solid rgba(229,229,229,.08);}
.act2-boundary-block{padding-right:1rem;}
.act2-boundary-block+.act2-boundary-block{padding-left:1rem;padding-right:0;border-left:1px solid rgba(197,160,89,.2);}
.act2-boundary-block strong{display:block;color:var(--gold);font-size:.55rem;font-weight:800;letter-spacing:.13em;text-transform:uppercase;}
.act2-boundary-block p{margin:.35rem 0 0;color:rgba(229,229,229,.59);font-size:.73rem;line-height:1.55;}
.act2-bridge{display:flex;align-items:center;justify-content:space-between;gap:1rem;margin-top:1rem;padding-top:.9rem;border-top:1px solid rgba(229,229,229,.07);}
.act2-bridge p{margin:0;max-width:50rem;color:rgba(229,229,229,.67);font-family:"Cormorant Garamond",Georgia,serif;font-size:1.07rem;line-height:1.38;}
.act2-bridge a{flex:0 0 auto;color:var(--gold);font-size:.59rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;border-bottom:1px solid rgba(197,160,89,.45);padding-bottom:.23rem;}
@media(max-width:900px){
  .act2-component-grid{grid-template-columns:repeat(2,1fr);}.act2-component:nth-child(2n){border-right:0;}.act2-component:nth-child(-n+6){border-bottom:1px solid rgba(229,229,229,.075);}.act2-architecture{grid-template-columns:repeat(2,1fr);}.act2-architecture-col:nth-child(2){border-right:0;}.act2-architecture-col:nth-child(-n+2){border-bottom:1px solid rgba(229,229,229,.075);}
}
@media(max-width:640px){
  .act2-matter-brief,.act2-boundary{grid-template-columns:1fr;}.act2-brief-question{padding:.8rem 0 0;border-left:0;border-top:1px solid rgba(197,160,89,.2);}.act2-movement-tab{padding-left:.4rem;padding-right:.4rem;}.act2-movement-tab .t{font-size:.95rem;}.act2-component-grid,.act2-architecture{grid-template-columns:1fr;}.act2-component,.act2-component:nth-child(n),.act2-architecture-col{border-right:0;border-bottom:1px solid rgba(229,229,229,.075);}.act2-component:last-child,.act2-architecture-col:last-child{border-bottom:0;}.act2-test-row{grid-template-columns:1fr;gap:.2rem;}.act2-boundary-block+.act2-boundary-block{padding:.8rem 0 0;border-left:0;border-top:1px solid rgba(197,160,89,.2);}.act2-bridge{align-items:flex-start;flex-direction:column;}.act2-output-strip{display:grid;gap:.4rem;}.act2-output-strip span+span::before{display:none;}
}
/* ---- MINIMALIST ACT II END ---- */
'''
if css_marker not in text:
    text = text.replace('</style>', css + '\n</style>', 1)

start = text.find('  // ---------- ACT II ----------')
end = text.find('  function normalizeAct2', start)
if start < 0 or end < 0:
    raise SystemExit('Act II replacement markers not found')

act2 = r'''  // ---------- ACT II ----------
  (function(){
    var movements=[
      {key:'deconstruct',label:'Deconstruct'},
      {key:'test',label:'Test'},
      {key:'reconstruct',label:'Reconstruct'}
    ];
    var threads={
      payment:{
        label:'Payment Orchestration',
        material:'AsterPay may initiate or orchestrate payment instructions while relying on licensed partners for account, settlement or funds movement.',
        question:'Which entity performs the regulated payment function, and who controls, receives or holds customer funds in substance?',
        duty:'Payment-perimeter, role-disclosure, safeguarding, settlement, consumer-representation and contractual-allocation duties.',
        trigger:'AsterPay controls initiation, execution, routing, funds handling or customer-facing responsibility in substance.',
        exclude:'A licensed partner exclusively performs the regulated function and the product, contracts and actual flow preserve that boundary.',
        evidence:'Funds-flow map, partner agreement, customer terms, settlement records, permissions and operational controls.',
        consequence:'Mischaracterised role, safeguarding or disclosure exposure, defective allocation and market-access questions.',
        limitation:'Public materials cannot establish the complete contractual or operational allocation.'
      },
      credit:{
        label:'Credit Scoring',
        material:'An automated score may materially influence whether a customer receives access to a financial product or commercial opportunity.',
        question:'Is the score merely informative, or does it participate in a consequential decision?',
        duty:'Fair-treatment, reason-giving, automated-decision, discrimination, data-protection and responsibility-allocation duties.',
        trigger:'The score materially determines, constrains or effectively controls the outcome.',
        exclude:'An independent decision-maker genuinely reassesses the relevant facts and retains authority to depart from the score.',
        evidence:'Decision flow, override records, reason-generation process, data inputs and actual reviewer authority.',
        consequence:'Financial-domain, discrimination, automated-decision and data-protection issues may arise through different legal routes.',
        limitation:'The public record cannot establish whether the human-review process is substantive.'
      },
      identity:{
        label:'Identity & KYC',
        material:'The onboarding flow may collect identity, financial and potentially biometric data before deciding whether access is permitted.',
        question:'What data is necessary for verification, who determines the result, and what exception route exists when the process fails?',
        duty:'KYC/AML, data-minimisation, transparency, retention, security, accuracy and review-route duties.',
        trigger:'The process collects or infers protected data, materially controls access, or lacks an effective correction and exception route.',
        exclude:'The provider performs only a limited verification service with proportionate data use and a genuine manual exception path.',
        evidence:'Data-field inventory, vendor role, retention schedule, decision flow, biometric use and exception records.',
        consequence:'Onboarding failure, wrongful denial, privacy exposure, defective vendor allocation or missing-proof escalation.',
        limitation:'Private processing details and actual exception performance require confirmation.'
      },
      dependency:{
        label:'Provider Dependencies',
        material:'AsterPay may depend on payment partners, identity vendors, model providers and infrastructure services for legally material functions.',
        question:'Which obligations remain with AsterPay, which are delegated, and which cannot be transferred by contract?',
        duty:'Vendor governance, data-processing, service continuity, responsibility allocation, audit, incident and customer-disclosure duties.',
        trigger:'A third party performs a critical function while customer-facing responsibility, control or legal duty remains with AsterPay.',
        exclude:'The dependency is non-material and the contractual, operational and disclosure structure accurately preserves the legal boundary.',
        evidence:'Vendor contracts, subprocessors, service map, audit rights, incident terms, fallback controls and customer representations.',
        consequence:'Concentration, pass-through, service, data and responsibility gaps may affect several instruments at once.',
        limitation:'The operative vendor agreements and actual control environment are not publicly available.'
      }
    };

    var movementButtons=movements.map(function(m,i){
      return '<button class="act2-movement-tab'+(i===0?' active':'')+'" type="button" data-act2-movement="'+m.key+'" aria-selected="'+(i===0?'true':'false')+'"><span class="n">0'+(i+1)+'</span><span class="t">'+esc(m.label)+'</span></button>';
    }).join('');
    var threadButtons=Object.keys(threads).map(function(k,i){
      return '<button class="act2-thread-tab'+(i===0?' active':'')+'" type="button" data-act2-thread="'+k+'" aria-selected="'+(i===0?'true':'false')+'">'+esc(threads[k].label)+'</button>';
    }).join('');

    main.appendChild(el(
      '<section id="matrix" class="act" data-rail="2"><div class="card-shell act2-matter">'
      +'<header id="act2-orientation" class="reveal act2-opening"><p class="eyebrow">ACT II · APPLIED LEGAL ARCHITECTURE</p><h2 class="font-display section-title text-white mt-2">From Commercial Reality to Legal Architecture.</h2><p class="act2-opening-copy">How I deconstruct a complex matter into legally material facts, test the consequences of those facts against the relevant duties and authorities, and reconstruct the resulting conclusions into a coherent legal position.</p></header>'
      +'<section class="reveal act2-matter-brief"><div><span class="act2-brief-kicker">Synthetic matter · AsterPay</span><h3 class="act2-brief-title">One commercial proposition. Several legally distinct activities.</h3><p class="act2-brief-copy">A cross-border technology platform presenting a unified payment and financial-operations experience.</p></div><div class="act2-brief-question"><strong>The lawyer must determine</strong><p>Whether payment orchestration, identity verification, credit scoring, automated decisions, data processing, contractual representations and third-party dependencies create separate roles, duties and response routes.</p></div></section>'
      +'<section class="reveal act2-movement-shell"><nav class="act2-movement-nav" aria-label="Matter analysis movements">'+movementButtons+'</nav><div id="act2-movement-panel" class="act2-movement-panel" aria-live="polite"></div></section>'
      +'<span id="act2-threat-matrix" class="anchor-point" aria-hidden="true"></span><span id="act2-living-document" class="anchor-point" aria-hidden="true"></span><span id="instruments-layer" class="anchor-point" aria-hidden="true"></span><span id="act2-vault-router" class="anchor-point" aria-hidden="true"></span>'
      +'<section class="reveal act2-output"><p class="eyebrow">What the legal architecture contains</p><p>The result connects commercial reality, evidence, authority, consequence and implementation without overstating what the available record can support.</p><div class="act2-output-strip"><span>Commercial Model</span><span>Material Activities</span><span>Legal Roles</span><span>Legal Consequences</span><span>Position & Allocation</span><span>Instruments & Controls</span><span>Evidence Gaps</span><span>Review Route</span></div></section>'
      +'<section class="reveal act2-boundary"><div class="act2-boundary-block"><strong>Act II is the lawyer’s work</strong><p>Understand the matter, select the legally material facts, apply the relevant law, reconcile competing duties and construct the legal architecture.</p></div><div class="act2-boundary-block"><strong>Act III is supporting execution</strong><p>The diligence engine preserves evidence, structured testing, routing and review-ready handoff. It does not authorise the legal conclusion.</p></div></section>'
      +'<div id="act2-act3-bridge" class="reveal act2-bridge"><p>Once the legal architecture is defined, technology can support its execution without becoming the source of legal judgment.</p><a href="#tooling-layer">See the legal architecture in operation →</a></div>'
      +'</div></section>'
    ));

    var currentMovement='deconstruct', currentThread='payment';
    function component(title,body){ return '<div class="act2-component"><strong>'+esc(title)+'</strong><span>'+esc(body)+'</span></div>'; }
    function testRow(label,value){ return '<div class="act2-test-row"><strong>'+esc(label)+'</strong><span>'+esc(value)+'</span></div>'; }
    function renderThread(){
      var t=threads[currentThread];
      document.querySelectorAll('[data-act2-thread]').forEach(function(btn){var active=btn.getAttribute('data-act2-thread')===currentThread;btn.classList.toggle('active',active);btn.setAttribute('aria-selected',active?'true':'false');});
      var panel=document.getElementById('act2-thread-panel');
      if(panel) panel.innerHTML='<div class="act2-test-grid">'+testRow('Material fact',t.material)+testRow('Legal question',t.question)+testRow('Relevant duties / authorities',t.duty)+testRow('Trigger',t.trigger)+testRow('Exclusion',t.exclude)+testRow('Evidence required',t.evidence)+testRow('Consequence',t.consequence)+testRow('Limitation',t.limitation)+'</div>';
    }
    function renderMovement(key){
      currentMovement=key;
      document.querySelectorAll('[data-act2-movement]').forEach(function(btn){var active=btn.getAttribute('data-act2-movement')===key;btn.classList.toggle('active',active);btn.setAttribute('aria-selected',active?'true':'false');});
      var panel=document.getElementById('act2-movement-panel');
      if(key==='deconstruct'){
        panel.innerHTML='<div class="act2-movement-head"><p class="eyebrow">Movement I · Deconstruct</p><h3>Expose the legally distinct matter.</h3><p>The commercial proposition is dismantled into components the law can recognise. The company is not treated as one actor and the product is not treated as one activity.</p></div><div class="act2-component-grid">'
          +component('Activities','Payment orchestration · credit scoring · identity verification · automated operations')
          +component('Actors & roles','Platform · licensed partners · vendors · customers · decision-makers')
          +component('Value & transaction flows','Instructions · settlement · fees · funds movement · commercial benefit')
          +component('Data & regulated assets','Identity data · credit data · transaction data · customer funds')
          +component('Decisions & authority','Eligibility · onboarding · transaction action · override authority')
          +component('Documents & representations','Customer terms · partner terms · privacy notices · product claims')
          +component('Dependencies','Payment partners · KYC vendors · model providers · infrastructure')
          +component('Jurisdictions','Market access · customer location · processing location · governing law')
          +'</div><p class="act2-thread-summary">The output is not a risk list. It is a structured matter map showing which facts, actors and relationships require separate legal treatment.</p>';
      } else if(key==='test'){
        panel.innerHTML='<div class="act2-movement-head"><p class="eyebrow">Movement II · Test</p><h3>Test the legal consequence of each material fact.</h3><p>Each issue is tested against the relevant duty, authority, factual trigger, exclusion, evidence basis, consequence and limitation. One issue thread is shown at a time.</p></div><div class="act2-thread-tabs" role="tablist">'+threadButtons+'</div><div id="act2-thread-panel"></div>';
        document.querySelectorAll('[data-act2-thread]').forEach(function(btn){btn.addEventListener('click',function(){currentThread=btn.getAttribute('data-act2-thread');renderThread();});});
        renderThread();
      } else {
        panel.innerHTML='<div class="act2-movement-head"><p class="eyebrow">Movement III · Reconstruct</p><h3>Rebuild the separate findings into one coherent legal architecture.</h3><p>A complex matter cannot end as disconnected issues. The lawyer determines which finding controls, which duties overlap, who bears responsibility, what response addresses the root problem and what remains for counsel review.</p></div><div class="act2-architecture">'
          +'<div class="act2-architecture-col"><strong>Position</strong><p>Activity-specific conclusions, evidence basis, exclusions and limitations.</p></div>'
          +'<div class="act2-architecture-col"><strong>Allocation</strong><p>Actor, duty bearer, contractual responsibility and dependency boundaries.</p></div>'
          +'<div class="act2-architecture-col"><strong>Implementation</strong><p>Contracts, disclosures, operational controls, evidence requests and remediation priorities.</p></div>'
          +'<div class="act2-architecture-col"><strong>Review</strong><p>Conflicts, private facts, jurisdiction-specific questions and review sequence.</p></div>'
          +'</div><p class="act2-reconstruction-note">AsterPay is not treated as one undifferentiated product. Each activity receives its own role, consequence, evidence basis, response and review boundary before the matter is recombined.</p>';
      }
    }
    document.querySelectorAll('[data-act2-movement]').forEach(function(btn){btn.addEventListener('click',function(){renderMovement(btn.getAttribute('data-act2-movement'));});});
    renderMovement('deconstruct');
  })();

'''
text = text[:start] + act2 + text[end:]

# Synchronise only the Act III bridge language; do not redesign Act III in this pass.
act3_replacements = {
    "{title:'Diligence architecture', short:'Act II structure', detail:'The locked report architecture from Act II becomes the runtime blueprint. The registry changes by vertical; the profile and review structure stays fixed.'}": "{title:'Legal architecture', short:'Act II matter structure', detail:'The legal architecture from Act II becomes the runtime blueprint. The engine preserves the matter structure, evidence path and review boundaries without originating the legal judgment.'}",
    'How the diligence architecture runs as a public review system.': 'How the legal architecture becomes a public review workflow.',
    "flow(['Diligence architecture','Public source intake','Profile stack','Active registry application','Legal exposure report','Qualified review','Assembly handoff','Regulatory signal loop'])": "flow(['Legal architecture','Public source intake','Profile stack','Active registry application','Legal exposure report','Qualified review','Assembly handoff','Regulatory signal loop'])",
    'This is the Act II diligence architecture expressed as a running workflow.': 'This is the Act II legal architecture expressed as a review-bound workflow.',
    "detail:'The runtime applies the Act II architecture: factual profiles first, registry second, report third.'": "detail:'The runtime supports the Act II architecture: evidence and factual profiles first, structured testing second, review-ready reporting third.'"
}
for old, new in act3_replacements.items():
    if old not in text:
        raise SystemExit(f'Act III bridge text not found: {old[:90]}')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
print('Act I repositioned and Act II rebuilt.')
