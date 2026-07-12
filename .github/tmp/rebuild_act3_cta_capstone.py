from pathlib import Path
import json
import re

index_path = Path('index.html')
content_path = Path('content.json')
text = index_path.read_text(encoding='utf-8')

LIVE_URL = 'https://sandbox.lexnovahq.com/interface-diligence/diligence-system/'

# 1. Extend the existing minimalist Act III styles without replacing the visual system.
css_anchor = '/* ---- MINIMALIST ACT III END ---- */'
if css_anchor not in text:
    raise SystemExit('Act III CSS anchor missing')
extra_css = r'''
/* ---- ACT III CTA HIERARCHY + INTEGRATED SYNTHESIS START ---- */
.journey-bridge-actions{display:flex;align-items:center;justify-content:flex-end;gap:.9rem;flex-wrap:wrap;}
.upstream-system-link{opacity:.68!important;border-bottom-color:rgba(197,160,89,.22)!important;white-space:nowrap;}
.upstream-system-link:hover,.upstream-system-link:focus{opacity:1!important;}
.os-gate-intro{margin:.75rem 0 0;color:rgba(229,229,229,.76);font-size:.84rem;line-height:1.65;}
.os-gate-map{margin-top:.9rem;border-top:1px solid rgba(197,160,89,.2);}
.os-gate-map div{display:grid;grid-template-columns:72px minmax(0,1fr);gap:.75rem;padding:.58rem 0;border-bottom:1px solid rgba(229,229,229,.07);}
.os-gate-map strong{color:var(--gold);font-size:.56rem;letter-spacing:.12em;text-transform:uppercase;}
.os-gate-map span{color:rgba(229,229,229,.58);font-size:.74rem;line-height:1.5;}
.os-gate-actions{display:flex;gap:.7rem;align-items:center;flex-wrap:wrap;margin-top:1rem;}
.act3-synthesis{margin-top:1.45rem;padding-top:1.2rem;border-top:1px solid rgba(229,229,229,.08);}
.act3-synthesis h3{margin:.3rem 0 0;font-family:"Cormorant Garamond",Georgia,serif;color:#f4efe7;font-size:1.85rem;line-height:1.03;font-weight:500;}
.act3-synthesis-intro{max-width:58rem;margin:.55rem 0 0;color:rgba(229,229,229,.58);font-size:.76rem;line-height:1.62;}
.act3-synthesis-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin-top:1rem;border-top:1px solid rgba(197,160,89,.22);border-bottom:1px solid rgba(229,229,229,.08);}
.act3-synthesis-item{padding:.9rem .9rem 1rem;border-right:1px solid rgba(229,229,229,.075);}
.act3-synthesis-item:last-child{border-right:0;}
.act3-synthesis-item strong{display:block;color:var(--gold);font-size:.56rem;letter-spacing:.12em;text-transform:uppercase;}
.act3-synthesis-item p{margin:.4rem 0 0;color:rgba(229,229,229,.6);font-size:.73rem;line-height:1.58;}
.act3-synthesis-line{margin:1rem 0 0;padding-left:.9rem;border-left:2px solid var(--gold);font-family:"Cormorant Garamond",Georgia,serif;color:#f4efe7;font-size:1.35rem;line-height:1.35;}
.act3-launch{position:relative;overflow:hidden;margin-top:1.5rem;padding:1.5rem;border:1px solid rgba(197,160,89,.55);border-radius:1.15rem;background:linear-gradient(135deg,rgba(197,160,89,.16),rgba(197,160,89,.045) 42%,rgba(255,255,255,.018));box-shadow:0 28px 70px rgba(0,0,0,.34),inset 0 1px 0 rgba(255,255,255,.03);}
.act3-launch::before{content:"";position:absolute;inset:-45% auto auto 58%;width:420px;height:420px;border-radius:50%;background:radial-gradient(circle,rgba(197,160,89,.17),transparent 68%);pointer-events:none;}
.act3-launch-copy{position:relative;z-index:1;max-width:64rem;}
.act3-launch h3{margin:.3rem 0 0;font-family:"Cormorant Garamond",Georgia,serif;color:#fff;font-size:2.35rem;line-height:1.01;font-weight:500;}
.act3-launch p{max-width:56rem;margin:.7rem 0 0;color:rgba(244,240,232,.72);font-size:.82rem;line-height:1.68;}
.act3-launch-proof{position:relative;z-index:1;display:flex;flex-wrap:wrap;gap:.45rem 1rem;margin-top:1rem;color:rgba(244,240,232,.78);font-size:.58rem;font-weight:800;letter-spacing:.11em;text-transform:uppercase;}
.act3-launch-proof span+span::before{content:"";display:inline-block;width:15px;height:1px;margin:0 .7rem .2rem 0;background:rgba(197,160,89,.7);}
.act3-launch-action{position:relative;z-index:1;display:flex;align-items:end;justify-content:space-between;gap:1.2rem;margin-top:1.2rem;padding-top:1.05rem;border-top:1px solid rgba(197,160,89,.32);}
.act3-launch-btn{display:inline-flex;align-items:center;justify-content:center;min-height:58px;padding:.95rem 1.45rem;border-radius:999px;background:var(--gold);color:#080808!important;font-size:.68rem;font-weight:900;letter-spacing:.11em;text-transform:uppercase;box-shadow:0 14px 36px rgba(197,160,89,.2);transition:transform .2s,box-shadow .2s,filter .2s;white-space:nowrap;}
.act3-launch-btn:hover,.act3-launch-btn:focus{outline:none;transform:translateY(-2px);box-shadow:0 18px 44px rgba(197,160,89,.3);filter:brightness(1.05);}
.act3-launch-boundary{max-width:39rem!important;margin:0!important;color:rgba(229,229,229,.5)!important;font-size:.68rem!important;line-height:1.55!important;}
@media(max-width:760px){
  .journey-bridge-actions{justify-content:flex-start;}
  .act3-synthesis-grid{grid-template-columns:1fr;}.act3-synthesis-item{border-right:0;border-bottom:1px solid rgba(229,229,229,.075);}.act3-synthesis-item:last-child{border-bottom:0;}
  .act3-launch{padding:1.2rem 1rem;}.act3-launch h3{font-size:1.9rem;}.act3-launch-action{align-items:flex-start;flex-direction:column;}.act3-launch-btn{width:100%;white-space:normal;text-align:center;}.act3-launch-proof{display:grid;gap:.4rem;}.act3-launch-proof span+span::before{display:none;}
}
/* ---- ACT III CTA HIERARCHY + INTEGRATED SYNTHESIS END ---- */
'''
text = text.replace(css_anchor, extra_css + '\n' + css_anchor, 1)

# 2. Remove standalone Capstone from top navigation.
cap_nav = '      <a class="nav-link" href="#capstone">Capstone</a>\n'
if cap_nav not in text:
    raise SystemExit('Capstone top-nav link missing')
text = text.replace(cap_nav, '', 1)

# 3. Replace the stale runtime rail override with the final lawyer-first journey.
rail_pattern = re.compile(r"  /\* ---- ACT II / ACT III RAIL OVERRIDE START ---- \*/[\s\S]*?  /\* ---- ACT II DILIGENCE RAIL PATCH END ---- \*/")
locked_rail = r'''  /* ---- FINAL PORTFOLIO RAIL START ---- */
  var lockedRail = {
    chip: {
      derived: 'grammar → matter',
      structured: 'matter → architecture',
      running: 'architecture → workflow'
    },
    nodes: [
      {kind:'start', label:'Start', sub:'the thesis', target:'hero-thesis', why:'Establishes the claim: lawyer first, systems second.'},
      {band:'ACT I · LEGAL GRAMMAR', band_tag:'how I determine what matters', node:'Legal Lenses', sub:'conduct → role → consequence', target:'doctrine-layer', why:'Shows the recurring legal questions used to identify what is materially relevant.'},
      {band:'ACT I · LEGAL GRAMMAR', band_tag:'how I determine what matters', node:'Domain Vocabulary', sub:'behavior · lane · surface · terminal harm', target:'taxonomy-map', why:'Shows how the same legal grammar adapts without collapsing distinct domain vocabularies.'},
      {band:'ACT II · APPLIED LEGAL ARCHITECTURE', band_tag:'the commercial matter', node:'Deconstruct', sub:'commercial reality → legal parts', target:'act2-threat-matrix', why:'Shows how one commercial proposition becomes separate activities, roles, flows, data, decisions and dependencies.'},
      {band:'ACT II · APPLIED LEGAL ARCHITECTURE', band_tag:'the commercial matter', node:'Test & Reconstruct', sub:'duties → position → response', target:'act2-living-document', why:'Shows how material facts are tested and recombined into one coherent legal architecture.'},
      {band:'ACT III · LEGAL ARCHITECTURE IN OPERATION', band_tag:'architecture preserved', node:'Evidence Path', sub:'source → structured fact', target:'project-walkthrough', why:'Shows how the system preserves source evidence and the factual structure authored by the lawyer.'},
      {band:'ACT III · LEGAL ARCHITECTURE IN OPERATION', band_tag:'architecture preserved', node:'Legal Testing', sub:'controlled test → limitation', target:'act3-trace', why:'Shows one legal conclusion traced from source through controlled testing and evidence gaps.'},
      {band:'ACT III · LEGAL ARCHITECTURE IN OPERATION', band_tag:'architecture preserved', node:'Qualified Review', sub:'uncertainty → human judgment', target:'prompt-agent-proof', why:'Shows that unsupported or private facts become review questions instead of automated conclusions.'},
      {band:'ACT III · LEGAL ARCHITECTURE IN OPERATION', band_tag:'architecture preserved', node:'Handoff', sub:'position → review route', target:'act3-synthesis', why:'Shows the synthesis and review-ready route while preserving the lawyer’s boundary.'},
      {band:'ACT III · LEGAL ARCHITECTURE IN OPERATION', band_tag:'architecture preserved', node:'Open System', sub:'live supporting proof', target:'sandbox-os', why:'Opens the public-safe diligence workflow after the legal method and architecture are understood.'},
      {kind:'terminal', label:'Close', sub:'technology & data protection lawyer', target:'contact', why:'Converts the proof into the hiring argument.'}
    ]
  };
  C.rail = lockedRail;
  /* ---- FINAL PORTFOLIO RAIL END ---- */'''
text, rail_count = rail_pattern.subn(locked_rail, text, count=1)
if rail_count != 1:
    raise SystemExit(f'Rail override replacement failed: {rail_count}')

# 4. Replace the upstream system gate with a context-aware gate and direct continuation route.
gate_pattern = re.compile(r"  function openInterfaceOSGate\(url\)\{[\s\S]*?  \}\);\n  modal\.addEventListener", re.M)
new_gate = r'''  function openInterfaceOSGate(url, continueTarget){
    var target=continueTarget || '#foundation';
    openModal('<p class="eyebrow">Supporting system</p><h3>Understand the method before running the system.</h3>'
      +'<p class="os-gate-intro">The diligence system is supporting proof of the legal method shown in this portfolio. Continue through the portfolio for the correct context, or open the public-safe workflow now.</p>'
      +'<div class="os-gate-map"><div><strong>Act I</strong><span>Explains the legal grammar used to identify what materially matters.</span></div><div><strong>Act II</strong><span>Shows how the lawyer constructs the legal architecture from a complex commercial matter.</span></div><div><strong>Act III</strong><span>Shows how technology preserves that architecture through evidence, testing, review and handoff.</span></div></div>'
      +'<div class="os-gate-actions"><button class="btn" type="button" data-system-continue data-target="'+esc(target)+'">Continue reading</button><a class="btn sec" href="'+esc(url)+'" target="_blank" rel="noopener">Open the system anyway</a></div>', false);
  }
  document.addEventListener('click', function(e){
    var link=e.target.closest('[data-upstream-system-cta]');
    if(!link) return;
    e.preventDefault();
    openInterfaceOSGate(link.getAttribute('href') || 'https://sandbox.lexnovahq.com/interface-diligence/diligence-system/', link.getAttribute('data-continue-target') || '#foundation');
  });
  modal.addEventListener('click', function(e){
    var next=e.target.closest ? e.target.closest('[data-system-continue]') : null;
    if(next){
      var target=document.querySelector(next.getAttribute('data-target') || '#foundation');
      closeModal();
      if(target) target.scrollIntoView({behavior:'smooth',block:'start'});
      return;
    }
    if(e.target===modal) closeModal();
  });
  modal.addEventListener'''
text, gate_count = gate_pattern.subn(new_gate, text, count=1)
if gate_count != 1:
    raise SystemExit(f'Gate replacement failed: {gate_count}')
# Remove the duplicate old modal overlay listener introduced at the join boundary.
text = text.replace("  modal.addEventListener('click', function(e){ if(e.target===modal) closeModal(); });\n", '', 1)

# 5. Convert the existing hero system button into the small upstream CTA.
old_hero_cta = "          +'<a class=\"btn sec\" href=\"'+esc(sandbox.target || 'https://sandbox.lexnovahq.com/interface-diligence/diligence-system/')+'\" data-interface-os-gate=\"true\">'+esc(sandbox.label || 'Enter the diligence sandbox')+'</a>'"
new_hero_cta = "          +'<a class=\"btn sec\" href=\"'+esc(sandbox.target || 'https://sandbox.lexnovahq.com/interface-diligence/diligence-system/')+'\" data-upstream-system-cta=\"true\" data-continue-target=\"#foundation\">Open the diligence system</a>'"
if old_hero_cta not in text:
    raise SystemExit('Hero system CTA source missing')
text = text.replace(old_hero_cta, new_hero_cta, 1)

# 6. Add restrained upstream CTAs to Act I and Act II bridges.
old_act1_bridge = "+'<div id=\"act1-act2-bridge\" class=\"reveal act1-bridge\"><p>These dimensions identify the legally material parts. Act II shows how I use them to dismantle a complex commercial matter, test the consequences of its facts and reconstruct the result into one coherent legal architecture.</p><a href=\"#matrix\">Continue to Act II →</a></div>'"
new_act1_bridge = "+'<div id=\"act1-act2-bridge\" class=\"reveal act1-bridge\"><p>These dimensions identify the legally material parts. Act II shows how I use them to dismantle a complex commercial matter, test the consequences of its facts and reconstruct the result into one coherent legal architecture.</p><div class=\"journey-bridge-actions\"><a href=\"#matrix\">Continue to Act II →</a><a class=\"upstream-system-link\" data-upstream-system-cta=\"true\" data-continue-target=\"#matrix\" href=\"'+esc('" + LIVE_URL + "')+'\">Open the diligence system</a></div></div>'"
if old_act1_bridge not in text:
    raise SystemExit('Act I bridge source missing')
text = text.replace(old_act1_bridge, new_act1_bridge, 1)

old_act2_bridge = "+'<div id=\"act2-act3-bridge\" class=\"reveal act2-bridge\"><p>Once the legal architecture is defined, technology can support its execution without becoming the source of legal judgment.</p><a href=\"#tooling-layer\">See the legal architecture in operation →</a></div>'"
new_act2_bridge = "+'<div id=\"act2-act3-bridge\" class=\"reveal act2-bridge\"><p>Once the legal architecture is defined, technology can support its execution without becoming the source of legal judgment.</p><div class=\"journey-bridge-actions\"><a href=\"#delivery-system\">See the legal architecture in operation →</a><a class=\"upstream-system-link\" data-upstream-system-cta=\"true\" data-continue-target=\"#delivery-system\" href=\"'+esc('" + LIVE_URL + "')+'\">Open the diligence system</a></div></div>'"
if old_act2_bridge not in text:
    raise SystemExit('Act II bridge source missing')
text = text.replace(old_act2_bridge, new_act2_bridge, 1)

# 7. Absorb Capstone into Act III and replace the small gated CTA with the dominant direct launch.
old_act3_end = r'''        +'<section id="act3-interface-diligence-engine" class="reveal act3-supporting-system"><div><p class="eyebrow">Supporting system</p><h3>The diligence engine preserves the architecture.</h3><p>I built the diligence engine to preserve evidence, structure factual profiles, apply controlled legal tests and prepare review-ready handoffs. It demonstrates how legal architecture can operate at scale. It is not presented as a substitute for qualified legal judgment.</p></div><a id="sandbox-os" class="btn" data-interface-os-gate="true" href="'+esc(liveUrl)+'" target="_blank" rel="noopener">Open the live diligence system →</a></section>'
        +'<div class="reveal act3-capstone-bridge"><p>The lawyer authors the architecture. Technology preserves it through execution.</p><a href="#capstone">Continue to Capstone →</a></div>'
'''
new_act3_end = r'''        +'<section id="act3-synthesis" class="reveal act3-synthesis"><p class="eyebrow">Synthesis</p><h3>One legal method, expressed through technology.</h3><p class="act3-synthesis-intro">The portfolio is not a shift from law into software. It is one lawyer-first method carried from legal grammar, through matter architecture, into controlled execution.</p><div class="act3-synthesis-grid"><div class="act3-synthesis-item"><strong>Lawyer authors the architecture</strong><p>The legal questions, authority, trigger, exclusion, consequence and review boundary remain matters of legal judgment.</p></div><div class="act3-synthesis-item"><strong>Technology preserves the architecture</strong><p>The system maintains the evidence path, applies the controlled structure consistently and exposes missing or contradictory proof.</p></div><div class="act3-synthesis-item"><strong>Qualified review controls reliance</strong><p>The output becomes usable only through human verification, correction and jurisdiction-specific judgment.</p></div></div><p class="act3-synthesis-line">The lawyer determines the position. The system preserves how that position was reached.</p></section>'
        +'<section id="act3-interface-diligence-engine" class="reveal act3-launch"><div class="act3-launch-copy"><p class="eyebrow">Supporting system · live proof</p><h3>See the legal architecture operate.</h3><p>Run the public-safe diligence workflow and trace how source evidence becomes structured facts, controlled legal testing, qualified review and a review-ready handoff.</p></div><div class="act3-launch-proof"><span>Evidence attached</span><span>Uncertainty escalated</span><span>Human review retained</span></div><div class="act3-launch-action"><p class="act3-launch-boundary">Public, synthetic or scrubbed materials only. The system prepares review-ready legal work; it does not provide autonomous legal advice or replace qualified counsel.</p><a id="sandbox-os" class="act3-launch-btn" href="'+esc(liveUrl)+'" target="_blank" rel="noopener">Open the live diligence system →</a></div></section>'
'''
if old_act3_end not in text:
    raise SystemExit('Act III ending source missing')
text = text.replace(old_act3_end, new_act3_end, 1)

# Add an explicit anchor to the trace section for the live rail.
text = text.replace("        +'<section class=\"reveal act3-trace\">", "        +'<section id=\"act3-trace\" class=\"reveal act3-trace\">", 1)

# 8. Remove the standalone Capstone renderer and tighten the Close section index.
capstone_pattern = re.compile(r"\n  // ---------- CAPSTONE ----------[\s\S]*?\n  // ---------- CLOSE ----------")
text, cap_count = capstone_pattern.subn("\n  // ---------- CLOSE ----------", text, count=1)
if cap_count != 1:
    raise SystemExit(f'Capstone renderer removal failed: {cap_count}')
text = text.replace("<section id=\"contact\" class=\"act\" data-rail=\"5\">", "<section id=\"contact\" class=\"act\" data-rail=\"4\">", 1)

# 9. Remove Capstone from fallback navigation and update the map.
text = text.replace("      'workflow-automation-proof',\n      'capstone',\n      'contact'", "      'act3-synthesis',\n      'sandbox-os',\n      'contact'", 1)
text = text.replace("      'Shows that the same controlled workflow logic can be applied outside law.',\n      'Synthesizes the portfolio into one legal method across jurisdictions and systems.',\n      'Converts the proof into the hiring argument.'", "      'Shows the synthesis and review-ready handoff without losing the legal boundary.',\n      'Opens the public-safe diligence workflow as supporting proof.',\n      'Converts the proof into the hiring argument.'", 1)
text = text.replace("var navMap={hero:'#foundation',foundation:'#foundation',matrix:'#matrix','delivery-system':'#delivery-system',funnel:'#delivery-system',capstone:'#capstone',contact:'#contact'};", "var navMap={hero:'#foundation',foundation:'#foundation',matrix:'#matrix','delivery-system':'#delivery-system',funnel:'#delivery-system',contact:'#contact'};", 1)

# 10. Synchronize embedded and external rail data.
final_rail = {
    'chip': {'derived':'grammar → matter','structured':'matter → architecture','running':'architecture → workflow'},
    'nodes': [
        {'kind':'start','label':'Start','sub':'the thesis','target':'hero-thesis','why':'Establishes the claim: lawyer first, systems second.'},
        {'band':'ACT I · LEGAL GRAMMAR','band_tag':'how I determine what matters','node':'Legal Lenses','sub':'conduct → role → consequence','target':'doctrine-layer','why':'Shows the recurring legal questions used to identify what is materially relevant.'},
        {'band':'ACT I · LEGAL GRAMMAR','band_tag':'how I determine what matters','node':'Domain Vocabulary','sub':'behavior · lane · surface · terminal harm','target':'taxonomy-map','why':'Shows how the same legal grammar adapts without collapsing distinct domain vocabularies.'},
        {'band':'ACT II · APPLIED LEGAL ARCHITECTURE','band_tag':'the commercial matter','node':'Deconstruct','sub':'commercial reality → legal parts','target':'act2-threat-matrix','why':'Shows how one commercial proposition becomes separate activities, roles, flows, data, decisions and dependencies.'},
        {'band':'ACT II · APPLIED LEGAL ARCHITECTURE','band_tag':'the commercial matter','node':'Test & Reconstruct','sub':'duties → position → response','target':'act2-living-document','why':'Shows how material facts are tested and recombined into one coherent legal architecture.'},
        {'band':'ACT III · LEGAL ARCHITECTURE IN OPERATION','band_tag':'architecture preserved','node':'Evidence Path','sub':'source → structured fact','target':'project-walkthrough','why':'Shows how the system preserves source evidence and the factual structure authored by the lawyer.'},
        {'band':'ACT III · LEGAL ARCHITECTURE IN OPERATION','band_tag':'architecture preserved','node':'Legal Testing','sub':'controlled test → limitation','target':'act3-trace','why':'Shows one legal conclusion traced from source through controlled testing and evidence gaps.'},
        {'band':'ACT III · LEGAL ARCHITECTURE IN OPERATION','band_tag':'architecture preserved','node':'Qualified Review','sub':'uncertainty → human judgment','target':'prompt-agent-proof','why':'Shows that unsupported or private facts become review questions instead of automated conclusions.'},
        {'band':'ACT III · LEGAL ARCHITECTURE IN OPERATION','band_tag':'architecture preserved','node':'Handoff','sub':'position → review route','target':'act3-synthesis','why':'Shows the synthesis and review-ready route while preserving the lawyer’s boundary.'},
        {'band':'ACT III · LEGAL ARCHITECTURE IN OPERATION','band_tag':'architecture preserved','node':'Open System','sub':'live supporting proof','target':'sandbox-os','why':'Opens the public-safe diligence workflow after the legal method and architecture are understood.'},
        {'kind':'terminal','label':'Close','sub':'technology & data protection lawyer','target':'contact','why':'Converts the proof into the hiring argument.'}
    ]
}
embedded_pattern = re.compile(r'(<script id="content-data" type="application/json">)(.*?)(</script>)', re.S)
match = embedded_pattern.search(text)
if not match:
    raise SystemExit('Embedded content block missing')
embedded = json.loads(match.group(2))
embedded['rail'] = final_rail
# Normalize the upstream hero CTA label in source data too.
if embedded.get('hero',{}).get('ctas') and len(embedded['hero']['ctas']) > 1:
    embedded['hero']['ctas'][1]['label'] = 'Open the diligence system'
embedded_json = json.dumps(embedded, ensure_ascii=False, separators=(',',':'))
text = text[:match.start(2)] + embedded_json + text[match.end(2):]

content = json.loads(content_path.read_text(encoding='utf-8'))
content['rail'] = final_rail
if content.get('hero',{}).get('ctas') and len(content['hero']['ctas']) > 1:
    content['hero']['ctas'][1]['label'] = 'Open the diligence system'
content_path.write_text(json.dumps(content, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

index_path.write_text(text, encoding='utf-8')
print('Act III CTA hierarchy and integrated synthesis applied.')
