from pathlib import Path
import json
import re

index_path = Path('index.html')
content_path = Path('content.json')
index = index_path.read_text(encoding='utf-8')

nav_replacements = {
    '<a class="nav-link" href="#foundation">Foundation</a>': '<a class="nav-link" href="#foundation">Legal Grammar</a>',
    '<a class="nav-link" href="#matrix">Diligence Architecture</a>': '<a class="nav-link" href="#matrix">Applied Architecture</a>',
    '<a class="nav-link" href="#delivery-system">Runtime Workflow</a>': '<a class="nav-link" href="#delivery-system">Supporting Workflow</a>'
}
for old, new in nav_replacements.items():
    if old not in index:
        raise SystemExit(f'Navigation source missing: {old}')
    index = index.replace(old, new, 1)

new_rail = {
    'chip': {
        'derived': 'grammar → matter',
        'structured': 'matter → architecture',
        'running': 'architecture → workflow'
    },
    'nodes': [
        {
            'kind': 'start',
            'label': 'Start',
            'sub': 'the thesis',
            'target': 'hero-thesis',
            'why': 'Establishes the claim: lawyer first, systems second.'
        },
        {
            'band': 'ACT I · LEGAL GRAMMAR',
            'band_tag': 'how I determine what matters',
            'node': 'Legal Lenses',
            'sub': 'conduct → role → consequence',
            'target': 'doctrine-layer',
            'why': 'Shows the recurring legal questions used to identify what is materially relevant.'
        },
        {
            'band': 'ACT I · LEGAL GRAMMAR',
            'band_tag': 'how I determine what matters',
            'node': 'Domain Vocabulary',
            'sub': 'behavior · lane · surface · harm',
            'target': 'taxonomy-map',
            'why': 'Shows how the same legal grammar adapts without collapsing distinct domain vocabularies.'
        },
        {
            'band': 'ACT II · APPLIED LEGAL ARCHITECTURE',
            'band_tag': 'the commercial matter',
            'node': 'Deconstruct',
            'sub': 'commercial reality → legal parts',
            'target': 'act2-threat-matrix',
            'why': 'Shows how one commercial proposition becomes separate activities, roles, flows, data, decisions and dependencies.'
        },
        {
            'band': 'ACT II · APPLIED LEGAL ARCHITECTURE',
            'band_tag': 'the commercial matter',
            'node': 'Test & Reconstruct',
            'sub': 'duties → position → response',
            'target': 'act2-living-document',
            'why': 'Shows how material facts are tested and recombined into one coherent legal architecture.'
        },
        {
            'band': 'ACT III · SUPPORTING WORKFLOW',
            'band_tag': 'architecture in operation',
            'node': 'Evidence Path',
            'sub': 'sources → factual profiles',
            'target': 'project-walkthrough',
            'why': 'Shows how the engine preserves the evidence and factual structure defined by the lawyer.'
        },
        {
            'band': 'ACT III · SUPPORTING WORKFLOW',
            'band_tag': 'architecture in operation',
            'node': 'Live System',
            'sub': 'structured testing → report',
            'target': 'sandbox-os',
            'why': 'Shows the public-safe workflow applying the architecture without originating legal judgment.'
        },
        {
            'band': 'ACT III · SUPPORTING WORKFLOW',
            'band_tag': 'architecture in operation',
            'node': 'Review Controls',
            'sub': 'boundaries · evidence · escalation',
            'target': 'prompt-agent-proof',
            'why': 'Shows the controls that prevent unsupported conclusions and preserve qualified review.'
        },
        {
            'band': 'ACT III · SUPPORTING WORKFLOW',
            'band_tag': 'architecture in operation',
            'node': 'Handoff',
            'sub': 'review → assembly route',
            'target': 'workflow-automation-proof',
            'why': 'Shows how reviewed findings move forward without losing their source, limitation or counsel route.'
        },
        {
            'band': 'CAPSTONE',
            'band_tag': 'the method',
            'node': 'Synthesis',
            'sub': 'lawyer → architecture → system',
            'target': 'capstone',
            'why': 'Synthesizes the portfolio into one lawyer-first Law × Technology method.'
        },
        {
            'kind': 'terminal',
            'label': 'Close',
            'sub': 'technology & data protection lawyer',
            'target': 'contact',
            'why': 'Converts the proof into the hiring argument.'
        }
    ]
}

pattern = re.compile(r'(<script id="content-data" type="application/json">)(.*?)(</script>)', re.S)
match = pattern.search(index)
if not match:
    raise SystemExit('Embedded content-data block not found')
embedded = json.loads(match.group(2))
embedded['rail'] = new_rail
embedded_json = json.dumps(embedded, ensure_ascii=False, separators=(',', ':'))
index = index[:match.start(2)] + embedded_json + index[match.end(2):]
index_path.write_text(index, encoding='utf-8')

content = json.loads(content_path.read_text(encoding='utf-8'))
content['rail'] = new_rail
content_path.write_text(json.dumps(content, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Navigation and rail synchronized.')
