from pathlib import Path
import json
import re

ROOT = Path('.')
PAGES = [
    Path('index.html'),
    Path('legal-grammar.html'),
    Path('applied-legal-architecture.html'),
    Path('legal-architecture-in-operation.html'),
]
LINEAGE = 'Registry lineage: 81 → 98 AI-governance rows. A second FinTech registry now contains 46 routable rows under the same key structure.'
HEADLINE = 'A litigator making AI legal work defensible enough to deploy.'
DOCTRINE = 'Model suggests. Rules decide. Evidence locks. Conflicts block auto-lock.'

content_path = Path('content.json')
content = json.loads(content_path.read_text(encoding='utf-8'))

def clean_stale(node):
    if isinstance(node, dict):
        return {k: clean_stale(v) for k, v in node.items()}
    if isinstance(node, list):
        return [clean_stale(v) for v in node]
    if isinstance(node, str):
        value = node.replace('80-point', '98-row').replace('80 point', '98 row')
        if 'refined from 81' in value:
            return LINEAGE
        return value
    return node

content = clean_stale(content)
content.setdefault('hero', {})['headline'] = HEADLINE
content['registry_proof'] = {
    'title': 'Two registries. One key structure.',
    'eyebrow': 'CROSS-DOMAIN REGISTRY PROOF',
    'supporting_line': 'The vocabulary changes by domain. The derivation contract does not.',
    'intro': 'The AI-governance and FinTech packages use different legal vocabularies, but the same controlled derivation contract. Each activity is resolved through the same seven gates before a row-specific threat trigger can fire.',
    'ai_governance': {
        'label': 'AI Governance',
        'package_id': 'ai-governance',
        'key_file': 'AI_Registry_Key.yml',
        'key_version': 'v4.0',
        'routable_rows': 98,
        'behavior_classes': 14,
        'scope': 'AI product and deployment exposures'
    },
    'fintech': {
        'label': 'FinTech',
        'package_id': 'fintech',
        'key_file': 'FinTech_Registry_Key.yml',
        'key_version': 'v1.0',
        'routable_rows': 46,
        'behavior_classes': 14,
        'scope': 'Payments, lending, custody, digital assets and financial-regulatory exposures',
        'built_to_structure_of': 'AI_Registry_Key.yml'
    },
    'derivation_order': [
        'Behavior Class',
        'Lane',
        'Surface',
        'Subcategory / Terminal Harm',
        'Compliance Framework',
        'Severity',
        'Threat Trigger'
    ],
    'doctrine': DOCTRINE,
    'lineage': LINEAGE,
    'sample_rows': [
        {
            'threat_id': 'PAY_LIC_001',
            'threat_name': 'Unlicensed Money Transmission / Payment Aggregation',
            'classification': 'PAY · Lane A · Transaction-Data | Merchant-SME · Licensing / Authorisation Defect',
            'authority_route': 'RBI Payment Aggregator Directions 2025 · EU payment-institution authorisation / incoming PSD3-PSR · FinCEN MSB and state money-transmitter licensing',
            'trigger': 'Funds are collected, pooled or transmitted through the product without the required authorisation or a disclosed licensed sponsor structure.'
        },
        {
            'threat_id': 'XCHG_LIC_001',
            'threat_name': 'Unauthorised Crypto-Asset Service — CASP / VASP',
            'classification': 'XCHG · Lane A · Crypto-VirtualAsset | Cross-Border · Licensing / Authorisation Defect',
            'authority_route': 'FIU-IND registration · MiCA CASP authorisation · FinCEN MSB and applicable securities registration',
            'trigger': 'Exchange, custody, transfer or brokerage is offered in a market without the required registration, authorisation or effective geographic exclusion.'
        },
        {
            'threat_id': 'SCOR_CONS_001',
            'threat_name': 'Algorithmic Underwriting Bias / AI Credit-Model Governance',
            'classification': 'SCOR · Lane A · Credit-Data | Sensitive-Financial · Consumer Harm',
            'authority_route': 'RBI fair-practices and model-governance expectations · GDPR Article 22 and EU AI Act · ECOA / Regulation B and model-risk guidance',
            'trigger': 'A credit model lacks bias testing, validation, specific adverse-action reasons, human oversight or a contest route.'
        }
    ],
    'closing_line': 'Different vocabulary. Identical structure. Domain-specific authority. Review-bound output.'
}
content_path.write_text(json.dumps(content, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

json_script = re.compile(r'(<script id="content-data" type="application/json">)(.*?)(</script>)', re.S)
minified = json.dumps(content, ensure_ascii=False, separators=(',', ':'))

registry_builder = r'''
    var registryProof=C.registry_proof||{};
    var registryAi=registryProof.ai_governance||{};
    var registryFintech=registryProof.fintech||{};
    var registryDerivation=(registryProof.derivation_order||[]).map(function(step,i){return '<span class="registry-step">'+esc(step)+'</span>'+(i<(registryProof.derivation_order||[]).length-1?'<span class="registry-arrow" aria-hidden="true">→</span>':'');}).join('');
    var registrySamples=(registryProof.sample_rows||[]).map(function(row){return '<article class="registry-sample-row"><div class="registry-sample-id"><code>'+esc(row.threat_id||'')+'</code><h4>'+esc(row.threat_name||'')+'</h4></div><div class="registry-sample-field"><strong>Classification</strong><span>'+esc(row.classification||'')+'</span></div><div class="registry-sample-field"><strong>Authority route</strong><span>'+esc(row.authority_route||'')+'</span></div><div class="registry-sample-field"><strong>Compressed trigger</strong><span>'+esc(row.trigger||'')+'</span></div></article>';}).join('');
    var registryCode='registry_key:\n  name: '+(registryFintech.key_file||'FinTech_Registry_Key.yml').replace(/\.yml$/,'')+'\n  built_to_structure_of: '+(registryFintech.built_to_structure_of||'AI_Registry_Key.yml');
    var registryTransferHtml='<section id="registry-transfer" class="reveal registry-transfer" aria-labelledby="registry-transfer-title">'
      +'<header class="registry-transfer-head"><p class="eyebrow">'+esc(registryProof.eyebrow||'CROSS-DOMAIN REGISTRY PROOF')+'</p><h3 id="registry-transfer-title">'+esc(registryProof.title||'Two registries. One key structure.')+'</h3><p class="registry-transfer-support">'+esc(registryProof.supporting_line||'')+'</p><p>'+esc(registryProof.intro||'')+'</p></header>'
      +'<div class="registry-count-grid"><div><span>'+esc(registryAi.label||'AI Governance')+'</span><strong>'+esc(String(registryAi.routable_rows||98))+' routable rows</strong><small>Key '+esc(registryAi.key_version||'v4.0')+' · '+esc(String(registryAi.behavior_classes||14))+' Behavior Classes</small><p>'+esc(registryAi.scope||'')+'</p></div><div><span>'+esc(registryFintech.label||'FinTech')+'</span><strong>'+esc(String(registryFintech.routable_rows||46))+' routable rows</strong><small>Key '+esc(registryFintech.key_version||'v1.0')+' · '+esc(String(registryFintech.behavior_classes||14))+' Behavior Classes</small><p>'+esc(registryFintech.scope||'')+'</p></div></div>'
      +'<div class="registry-derivation"><strong>One derivation sequence</strong><div>'+registryDerivation+'</div></div>'
      +'<pre class="registry-code"><code>'+esc(registryCode)+'</code></pre>'
      +'<div class="registry-samples"><div class="registry-samples-head"><strong>Representative FinTech rows</strong><span>India · EU · US authority routes</span></div>'+registrySamples+'</div>'
      +'<p class="registry-lineage">'+esc(registryProof.lineage||'')+'</p><p class="registry-closing">'+esc(registryProof.closing_line||'')+'</p>'
      +'</section>';
'''

domain_button_needle = "    var domainButtons=Object.keys(demos).map(function(k,i){\n      return '<button class=\"act1-domain-tab'+(i===0?' active':'')+'\" type=\"button\" data-act1-domain=\"'+k+'\" aria-selected=\"'+(i===0?'true':'false')+'\">'+esc(demos[k].label)+'</button>';\n    }).join('');\n"
discipline_needle = "      +'<section class=\"reveal act1-disciplines\" aria-label=\"Governing disciplines\">'"
act3_live_needle = "    var liveUrl='https://sandbox.lexnovahq.com/interface-diligence/diligence-system/';\n"
act3_workflow_needle = "        +'<section id=\"project-walkthrough\" class=\"reveal act3-operation-shell\"><nav class=\"act3-operation-nav\" aria-label=\"Supporting workflow\">'+workflowButtons+'</nav><div id=\"act3-operation-panel\" class=\"act3-operation-panel\" aria-live=\"polite\"></div></section>'"

for page in PAGES:
    text = page.read_text(encoding='utf-8')
    text = json_script.sub(lambda m: m.group(1) + minified + m.group(3), text, count=1)

    if 'var registryTransferHtml=' not in text:
        if domain_button_needle not in text:
            raise SystemExit(f'{page}: Act I domain-button insertion point missing')
        text = text.replace(domain_button_needle, domain_button_needle + registry_builder, 1)
    if '+registryTransferHtml' not in text:
        if discipline_needle not in text:
            raise SystemExit(f'{page}: Act I disciplines insertion point missing')
        text = text.replace(discipline_needle, "      +registryTransferHtml\n" + discipline_needle, 1)

    if 'var operatingDoctrine=' not in text:
        if act3_live_needle not in text:
            raise SystemExit(f'{page}: Act III live-url insertion point missing')
        text = text.replace(act3_live_needle, act3_live_needle + "    var operatingDoctrine=((C.registry_proof||{}).doctrine)||'" + DOCTRINE + "';\n", 1)
    if 'id="operating-doctrine"' not in text:
        if act3_workflow_needle not in text:
            raise SystemExit(f'{page}: Act III workflow insertion point missing')
        doctrine_markup = "        +'<aside id=\"operating-doctrine\" class=\"reveal operating-doctrine\" aria-label=\"Operating doctrine\"><p class=\"eyebrow\">OPERATING DOCTRINE</p><p>'+esc(operatingDoctrine)+'</p></aside>'\n"
        text = text.replace(act3_workflow_needle, doctrine_markup + act3_workflow_needle, 1)

    page.write_text(text, encoding='utf-8')

portfolio = Path('portfolio.html')
if portfolio.exists():
    text = portfolio.read_text(encoding='utf-8')
    text = text.replace('80-point', '98-row').replace('80 point', '98 row')
    text = text.replace('refined from 81 through forensic-engine runs.', LINEAGE)
    text = text.replace('refined from 81', 'evolved from 81 → 98, with a second FinTech registry at 46')
    portfolio.write_text(text, encoding='utf-8')

js_path = Path('assets/editorial-multipage.js')
js = js_path.read_text(encoding='utf-8')
old = "act1:{title:'ACT I OF III',items:[['Legal Lenses','doctrine-layer'],['Domain Vocabulary','taxonomy-map'],['Governing Disciplines','act1-disciplines'],['Grammar Output','act1-output'],['Continue','act1-act2-bridge']]},"
new = "act1:{title:'ACT I OF III',items:[['Legal Lenses','doctrine-layer'],['Domain Vocabulary','taxonomy-map'],['Registry Transfer','registry-transfer'],['Governing Disciplines','act1-disciplines'],['Grammar Output','act1-output'],['Continue','act1-act2-bridge']]},"
if old not in js and "['Registry Transfer','registry-transfer']" not in js:
    raise SystemExit('assets/editorial-multipage.js: Act I rail contract not found')
js = js.replace(old, new, 1)
js_path.write_text(js, encoding='utf-8')

css_path = Path('assets/editorial-multipage-fixes.css')
css = css_path.read_text(encoding='utf-8')
marker = '/* Registry transfer and operating doctrine */'
if marker not in css:
    css += r'''

/* Registry transfer and operating doctrine */
.registry-transfer{margin-top:28px;padding:28px;border:1px solid var(--editorial-line);border-top:3px solid var(--editorial-oxblood);background:rgba(255,253,248,.78)}
.registry-transfer-head{max-width:850px}.registry-transfer-head h3{margin:5px 0 0;font-family:"Libre Caslon Display",Georgia,serif;font-size:clamp(1.65rem,2.5vw,2.25rem);line-height:1.08;font-weight:400;color:var(--editorial-ink)}
.registry-transfer-head>p:last-child{margin:12px 0 0;color:#4a4e51;font-size:.82rem;line-height:1.65}.registry-transfer-support{margin:8px 0 0!important;color:var(--editorial-oxblood)!important;font-size:.72rem!important;font-weight:700;letter-spacing:.04em}
.registry-count-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));margin-top:22px;border-top:1px solid var(--editorial-line);border-bottom:1px solid var(--editorial-line)}
.registry-count-grid>div{padding:18px 20px}.registry-count-grid>div+div{border-left:1px solid var(--editorial-line)}.registry-count-grid span{display:block;color:var(--editorial-oxblood);font-size:.62rem;font-weight:800;letter-spacing:.13em;text-transform:uppercase}.registry-count-grid strong{display:block;margin-top:5px;font-family:"Libre Caslon Display",Georgia,serif;font-size:1.45rem;font-weight:400;color:var(--editorial-ink)}.registry-count-grid small{display:block;margin-top:3px;color:#6b6e71;font-size:.66rem}.registry-count-grid p{margin:8px 0 0;color:#4a4e51;font-size:.74rem;line-height:1.5}
.registry-derivation{margin-top:20px}.registry-derivation>strong,.registry-samples-head strong{display:block;color:var(--editorial-oxblood);font-size:.62rem;letter-spacing:.12em;text-transform:uppercase}.registry-derivation>div{display:flex;align-items:center;flex-wrap:wrap;gap:8px;margin-top:10px}.registry-step{padding:7px 9px;border:1px solid var(--editorial-line);background:var(--editorial-white);color:var(--editorial-ink);font-size:.67rem;font-weight:700}.registry-arrow{color:var(--editorial-oxblood);font-size:.78rem}
.registry-code{margin:20px 0 0;padding:15px 17px;overflow:auto;border-left:3px solid var(--editorial-oxblood);background:#17191b;color:#f3d49a;font-size:.72rem;line-height:1.6}.registry-code code{font-family:"SFMono-Regular",Consolas,"Liberation Mono",monospace}
.registry-samples{margin-top:22px;border-top:1px solid var(--editorial-line)}.registry-samples-head{display:flex;justify-content:space-between;gap:18px;padding:13px 0}.registry-samples-head span{color:#6b6e71;font-size:.66rem}.registry-sample-row{display:grid;grid-template-columns:minmax(150px,.8fr) minmax(180px,1fr) minmax(220px,1.35fr) minmax(220px,1.35fr);border-top:1px solid var(--editorial-line)}.registry-sample-row>div{padding:14px 13px}.registry-sample-row>div+div{border-left:1px solid var(--editorial-line)}.registry-sample-id code{color:var(--editorial-oxblood);font-size:.65rem;font-weight:800}.registry-sample-id h4{margin:5px 0 0;color:var(--editorial-ink);font-size:.78rem;line-height:1.35}.registry-sample-field strong{display:block;color:var(--editorial-oxblood);font-size:.55rem;letter-spacing:.1em;text-transform:uppercase}.registry-sample-field span{display:block;margin-top:5px;color:#4a4e51;font-size:.69rem;line-height:1.5}.registry-lineage{margin:18px 0 0;padding-top:15px;border-top:1px solid var(--editorial-line);color:#4a4e51;font-size:.72rem;line-height:1.55}.registry-closing{margin:10px 0 0;padding-left:12px;border-left:2px solid var(--editorial-oxblood);font-family:"Libre Caslon Display",Georgia,serif;color:var(--editorial-ink);font-size:1.05rem;line-height:1.4}
.operating-doctrine{margin:20px 0 24px;padding:17px 20px;border:1px solid var(--editorial-line);border-left:3px solid var(--editorial-oxblood);background:rgba(255,253,248,.72)}.operating-doctrine .eyebrow{margin:0}.operating-doctrine>p:last-child{margin:7px 0 0;font-family:"Libre Caslon Display",Georgia,serif;color:var(--editorial-ink);font-size:clamp(1.15rem,2vw,1.5rem);line-height:1.35}
@media(max-width:980px){.registry-sample-row{grid-template-columns:1fr 1fr}.registry-sample-row>div:nth-child(3){border-left:0;border-top:1px solid var(--editorial-line)}.registry-sample-row>div:nth-child(4){border-top:1px solid var(--editorial-line)}}
@media(max-width:640px){.registry-transfer{padding:22px 17px}.registry-count-grid{grid-template-columns:1fr}.registry-count-grid>div+div{border-left:0;border-top:1px solid var(--editorial-line)}.registry-sample-row{grid-template-columns:1fr}.registry-sample-row>div+div{border-left:0;border-top:1px solid var(--editorial-line)}.registry-samples-head{align-items:flex-start;flex-direction:column;gap:4px}.registry-arrow{display:none}.registry-derivation>div{display:grid;grid-template-columns:1fr}.registry-step{width:100%}}
'''
css_path.write_text(css, encoding='utf-8')

validator = r'''import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const read = (p) => fs.readFileSync(path.join(root, p), "utf8");
const canonical = JSON.parse(read("content.json"));
const proof = canonical.registry_proof;
const headline = "A litigator making AI legal work defensible enough to deploy.";
const doctrine = "Model suggests. Rules decide. Evidence locks. Conflicts block auto-lock.";
const lineage = "Registry lineage: 81 → 98 AI-governance rows. A second FinTech registry now contains 46 routable rows under the same key structure.";

assert.ok(proof, "content.json registry_proof missing");
assert.equal(proof.ai_governance.routable_rows, 98);
assert.equal(proof.ai_governance.key_version, "v4.0");
assert.equal(proof.fintech.routable_rows, 46);
assert.equal(proof.fintech.key_version, "v1.0");
assert.equal(proof.fintech.built_to_structure_of, "AI_Registry_Key.yml");
assert.equal(proof.doctrine, doctrine);
assert.equal(proof.lineage, lineage);
assert.deepEqual(proof.derivation_order, ["Behavior Class","Lane","Surface","Subcategory / Terminal Harm","Compliance Framework","Severity","Threat Trigger"]);
assert.deepEqual(proof.sample_rows.map((r) => r.threat_id), ["PAY_LIC_001","XCHG_LIC_001","SCOR_CONS_001"]);
assert.equal(canonical.hero.headline, headline);
assert.match(canonical._meta.og_title, /Technology & Data Protection Lawyer/);

const pages = ["index.html","legal-grammar.html","applied-legal-architecture.html","legal-architecture-in-operation.html"];
for (const file of pages) {
  const source = read(file);
  const match = source.match(/<script id="content-data" type="application\/json">([\s\S]*?)<\/script>/);
  assert.ok(match, `${file}: embedded content-data missing`);
  const embedded = JSON.parse(match[1]);
  assert.deepEqual(embedded, canonical, `${file}: embedded content drift`);
  assert.ok(source.includes(headline), `${file}: canonical headline absent`);
  assert.ok(source.includes(doctrine), `${file}: doctrine absent`);
}

const grammar = read("legal-grammar.html");
assert.ok(grammar.includes('id="registry-transfer"'), "Act I registry-transfer anchor missing");
assert.ok(grammar.includes("Two registries. One key structure."), "Act I registry title missing");
assert.ok(grammar.includes("built_to_structure_of"), "Act I structural proof missing");
const operation = read("legal-architecture-in-operation.html");
assert.ok(operation.includes('id="operating-doctrine"'), "Act III operating-doctrine anchor missing");
assert.ok(read("assets/editorial-multipage.js").includes("['Registry Transfer','registry-transfer']"), "Act I rail item missing");
assert.ok(read("assets/editorial-multipage-fixes.css").includes(".registry-transfer"), "registry transfer styles missing");

const forbidden = [
  ["80", "-point"].join(""),
  ["80", " point"].join(""),
  ["refined", " from 81"].join(""),
  ["Shwet", "av Singh"].join(""),
  ["shwetav", ".alpna.singh@gmail.com"].join("")
];
const deadLabels = ["Watch walkthrough","Watch prompt-agent walkthrough","View scrubbed output sample","View automation build notes","Watch Category 2 demo"];
const textExtensions = new Set([".html",".json",".js",".css",".md",".txt",".yml",".yaml"]);
const skip = new Set([path.normalize("scripts/check-portfolio-content-contract.mjs")]);
const escapeRegExp = (value) => value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if ([".git","node_modules"].includes(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    else if (textExtensions.has(path.extname(entry.name)) && !skip.has(path.relative(root, full))) {
      const text = fs.readFileSync(full, "utf8");
      for (const token of forbidden) assert.ok(!text.includes(token), `${path.relative(root, full)}: forbidden stale token ${token}`);
      for (const label of deadLabels) assert.ok(!new RegExp(`href=["']#["'][^>]*>\\s*${escapeRegExp(label)}`, "is").test(text), `${path.relative(root, full)}: dead CTA ${label}`);
    }
  }
}
walk(root);
console.log(JSON.stringify({check:"portfolio content contract",status:"PASS",pages:pages.length,ai_rows:98,fintech_rows:46}, null, 2));
'''
Path('scripts/check-portfolio-content-contract.mjs').write_text(validator, encoding='utf-8')

permanent_workflow = '''name: Portfolio content contract

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - name: Validate portfolio content contract
        run: node scripts/check-portfolio-content-contract.mjs
'''
Path('.github/workflows/portfolio-content-contract.yml').write_text(permanent_workflow, encoding='utf-8')

for temp in [
    Path('.github/workflows/apply-registry-proof.yml'),
    Path('.github/workflows/apply-registry-proof-pr.yml'),
    Path('scripts/apply-registry-proof.py'),
    Path('REGISTRY_PROOF_APPLY_TRIGGER.md'),
]:
    if temp.exists():
        temp.unlink()
