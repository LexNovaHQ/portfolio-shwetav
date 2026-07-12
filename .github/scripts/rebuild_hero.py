from __future__ import annotations

import json
import re
from pathlib import Path

INDEX = Path("index.html")
CONTENT = Path("content.json")

html = INDEX.read_text(encoding="utf-8")

# ---------------------------------------------------------------------------
# 1. Keep the original UI, but add hero-local styles only.
# ---------------------------------------------------------------------------
hero_css = r'''

/* ---- LAWYER-FIRST HERO SURGERY START ---- */
.hero-grid{display:grid;gap:1.35rem;align-items:stretch;}
@media(min-width:1024px){.hero-grid{grid-template-columns:minmax(0,1.12fr) minmax(330px,.88fr);gap:1.35rem;}}
.hero-brief{height:100%;border-top:2px solid var(--gold);padding:1.15rem 1.05rem;background:linear-gradient(180deg,rgba(197,160,89,.075),rgba(255,255,255,.018));}
.hero-brief h3{margin:.1rem 0 .9rem;font-family:"Cormorant Garamond",Georgia,serif;color:#fff;font-size:1.75rem;line-height:1.02;font-weight:500;}
.hero-brief-row{padding:.72rem 0;border-top:1px solid rgba(197,160,89,.2);}
.hero-brief-row:first-of-type{border-top:0;padding-top:.15rem;}
.hero-brief-row strong{display:block;margin-bottom:.28rem;color:var(--gold);font-size:.55rem;letter-spacing:.14em;text-transform:uppercase;font-weight:800;}
.hero-brief-row span{display:block;color:rgba(229,229,229,.73);font-size:.75rem;line-height:1.52;}
.legal-method-intro{max-width:61rem;color:rgba(229,229,229,.75);font-size:.86rem;line-height:1.65;margin:.85rem 0 0;}
.legal-method-chain{display:grid;grid-template-columns:1fr;gap:.65rem;margin-top:1.15rem;}
@media(min-width:700px){.legal-method-chain{grid-template-columns:repeat(2,minmax(0,1fr));}}
@media(min-width:1120px){.legal-method-chain{grid-template-columns:repeat(6,minmax(0,1fr));}}
.legal-method-step{position:relative;min-height:154px;border:1px solid rgba(229,229,229,.1);border-radius:.9rem;background:rgba(255,255,255,.018);padding:.82rem;text-align:left;color:rgba(229,229,229,.76);cursor:pointer;transition:border-color .22s,background .22s,transform .22s,box-shadow .22s;}
.legal-method-step:hover,.legal-method-step:focus{outline:none;border-color:rgba(197,160,89,.68);background:rgba(197,160,89,.07);transform:translateY(-2px);box-shadow:0 14px 34px rgba(0,0,0,.28);}
.legal-method-step .num{display:inline-flex;align-items:center;justify-content:center;width:1.5rem;height:1.5rem;border:1px solid rgba(197,160,89,.46);border-radius:999px;color:var(--gold);font-size:.58rem;font-weight:800;margin-bottom:.62rem;}
.legal-method-step strong{display:block;color:#f0ece5;font-family:"Cormorant Garamond",Georgia,serif;font-size:1.13rem;line-height:1.02;font-weight:600;}
.legal-method-step p{margin:.52rem 0 0;color:rgba(229,229,229,.57);font-size:.67rem;line-height:1.48;}
.regulatory-signal-strip{display:grid;grid-template-columns:auto minmax(0,1fr);gap:.85rem;align-items:start;margin-top:.85rem;padding:.85rem .95rem;border:1px solid rgba(197,160,89,.28);border-left:2px solid var(--gold);border-radius:.85rem;background:linear-gradient(90deg,rgba(197,160,89,.09),rgba(255,255,255,.014));}
.regulatory-signal-strip .loop{color:var(--gold);font-family:"Cormorant Garamond",Georgia,serif;font-size:1.7rem;line-height:1;}
.regulatory-signal-strip strong{display:block;color:var(--gold);font-size:.6rem;letter-spacing:.14em;text-transform:uppercase;margin-bottom:.25rem;}
.regulatory-signal-strip p{margin:0;color:rgba(229,229,229,.67);font-size:.76rem;line-height:1.55;}
.hero-method-cta{display:flex;flex-direction:column;gap:.65rem;align-items:flex-start;margin-top:1.05rem;padding-top:1rem;border-top:1px solid rgba(197,160,89,.18);}
@media(min-width:720px){.hero-method-cta{flex-direction:row;align-items:center;justify-content:space-between;}}
.hero-method-actions{display:flex;flex-wrap:wrap;gap:.65rem;}
.hero-method-note{max-width:34rem;color:rgba(229,229,229,.46);font-size:.65rem;line-height:1.5;}
/* ---- LAWYER-FIRST HERO SURGERY END ---- */
'''

if "/* ---- LAWYER-FIRST HERO SURGERY START ---- */" not in html:
    html = html.replace("</style>", hero_css + "\n</style>", 1)

# ---------------------------------------------------------------------------
# 2. Update the embedded content source and external content.json in sync.
# ---------------------------------------------------------------------------
match = re.search(
    r'<script id="content-data" type="application/json">(.*?)</script>',
    html,
    flags=re.S,
)
if not match:
    raise RuntimeError("content-data block not found")

content = json.loads(match.group(1))
hero = content.setdefault("hero", {})
hero.update(
    {
        "name": "Shwetav Singh",
        "identity_line": "Technology & Data Protection Lawyer | AI Governance · Cross-Border Privacy · Commercial Contracts for Technology",
        "headline": "Technology changes the fact pattern. Legal judgment determines the position.",
        "hook": "Technology changes the fact pattern. Legal judgment determines the position.",
        "builder_line": "I work at the point where product mechanics, evidence and legal consequence meet.",
        "foundation_paragraph": "My legal foundation is 3.5 years of litigation. That experience taught me to separate assertion from evidence, identify the issue that actually determines the outcome, and draft for scrutiny rather than appearance. I now apply that discipline to technology, data, AI governance and commercial-contract work—understanding how the product operates, identifying the legal consequences, and translating those conclusions into contracts, controls and review-ready legal work.",
        "thesis": "The work is not complete when a risk is identified. It is complete when the legal position is evidenced, defensible and capable of being implemented.",
        "formation_spine": [],
        "proof_architecture": [
            "Doctrine",
            "Product Reality",
            "Legal Classification",
            "Exposure Analysis",
            "Legal Instruments",
            "Review-Ready Delivery",
        ],
        "ctas": [
            {"label": "See the legal architecture", "target": "#act2-threat-matrix"},
            {
                "label": "Enter the diligence sandbox",
                "target": "https://sandbox.lexnovahq.com/interface-diligence/diligence-system/",
            },
        ],
        "proof_line": "Portfolio examples use public, synthetic or scrubbed materials. The live sandbox demonstrates the delivery workflow; final legal reliance remains with qualified counsel.",
        "credential_bar": "3.5 years litigation · B.A. LL.B., NLU Odisha · AI governance · cross-border privacy · commercial contracts · legal systems",
    }
)

meta = content.setdefault("_meta", {})
meta.update(
    {
        "page_title": "Shwetav Singh — Technology & Data Protection Lawyer",
        "og_title": "Shwetav Singh — Technology & Data Protection Lawyer",
        "og_description": "Technology, data protection, AI governance and commercial-contract work grounded in litigation, evidence and reviewable legal judgment.",
        "footer": "© 2026 Shwetav Singh",
    }
)

content_json = json.dumps(content, ensure_ascii=False, separators=(",", ":"))
html = html[: match.start(1)] + content_json + html[match.end(1) :]
CONTENT.write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# Also correct document metadata without touching the UI.
html = re.sub(
    r"<title>.*?</title>",
    "<title>Shwetav Singh — Technology & Data Protection Lawyer</title>",
    html,
    count=1,
    flags=re.S,
)
html = re.sub(
    r'<meta name="description" content=".*?"/>',
    '<meta name="description" content="Technology, data protection, AI governance and commercial-contract work grounded in litigation, evidence and reviewable legal judgment."/>',
    html,
    count=1,
    flags=re.S,
)
html = re.sub(
    r'<meta property="og:title" content=".*?"/>',
    '<meta property="og:title" content="Shwetav Singh — Technology & Data Protection Lawyer"/>',
    html,
    count=1,
    flags=re.S,
)
html = re.sub(
    r'<meta property="og:description" content=".*?"/>',
    '<meta property="og:description" content="Technology, data protection, AI governance and commercial-contract work grounded in litigation, evidence and reviewable legal judgment."/>',
    html,
    count=1,
    flags=re.S,
)

# ---------------------------------------------------------------------------
# 3. Replace only the hero renderer. No global shell/navigation/rail changes.
# ---------------------------------------------------------------------------
hero_renderer = r'''  // ---------- HERO ----------
  (function(){
    var h=C.hero || {};
    main.appendChild(el(
    '<section id="hero" class="act" data-rail="0" style="min-height:auto; display:flex; align-items:center">'
    +'<div class="card-shell w-full">'
      +'<div class="hero-grid">'
        +'<div>'
          +'<h1 class="load-in font-display hero-name">'+esc(h.name || 'Shwetav Singh')+'</h1>'
          +'<p class="load-in d1 text-sm sm:text-base mt-2 hero-identity">'+esc(h.identity_line || '')+'</p>'
          +'<div class="hairline my-4"></div>'
          +'<h2 class="load-in d2 font-display text-white hero-hook">'+esc(h.headline || h.hook || '')+'</h2>'
          +'<p class="load-in d3 text-sm mt-4 hero-builder">'+esc(h.builder_line || '')+'</p>'
          +'<p class="load-in d4 hero-foundation">'+esc(h.foundation_paragraph || '')+'</p>'
          +'<p id="hero-thesis" class="load-in d4 font-display italic gold hero-thesis">'+esc(h.thesis || '')+'</p>'
        +'</div>'
        +'<aside class="load-in d3 surface rounded-2xl hero-brief" aria-label="Professional summary">'
          +'<h3>Law first. Systems second.</h3>'
          +'<div class="hero-brief-row"><strong>Legal foundation</strong><span>Litigation-trained issue analysis, evidence discipline, procedural judgment and drafting.</span></div>'
          +'<div class="hero-brief-row"><strong>Practice focus</strong><span>Technology, data protection, AI governance and commercial contracts.</span></div>'
          +'<div class="hero-brief-row"><strong>Applied method</strong><span>Product reality → legal classification → exposure analysis → legal instruments.</span></div>'
          +'<div class="hero-brief-row"><strong>What it proves</strong><span>I can convert complex technology facts into a structured legal position that remains reviewable by counsel.</span></div>'
        +'</aside>'
      +'</div>'
      +'<div class="load-in d5 surface rounded-2xl hero-credential" style="color:rgba(229,229,229,.8);border-left:1px solid var(--gold)">'+esc(h.credential_bar || '')+'</div>'
    +'</div></section>'));
  })();

'''

html, hero_count = re.subn(
    r"  // ---------- HERO ----------.*?(?=  // ---------- SECTION 2 / PROOF ARCHITECTURE ----------)",
    hero_renderer,
    html,
    count=1,
    flags=re.S,
)
if hero_count != 1:
    raise RuntimeError(f"hero renderer replacement count={hero_count}")

# ---------------------------------------------------------------------------
# 4. Replace Proof Architecture with a lawyer-first six-stage legal method.
#    CTA appears only after all six stages and the regulatory feedback strip.
# ---------------------------------------------------------------------------
method_renderer = r'''  // ---------- SECTION 2 / HOW I APPLY THE LAW ----------
  (function(){
    var h=C.hero || {};
    var methodChain=[
      {
        title:'Doctrine',
        short:'Identify the governing legal principles, duties, authorities and accepted interpretive boundaries.',
        practice:'The work begins with the governing rules, authorities and legal principles—not with a tool, taxonomy or product label.',
        application:'I identify the legal questions that control the matter and the evidential propositions that must be proved or qualified.',
        result:'A defined legal source and issue framework.'
      },
      {
        title:'Product Reality',
        short:'Establish what the business, product and activity actually do.',
        practice:'Commercial labels do not determine legal character. The factual operation, actors, inputs, outputs, affected parties and control structure do.',
        application:'I reconstruct the target and separate marketing claims from legally material product and activity facts.',
        result:'An evidenced factual record for legal analysis.'
      },
      {
        title:'Legal Classification',
        short:'Characterise the conduct, role and legally relevant surface.',
        practice:'The same technology can create different legal consequences depending on function, role, affected party, data, market and decision context.',
        application:'I classify the legally material conduct without treating a category or signal as a concluded exposure.',
        result:'The correct obligation and authority universe.'
      },
      {
        title:'Exposure Analysis',
        short:'Test relevant duties and risks against evidence, controls and exclusions.',
        practice:'An identified risk surface is not proof of breach or liability. The trigger conditions must be tested against the available record.',
        application:'I distinguish triggered issues, controlled issues, evidence limitations and matters that require further legal review.',
        result:'A reasoned legal position with stated limitations.'
      },
      {
        title:'Legal Instruments',
        short:'Translate the confirmed position into contracts, policies, controls and review questions.',
        practice:'The remedy must match the legal problem. A clause cannot repair a defective consent flow, and a technical control cannot resolve an allocation failure by itself.',
        application:'I route each confirmed issue into the legal instrument, operational control, evidence request or counsel question capable of addressing it.',
        result:'Coordinated drafting and control routes.'
      },
      {
        title:'Review-Ready Delivery',
        short:'Present the position, record, open questions and drafting routes for counsel review.',
        practice:'Structured preparation should make legal review faster and more reliable without pretending to replace qualified judgment.',
        application:'I assemble the findings, evidence basis, limitations, proposed instruments and local-law questions into review-ready work.',
        result:'A defensible handoff for qualified and local counsel.'
      }
    ];
    var chainHtml=methodChain.map(function(item,i){
      return '<button class="legal-method-step" type="button" data-method-chain="'+i+'">'
        +'<span class="num">0'+(i+1)+'</span><strong>'+esc(item.title)+'</strong><p>'+esc(item.short)+'</p></button>';
    }).join('');
    var ctas=Array.isArray(h.ctas)?h.ctas:[];
    var architecture=ctas[0]||{label:'See the legal architecture',target:'#act2-threat-matrix'};
    var sandbox=ctas[1]||{label:'Enter the diligence sandbox',target:'https://sandbox.lexnovahq.com/interface-diligence/diligence-system/'};

    main.appendChild(el(
    '<section id="proof-architecture" class="act" style="min-height:auto">'
    +'<div class="card-shell">'
      +'<div class="reveal">'
        +'<p class="eyebrow">How I Apply the Law</p>'
        +'<h2 class="font-display section-title text-white mt-2">From governing rule to review-ready legal work.</h2>'
        +'<p class="legal-method-intro">The sequence below is the legal method. Technology supports the preparation, traceability and handoff; it does not replace the judgment required at any stage.</p>'
      +'</div>'
      +'<div class="reveal legal-method-chain" aria-label="Legal method chain">'+chainHtml+'</div>'
      +'<div class="reveal regulatory-signal-strip"><span class="loop">↺</span><div><strong>Regulatory Update Signals</strong><p>New legislation, regulatory guidance, enforcement action and case law feed back into doctrine, legal classification, exposure tests and legal instruments. The method is maintained as a living legal framework, not frozen at the date of first delivery.</p></div></div>'
      +'<div class="reveal hero-method-cta">'
        +'<div class="hero-method-actions">'
          +'<a class="btn" href="'+esc(architecture.target || '#act2-threat-matrix')+'">'+esc(architecture.label || 'See the legal architecture')+'</a>'
          +'<a class="btn sec" href="'+esc(sandbox.target || 'https://sandbox.lexnovahq.com/interface-diligence/diligence-system/')+'" data-interface-os-gate="true">'+esc(sandbox.label || 'Enter the diligence sandbox')+'</a>'
        +'</div>'
        +'<p class="hero-method-note">'+esc(h.proof_line || '')+'</p>'
      +'</div>'
    +'</div></section>'));

    document.querySelectorAll('[data-method-chain]').forEach(function(btn){
      btn.addEventListener('click',function(){
        var item=methodChain[parseInt(btn.getAttribute('data-method-chain'),10)]||methodChain[0];
        openModal('<p class="eyebrow">How I Apply the Law</p><h3>'+esc(item.title)+'</h3>'
          +'<div class="beat"><div class="lab">What it means in legal practice</div><p>'+esc(item.practice)+'</p></div>'
          +'<div class="beat"><div class="lab">How I apply it</div><p>'+esc(item.application)+'</p></div>'
          +'<div class="beat"><div class="lab">Result</div><p>'+esc(item.result)+'</p></div>',false);
      });
    });
  })();

'''

html, method_count = re.subn(
    r"  // ---------- SECTION 2 / PROOF ARCHITECTURE ----------.*?(?=  // ---------- ACT I ----------)",
    method_renderer,
    html,
    count=1,
    flags=re.S,
)
if method_count != 1:
    raise RuntimeError(f"method renderer replacement count={method_count}")

# ---------------------------------------------------------------------------
# 5. Mechanical assertions.
# ---------------------------------------------------------------------------
for required in [
    "How I Apply the Law",
    "Doctrine",
    "Product Reality",
    "Legal Classification",
    "Exposure Analysis",
    "Legal Instruments",
    "Review-Ready Delivery",
    "Regulatory Update Signals",
    "Law first. Systems second.",
]:
    if required not in html:
        raise RuntimeError(f"missing required hero text: {required}")

if "Proof Architecture</p>" in html:
    raise RuntimeError("old visible Proof Architecture label still active")

chain_pos = html.find("legal-method-chain")
cta_pos = html.find("hero-method-cta")
if chain_pos < 0 or cta_pos < 0 or cta_pos <= chain_pos:
    raise RuntimeError("CTA does not occur after the six-stage chain")

# IDs in static HTML should remain unique. IDs appearing inside JS strings are
# intentionally counted only at literal markup boundaries elsewhere by runtime.
INDEX.write_text(html, encoding="utf-8")

print("Hero surgery: PASS")
print("Original UI shell retained; hero and immediate legal-method section rebuilt.")
