from pathlib import Path
import re

ROOT = Path('.')
SOURCE = ROOT / 'index.html'
source = SOURCE.read_text(encoding='utf-8')

if 'editorial-multipage.css' in source:
    raise SystemExit('The current index already contains the multi-page build marker.')

# The only approved content correction in this surgery.
source = source.replace(
    '<strong>Practice focus</strong><span>Technology, data protection, AI governance and commercial contracts.</span>',
    '<strong>Practice focus</strong><span>High Court litigation · technology · data protection · AI governance · commercial contracts.</span>',
    1,
)

# Preserve the existing disclaimer modal while allowing its Continue Reading button
# to move between the newly separated pages.
old_continue = """      var target=document.querySelector(next.getAttribute('data-target') || '#foundation');
      closeModal();
      if(target) target.scrollIntoView({behavior:'smooth',block:'start'});
      return;"""
new_continue = """      var destination=next.getAttribute('data-target') || '#foundation';
      closeModal();
      if(destination.charAt(0)==='#'){
        var target=document.querySelector(destination);
        if(target) target.scrollIntoView({behavior:'smooth',block:'start'});
      } else {
        window.location.href=destination;
      }
      return;"""
if old_continue not in source:
    raise SystemExit('Existing disclaimer continue handler was not found.')
source = source.replace(old_continue, new_continue, 1)

font_link = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Libre+Caslon+Display&display=swap" rel="stylesheet"><link rel="stylesheet" href="assets/editorial-multipage.css">'
if '</head>' not in source:
    raise SystemExit('Head closing tag missing.')
source = source.replace('</head>', font_link + '\n</head>', 1)
if '</body>' not in source:
    raise SystemExit('Body closing tag missing.')
source = source.replace('</body>', '<script src="assets/editorial-multipage.js"></script>\n</body>', 1)

header_pattern = re.compile(r'<header class="topnav"[\s\S]*?</header>', re.M)
if not header_pattern.search(source):
    raise SystemExit('Current header was not found.')

PAGES = {
    'home': {
        'file': 'index.html',
        'title': 'The Interface — Shwetav Singh',
        'continue': 'legal-grammar.html',
    },
    'act1': {
        'file': 'legal-grammar.html',
        'title': 'Legal Grammar — The Interface',
        'continue': 'applied-legal-architecture.html',
    },
    'act2': {
        'file': 'applied-legal-architecture.html',
        'title': 'Applied Legal Architecture — The Interface',
        'continue': 'legal-architecture-in-operation.html',
    },
    'act3': {
        'file': 'legal-architecture-in-operation.html',
        'title': 'Legal Architecture in Operation — The Interface',
        'continue': '#project-walkthrough',
    },
}

NAV = [
    ('home', 'Home', 'index.html'),
    ('act1', 'Legal Grammar', 'legal-grammar.html'),
    ('act2', 'Applied Architecture', 'applied-legal-architecture.html'),
    ('act3', 'Architecture in Operation', 'legal-architecture-in-operation.html'),
]


def header_for(page_key: str, continue_target: str) -> str:
    links = []
    for key, label, href in NAV:
        active = ' active' if key == page_key else ''
        current = ' aria-current="page"' if key == page_key else ''
        links.append(f'<a class="editorial-nav-link{active}" href="{href}"{current}>{label}</a>')
    links.append('<a class="editorial-nav-link" href="legal-architecture-in-operation.html#contact">Contact</a>')
    links.append(
        '<a class="editorial-header-cta" data-upstream-system-cta="true" '
        f'data-continue-target="{continue_target}" '
        'href="https://sandbox.lexnovahq.com/interface-diligence/diligence-system/">Open Diligence System</a>'
    )
    return (
        '<header class="topnav editorial-header" role="banner">'
        '<div class="editorial-header-inner">'
        '<a href="index.html" class="wordmark editorial-wordmark" aria-label="The Interface portfolio home">'
        '<span class="wordmark-title">The Interface</span>'
        '<span class="wordmark-subtitle">Law × Technology · AI Governance · Privacy · Systems</span>'
        '</a>'
        '<button class="editorial-menu-toggle" type="button" aria-expanded="false" aria-controls="editorial-nav">Menu</button>'
        '<nav id="editorial-nav" class="editorial-nav" aria-label="Primary">' + ''.join(links) + '</nav>'
        '</div></header>'
    )


def build_page(page_key: str, cfg: dict) -> str:
    html = source
    html = header_pattern.sub(header_for(page_key, cfg['continue']), html, count=1)
    html = re.sub(r'<title>[\s\S]*?</title>', f'<title>{cfg["title"]}</title>', html, count=1)
    html = html.replace('<body>', f'<body data-page="{page_key}">', 1)
    if '<body data-page=' not in html:
        raise SystemExit(f'Body marker failed for {page_key}.')
    return html

for page_key, cfg in PAGES.items():
    (ROOT / cfg['file']).write_text(build_page(page_key, cfg), encoding='utf-8')

assets = ROOT / 'assets'
assets.mkdir(exist_ok=True)

css = r'''
:root{
  --editorial-ink:#151719;
  --editorial-muted:#64686c;
  --editorial-paper:#f5f1e8;
  --editorial-paper-2:#ebe4d7;
  --editorial-white:#fffdf8;
  --editorial-line:#d3cab9;
  --editorial-oxblood:#6d2028;
  --editorial-oxblood-dark:#45141a;
  --editorial-brass:#9b7436;
  --editorial-charcoal:#17191b;
  --editorial-shadow:0 20px 70px rgba(32,29,24,.10);
  --gold:var(--editorial-brass);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:88px}
body{margin:0;background:radial-gradient(circle at 12% 4%,rgba(155,116,54,.10),transparent 28rem),linear-gradient(180deg,#f8f5ee 0%,var(--editorial-paper) 45%,#eee8dc 100%)!important;color:var(--editorial-ink)!important;font-family:"DM Sans",Arial,sans-serif!important;line-height:1.58}
body::before{opacity:.12!important;filter:sepia(.55)}
a{color:inherit}.font-display,.section-title,.hero-name,.hero-hook{font-family:"Libre Caslon Display",Georgia,serif!important}.gold{color:var(--editorial-oxblood)!important}
.progress-line{background:var(--editorial-oxblood)!important;height:2px!important}
.editorial-header{position:sticky!important;top:0;z-index:70!important;border-bottom:1px solid rgba(75,67,56,.18)!important;background:rgba(248,245,238,.94)!important;backdrop-filter:blur(18px)!important;color:var(--editorial-ink)!important}
.editorial-header-inner{width:min(1180px,calc(100% - 40px));min-height:70px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:24px}
.editorial-wordmark{text-decoration:none!important;display:inline-flex!important;flex-direction:column!important;line-height:1.06!important;min-width:250px}
.editorial-wordmark .wordmark-title{font-family:"Libre Caslon Display",Georgia,serif!important;font-size:1.35rem!important;font-weight:400!important;color:var(--editorial-ink)!important;letter-spacing:0!important}
.editorial-wordmark .wordmark-subtitle{margin-top:4px!important;color:var(--editorial-muted)!important;font-size:.62rem!important;letter-spacing:.12em!important;text-transform:uppercase!important}
.editorial-nav{display:flex;align-items:center;justify-content:flex-end;gap:18px}
.editorial-nav-link{position:relative;color:#4d5053!important;font-size:.72rem!important;font-weight:600!important;text-decoration:none!important;white-space:nowrap}
.editorial-nav-link:hover,.editorial-nav-link:focus,.editorial-nav-link.active{color:var(--editorial-oxblood)!important;outline:none}
.editorial-nav-link.active::after{content:"";position:absolute;left:0;right:0;bottom:-8px;height:1px;background:var(--editorial-oxblood)}
.editorial-header-cta{display:inline-flex;align-items:center;justify-content:center;min-height:40px;padding:10px 14px;border:1px solid var(--editorial-oxblood);border-radius:2px;background:var(--editorial-oxblood);color:#fff!important;font-size:.66rem;font-weight:700;letter-spacing:.055em;text-decoration:none;text-transform:uppercase;white-space:nowrap}
.editorial-header-cta:hover,.editorial-header-cta:focus{background:var(--editorial-oxblood-dark);outline:none}
.editorial-menu-toggle{display:none;border:1px solid var(--editorial-line);background:transparent;color:var(--editorial-oxblood);padding:8px 11px;font-size:.68rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.mobile-funnel{display:none!important}
.page-shell{width:min(1180px,calc(100% - 40px))!important;max-width:none!important;padding-left:0!important;padding-right:0!important}
.main-grid{display:grid!important;grid-template-columns:190px minmax(0,1fr)!important;gap:38px!important;align-items:start!important}
body[data-page="home"] .main-grid{grid-template-columns:minmax(0,1fr)!important}
body[data-page="home"] .rail-wrap{display:none!important}
.rail-wrap{position:relative!important;width:auto!important;min-width:0!important}
.rail{position:sticky!important;top:96px!important;max-height:calc(100vh - 120px);overflow:auto;padding:8px 0 24px!important;border:0!important;background:transparent!important}
.local-rail-title{display:block;margin-bottom:12px;color:var(--editorial-oxblood);font-size:.62rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase}
.local-rail-link{display:block;padding:10px 0;border-top:1px solid var(--editorial-line);color:var(--editorial-muted);font-size:.7rem;font-weight:600;line-height:1.35;text-decoration:none}
.local-rail-link:last-child{border-bottom:1px solid var(--editorial-line)}
.local-rail-link:hover,.local-rail-link.active{color:var(--editorial-oxblood)}
#main>section{display:none!important}
body[data-page="home"] #main>#hero,body[data-page="home"] #main>#proof-architecture{display:block!important}
body[data-page="act1"] #main>#foundation{display:block!important}
body[data-page="act2"] #main>#matrix{display:block!important}
body[data-page="act3"] #main>#delivery-system,body[data-page="act3"] #main>#contact{display:block!important}
.act{min-height:auto!important;padding:62px 0!important;scroll-margin-top:92px!important}
.card-shell{padding:0!important;border:0!important;border-radius:0!important;background:transparent!important;box-shadow:none!important;color:var(--editorial-ink)!important}
.eyebrow{margin:0 0 10px!important;color:var(--editorial-oxblood)!important;font-size:.68rem!important;font-weight:700!important;letter-spacing:.15em!important;text-transform:uppercase!important}
.section-title{max-width:860px!important;margin:0!important;color:var(--editorial-ink)!important;font-size:clamp(2.15rem,4.3vw,3.65rem)!important;font-weight:400!important;line-height:1!important;letter-spacing:-.025em!important}
.hero-grid{grid-template-columns:minmax(0,1.18fr) minmax(300px,.82fr)!important;gap:48px!important;align-items:end!important}
.hero-name{color:var(--editorial-ink)!important;font-size:clamp(2.9rem,5.7vw,4.8rem)!important;line-height:.94!important;font-weight:400!important;letter-spacing:-.035em!important}
.hero-identity{color:var(--editorial-oxblood)!important;font-weight:700!important;letter-spacing:.035em!important}
.hero-hook{max-width:760px!important;color:var(--editorial-ink)!important;font-size:clamp(1.8rem,3.2vw,2.7rem)!important;line-height:1.04!important;font-weight:400!important}
.hero-builder,.hero-foundation{color:#414549!important;max-width:780px!important;font-size:.92rem!important;line-height:1.68!important}.hero-thesis{color:var(--editorial-oxblood)!important;font-size:1.15rem!important;line-height:1.45!important}
.surface,.hero-brief,.hero-credential{border:1px solid var(--editorial-line)!important;border-radius:2px!important;background:var(--editorial-white)!important;box-shadow:var(--editorial-shadow)!important;color:var(--editorial-ink)!important}
.hero-brief{border-top:3px solid var(--editorial-oxblood)!important;padding:26px!important}.hero-brief h3{font-family:"Libre Caslon Display",Georgia,serif!important;color:var(--editorial-ink)!important;font-size:1.65rem!important;font-weight:400!important}.hero-brief-row{border-color:var(--editorial-line)!important}.hero-brief-row strong{color:var(--editorial-oxblood)!important}.hero-brief-row span{color:#34383b!important}.hero-credential{box-shadow:none!important;border-left:2px solid var(--editorial-oxblood)!important;color:#34383b!important}
.hairline{background:linear-gradient(90deg,var(--editorial-oxblood),var(--editorial-line),transparent)!important}
.btn{border:1px solid var(--editorial-oxblood)!important;border-radius:2px!important;background:var(--editorial-oxblood)!important;color:#fff!important;box-shadow:none!important;font-size:.68rem!important;font-weight:700!important;letter-spacing:.06em!important;text-transform:uppercase!important}
.btn.sec{background:transparent!important;color:var(--editorial-oxblood)!important}.btn:hover,.btn:focus{transform:translateY(-1px);background:var(--editorial-oxblood-dark)!important;color:#fff!important}.btn.sec:hover,.btn.sec:focus{background:rgba(109,32,40,.06)!important;color:var(--editorial-oxblood)!important}
#proof-architecture{padding-top:34px!important}.legal-method-intro,.hero-method-note{color:#4a4e51!important}.legal-method-chain,.regulatory-signal-strip,.hero-method-cta{border-color:var(--editorial-line)!important}.regulatory-signal-strip{background:rgba(255,253,248,.7)!important}.regulatory-signal-strip strong,.regulatory-signal-strip .loop{color:var(--editorial-oxblood)!important}
.act1-opening-copy,.act1-domain-head p,.act1-domain-context,.act1-domain-note,.act1-discipline span,.act1-output-head p,.act1-bridge p{color:#4a4e51!important}.act1-method-shell,.act1-domain,.act1-disciplines,.act1-output,.act1-bridge,.act1-domain-compare,.act1-application{border-color:var(--editorial-line)!important}.act1-method-step,.act1-domain-tab{color:#6b6e71!important}.act1-method-step:hover,.act1-method-step:focus,.act1-method-step.active,.act1-domain-tab:hover,.act1-domain-tab:focus,.act1-domain-tab.active{color:var(--editorial-oxblood)!important;background:rgba(109,32,40,.035)!important}.act1-method-step.active::after,.act1-domain-tab.active::after{background:var(--editorial-oxblood)!important;box-shadow:none!important}.act1-stage-count,.act1-stage-block strong,.act1-domain-row .lens,.act1-domain-note strong,.act1-application strong{color:var(--editorial-oxblood)!important}.act1-stage-id h3,.act1-domain-head h3,.act1-discipline strong{color:var(--editorial-ink)!important}.act1-stage-block p,.act1-domain-cell span,.act1-application span{color:#4a4e51!important}.act1-domain-cell strong{color:var(--editorial-ink)!important}.act1-discipline{grid-template-columns:220px 1fr!important}.act1-discipline strong{padding-left:12px;border-left:3px solid var(--editorial-oxblood)}.act1-bridge a{color:var(--editorial-oxblood)!important;border-color:rgba(109,32,40,.42)!important}
body[data-page="act2"] #matrix{padding-top:48px!important}.act2-matter{padding:34px!important;background:var(--editorial-charcoal)!important;color:#f3eee5!important;box-shadow:0 28px 90px rgba(0,0,0,.18)!important}.act2-matter .eyebrow{color:#d9b77a!important}.act2-opening .section-title,.act2-movement-head h3,.act2-brief-title,.act2-brief-question p,.act2-thread-summary,.act2-reconstruction-note,.act2-bridge p{color:#f3eee5!important}.act2-opening-copy,.act2-brief-copy,.act2-movement-head p,.act2-output p,.act2-boundary-block p,.act2-component span,.act2-test-row span,.act2-architecture-col p{color:#bbb6af!important}.act2-matter-brief,.act2-movement-shell,.act2-output,.act2-boundary,.act2-bridge,.act2-component-grid,.act2-test-grid,.act2-architecture{border-color:#3a3c3e!important}.act2-movement-tab,.act2-thread-tab{color:#aaa69f!important}.act2-movement-tab:hover,.act2-movement-tab:focus,.act2-movement-tab.active,.act2-thread-tab:hover,.act2-thread-tab:focus,.act2-thread-tab.active{color:#d9b77a!important;background:rgba(217,183,122,.035)!important}.act2-movement-tab.active::after,.act2-thread-tab.active::after{background:#d9b77a!important;box-shadow:none!important}.act2-component,.act2-test-row,.act2-architecture-col{border-color:#3a3c3e!important;background:#202326!important}.act2-component strong,.act2-test-row strong,.act2-architecture-col strong,.act2-boundary-block strong,.act2-brief-kicker{color:#d9b77a!important}.act2-output-strip{color:#ddd8d1!important}.act2-bridge a{color:#d9b77a!important;border-color:rgba(217,183,122,.5)!important}
.act3-opening-copy,.act3-trace-head p,.act3-trace-row span,.act3-control-line span,.act3-synthesis-intro,.act3-synthesis-item p{color:#4a4e51!important}.act3-operation-shell{padding:24px!important;border:1px solid #35383a!important;background:var(--editorial-charcoal)!important}.act3-operation-step{color:#aaa69f!important;border-color:#35383a!important}.act3-operation-step:hover,.act3-operation-step:focus,.act3-operation-step.active{color:#d9b77a!important;background:rgba(217,183,122,.035)!important}.act3-operation-step.active::after{background:#d9b77a!important;box-shadow:none!important}.act3-operation-id span,.act3-operation-block strong{color:#d9b77a!important}.act3-operation-id h3{color:#f3eee5!important}.act3-operation-block{border-color:#4a4740!important}.act3-operation-block p{color:#cbc7c1!important}.act3-trace,.act3-controls,.act3-synthesis{border-color:var(--editorial-line)!important}.act3-trace-head h3,.act3-control-line strong,.act3-synthesis h3{color:var(--editorial-ink)!important}.act3-trace-tab{color:#6b6e71!important}.act3-trace-tab:hover,.act3-trace-tab:focus,.act3-trace-tab.active{color:var(--editorial-oxblood)!important}.act3-trace-tab.active::after{background:var(--editorial-oxblood)!important;box-shadow:none!important}.act3-trace-panel,.act3-trace-row,.act3-control-line{border-color:var(--editorial-line)!important}.act3-trace-row strong,.act3-synthesis-item strong{color:var(--editorial-oxblood)!important}.act3-regulatory-loop{border-color:rgba(109,32,40,.28)!important;border-left-color:var(--editorial-oxblood)!important;background:rgba(255,253,248,.72)!important}.act3-regulatory-loop .loop,.act3-regulatory-loop strong{color:var(--editorial-oxblood)!important}.act3-regulatory-loop p{color:#4a4e51!important}.act3-synthesis-grid{border-color:var(--editorial-line)!important}.act3-synthesis-item{border-color:var(--editorial-line)!important}.act3-synthesis-line{color:var(--editorial-ink)!important;border-left-color:var(--editorial-oxblood)!important}.act3-launch{border-color:rgba(109,32,40,.55)!important;background:linear-gradient(135deg,var(--editorial-oxblood-dark),var(--editorial-oxblood) 62%,#7e3b42)!important;box-shadow:0 22px 60px rgba(69,20,26,.22)!important}.act3-launch::before{background:radial-gradient(circle,rgba(243,212,154,.18),transparent 70%)!important}.act3-launch .eyebrow{color:#f3d49a!important}.act3-launch h3{color:#fff8ee!important;font-size:clamp(1.9rem,3.5vw,2.9rem)!important}.act3-launch p,.act3-launch-boundary{color:#ead9d9!important}.act3-launch-proof{color:#f4e7d7!important}.act3-launch-btn{background:#f3d49a!important;color:var(--editorial-oxblood-dark)!important;border-color:#f3d49a!important}
#contact{margin-top:18px!important;padding:54px 0 68px!important;background:var(--editorial-oxblood-dark)!important;color:#fff7ee!important;position:relative;left:50%;right:50%;width:100vw;margin-left:-50vw;margin-right:-50vw}#contact>.card-shell{width:min(1180px,calc(100% - 40px));margin:0 auto;color:#fff7ee!important}#contact .eyebrow{color:#f3d49a!important}#contact h2,#contact h3,#contact strong{color:#fff7ee!important}#contact p,#contact span{color:#e2cfd0!important}#contact .terminal-safety{color:#cfaeb1!important}#contact .terminal-genuine{color:#fff7ee!important}.contact-ico{border-color:rgba(243,212,154,.35)!important;color:#f3d49a!important}
.page-transition{margin:18px 0 72px;padding:28px;border:1px solid var(--editorial-line);border-top:3px solid var(--editorial-oxblood);background:var(--editorial-white);box-shadow:var(--editorial-shadow)}.page-transition h2{max-width:760px;margin:0;font-family:"Libre Caslon Display",Georgia,serif;font-size:clamp(1.75rem,3vw,2.55rem);line-height:1.03;font-weight:400}.page-transition p{max-width:780px;margin:14px 0 0;color:#4a4e51;font-size:.86rem;line-height:1.65}.page-transition-actions{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-top:20px}.page-return-link{color:var(--editorial-oxblood);font-size:.7rem;font-weight:700;text-decoration:none}.journey-bridge-actions{gap:12px!important}.upstream-system-link{color:var(--editorial-oxblood)!important}
.modal{background:rgba(21,23,25,.68)!important}.modal-card{border:1px solid var(--editorial-line)!important;border-radius:3px!important;background:var(--editorial-white)!important;color:var(--editorial-ink)!important;box-shadow:0 28px 90px rgba(0,0,0,.28)!important}.modal-card h3{font-family:"Libre Caslon Display",Georgia,serif!important;color:var(--editorial-ink)!important}.modal-card p,.os-gate-map span{color:#4a4e51!important}.os-gate-map,.os-gate-map div{border-color:var(--editorial-line)!important}.os-gate-map strong{color:var(--editorial-oxblood)!important}.modal-close{color:var(--editorial-oxblood)!important}
footer{margin-top:0!important;padding:24px 0!important;border:0!important;background:#111315!important;color:#a9aaab!important}.editorial-footer{width:min(1180px,calc(100% - 40px));margin:0 auto;display:flex;justify-content:space-between;gap:24px;align-items:flex-end}.editorial-footer-brand strong{display:block;font-family:"Libre Caslon Display",Georgia,serif;color:#fff7ee;font-size:1.15rem;font-weight:400}.editorial-footer-brand span{display:block;margin-top:4px;font-size:.62rem;letter-spacing:.1em;text-transform:uppercase}.editorial-footer-links{display:flex;gap:16px;align-items:center;flex-wrap:wrap;justify-content:flex-end;font-size:.7rem}.editorial-footer-links a{color:#d2cbc3;text-decoration:none}.editorial-footer-note{width:100%;margin-top:10px;color:#818385;font-size:.65rem;text-align:right}
@media(max-width:1040px){.editorial-nav{gap:12px}.editorial-nav-link{font-size:.66rem!important}.editorial-header-cta{padding:9px 10px}.main-grid{grid-template-columns:160px minmax(0,1fr)!important;gap:24px!important}}
@media(max-width:860px){.editorial-header-inner{width:min(100% - 24px,1180px);min-height:64px}.editorial-menu-toggle{display:block}.editorial-nav{display:none;position:absolute;left:12px;right:12px;top:64px;padding:14px;border:1px solid var(--editorial-line);background:var(--editorial-white);box-shadow:var(--editorial-shadow);flex-direction:column;align-items:stretch}.editorial-nav.open{display:flex}.editorial-nav-link,.editorial-header-cta{text-align:left;justify-content:flex-start;padding:10px}.editorial-nav-link.active::after{display:none}.page-shell{width:min(100% - 24px,1180px)!important}.main-grid{grid-template-columns:1fr!important;gap:0!important}.rail-wrap{position:sticky!important;top:64px!important;z-index:40!important;background:rgba(248,245,238,.96)!important;border-bottom:1px solid var(--editorial-line)!important;margin:0 0 20px!important}.rail{position:static!important;display:flex!important;align-items:center!important;gap:18px!important;overflow-x:auto!important;max-height:none!important;padding:10px 0!important}.local-rail-title{flex:0 0 auto;margin:0}.local-rail-link{flex:0 0 auto;border:0!important;padding:4px 0;white-space:nowrap}.act{padding:48px 0!important}.hero-grid{grid-template-columns:1fr!important}.hero-brief{margin-top:10px}.act1-stage-panel{grid-template-columns:1fr!important}.act1-stage-id{border-right:0!important;border-bottom:1px solid var(--editorial-line)!important}.act1-stage-block:last-child{grid-column:auto!important}}
@media(max-width:640px){.editorial-wordmark{min-width:0}.editorial-wordmark .wordmark-title{font-size:1.15rem!important}.editorial-wordmark .wordmark-subtitle{font-size:.52rem!important;letter-spacing:.08em!important}.section-title{font-size:clamp(2rem,10vw,2.8rem)!important}.hero-name{font-size:clamp(2.7rem,14vw,3.8rem)!important}.hero-hook{font-size:clamp(1.65rem,8vw,2.2rem)!important}.act2-matter{padding:22px 16px!important}.act3-operation-shell{padding:16px!important}.page-transition{padding:22px 18px}.page-transition-actions{align-items:flex-start;flex-direction:column}.editorial-footer{align-items:flex-start;flex-direction:column}.editorial-footer-links{justify-content:flex-start}.editorial-footer-note{text-align:left}.act1-discipline{grid-template-columns:1fr!important}.act3-launch{padding:1.2rem 1rem!important}.act3-launch-action{align-items:flex-start!important;flex-direction:column!important}.act3-launch-btn{width:100%!important}}
'''

js = r'''
(function(){
  var page=document.body.getAttribute('data-page')||'home';
  var liveUrl='https://sandbox.lexnovahq.com/interface-diligence/diligence-system/';
  var configs={
    act1:{title:'ACT I OF III',items:[['Legal Lenses','doctrine-layer'],['Domain Vocabulary','taxonomy-map'],['Governing Disciplines','act1-disciplines'],['Grammar Output','act1-output'],['Continue','act1-act2-bridge']]},
    act2:{title:'ACT II OF III',items:[['AsterPay Matter','act2-orientation'],['Matter Analysis','act2-movement-shell'],['Architecture Output','act2-output'],['Lawyer / System Boundary','act2-boundary'],['Continue','act2-act3-bridge']]},
    act3:{title:'ACT III OF III',items:[['Supporting Workflow','project-walkthrough'],['Trace a Conclusion','act3-trace'],['Review Controls','prompt-agent-proof'],['Regulatory Loop','workflow-automation-proof'],['Synthesis','act3-synthesis'],['Open System','sandbox-os'],['Terminal','contact']]}
  };
  var idMap={
    '.act1-disciplines':'act1-disciplines','.act1-output':'act1-output',
    '.act2-movement-shell':'act2-movement-shell','.act2-output':'act2-output','.act2-boundary':'act2-boundary',
    '.act3-trace':'act3-trace'
  };
  function assignIds(){Object.keys(idMap).forEach(function(sel){var n=document.querySelector(sel);if(n&&!n.id)n.id=idMap[sel];});}
  function buildRail(){
    var cfg=configs[page], rail=document.getElementById('rail');
    if(!cfg||!rail)return;
    rail.innerHTML='<span class="local-rail-title">'+cfg.title+'</span>'+cfg.items.map(function(x){return '<a class="local-rail-link" href="#'+x[1]+'" data-local-target="'+x[1]+'">'+x[0]+'</a>';}).join('');
  }
  function rewriteLinks(){
    var routes={foundation:'legal-grammar.html',matrix:'applied-legal-architecture.html','act2-threat-matrix':'applied-legal-architecture.html#act2-threat-matrix','act2-living-document':'applied-legal-architecture.html#act2-living-document','tooling-layer':'legal-architecture-in-operation.html','delivery-system':'legal-architecture-in-operation.html',contact:'legal-architecture-in-operation.html#contact'};
    document.querySelectorAll('a[href^="#"]').forEach(function(a){
      var id=(a.getAttribute('href')||'').slice(1); if(!id)return;
      var target=document.getElementById(id);
      if(target&&target.offsetParent!==null)return;
      if(routes[id])a.setAttribute('href',routes[id]);
    });
    var a1=document.querySelector('#act1-act2-bridge a[href="#matrix"]'); if(a1)a1.setAttribute('href','applied-legal-architecture.html');
    var a2=document.querySelector('#act2-act3-bridge a[href="#tooling-layer"]'); if(a2)a2.setAttribute('href','legal-architecture-in-operation.html');
  }
  function addTransition(){
    var main=document.getElementById('main'); if(!main)return;
    if(page==='home'){
      var sec=document.createElement('section'); sec.className='page-transition'; sec.id='page-transition';
      sec.innerHTML='<p class="eyebrow">BEGIN THE PORTFOLIO</p><h2>Start with how I determine what legally matters.</h2><p>Commercial labels do not determine legal consequences. The lawyer must identify the conduct, role, context and terminal harm; select the governing authority; test the factual trigger and exclusion; and determine the consequence and appropriate response.</p><div class="page-transition-actions"><a class="btn" href="legal-grammar.html">Begin with Legal Grammar →</a><a class="btn sec" data-upstream-system-cta="true" data-continue-target="legal-grammar.html" href="'+liveUrl+'">Open the diligence system</a></div>';
      main.appendChild(sec);
    } else if(page==='act1'){
      var b1=document.getElementById('act1-act2-bridge'); if(b1&&!b1.querySelector('.page-return-link')){var l1=document.createElement('a');l1.className='page-return-link';l1.href='index.html';l1.textContent='← Return Home';b1.appendChild(l1);}
    } else if(page==='act2'){
      var b2=document.getElementById('act2-act3-bridge'); if(b2&&!b2.querySelector('.page-return-link')){var l2=document.createElement('a');l2.className='page-return-link';l2.href='legal-grammar.html';l2.textContent='← Return to Legal Grammar';b2.appendChild(l2);}
    }
  }
  function buildFooter(){
    var footer=document.querySelector('footer'); if(!footer)return;
    footer.innerHTML='<div class="editorial-footer"><div class="editorial-footer-brand"><strong>The Interface</strong><span>Law × Technology · AI Governance · Privacy · Systems</span></div><div><div class="editorial-footer-links"><a href="https://linkedin.com/in/shwetabh-singh" target="_blank" rel="noopener">LinkedIn</a><a href="mailto:shwetav.alpna.singh@gmail.com">Email</a><a href="legal-architecture-in-operation.html#contact">Contact</a><span>© 2026 Shwetav Singh</span></div><div class="editorial-footer-note">Public, synthetic and scrubbed proof only.</div></div></div>';
  }
  function menu(){var btn=document.querySelector('.editorial-menu-toggle'),nav=document.getElementById('editorial-nav');if(!btn||!nav)return;btn.addEventListener('click',function(){var open=nav.classList.toggle('open');btn.setAttribute('aria-expanded',open?'true':'false');});}
  function spy(){var links=[].slice.call(document.querySelectorAll('[data-local-target]'));if(!links.length)return;function update(){var cur=0;links.forEach(function(l,i){var n=document.getElementById(l.getAttribute('data-local-target'));if(n&&n.getBoundingClientRect().top<window.innerHeight*.38)cur=i;});links.forEach(function(l,i){l.classList.toggle('active',i===cur);});}window.addEventListener('scroll',update,{passive:true});update();}
  function init(){
    if(!document.getElementById('main')||!document.querySelector('#main>section')){setTimeout(init,60);return;}
    assignIds(); buildRail(); rewriteLinks(); addTransition(); buildFooter(); menu(); spy();
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
'''

(assets / 'editorial-multipage.css').write_text(css.strip() + '\n', encoding='utf-8')
(assets / 'editorial-multipage.js').write_text(js.strip() + '\n', encoding='utf-8')

print('Built four-page editorial portfolio without rewriting locked Act content.')
