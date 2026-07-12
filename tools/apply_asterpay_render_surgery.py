from pathlib import Path

PATH = Path("index.html")
text = PATH.read_text(encoding="utf-8")


def replace_once(old: str, new: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Expected exactly one match, found {count}: {old[:90]!r}")
    text = text.replace(old, new, 1)


replace_once(
    '<h1>I built a diligence engine that converts <span>product reality</span> into reviewable legal decisions.</h1>\n            <p class="hero-sub">It does not begin with a generic checklist or an open-ended prompt. It reconstructs the target, decomposes each offering into legally material activities, classifies those activities through domain-specific legal taxonomies, tests only the relevant obligations and exposure rows against evidence, controls and exclusions, and routes the result into drafting and review.</p>',
    '<h1>I turn complex <span>product reality</span> into reviewable legal decisions.</h1>\n            <p class="hero-sub">I am an advocate with a litigation foundation working across technology, data, commercial contracts and legal systems. I built the diligence engine to preserve that legal method in practice: reconstruct the target, decompose the offering into legally material activities, apply domain-specific legal taxonomies, test only the relevant obligations and exposure rows against evidence, controls and exclusions, and route the result into drafting and review.</p>',
)

replace_once(
    '  <a class="cta sticky-sandbox" href="https://sandbox.lexnovahq.com/interface-diligence/diligence-system/" target="_blank" rel="noopener">Open engine</a>\n\n',
    '',
)

for old in (
    'Run a target in the sandbox',
    'Open the complete diligence run',
    'Inspect the running system',
    'Enter the diligence sandbox →',
):
    text = text.replace(old, 'Enter the diligence sandbox')

replace_once(
    '<p class="section-intro">This is not a research paper or a conventional case study. It is a selected decision path through one synthetic diligence run, showing how the engine moves from activity mechanics to legal classification, obligation routing, exposure testing and remediation.</p>',
    '<p class="section-intro">This selected AsterPay run shows the method in operation: activity mechanics are established first, classifications narrow the review universe, obligations and exposure rows are applied against evidence and exclusions, and the resolved findings are rebuilt into coordinated legal architecture.</p>',
)

replace_once(
    '<p class="eyebrow">Synthetic target · AsterPay</p>\n            <h3>AI-enabled merchant payments, identity verification and credit-risk decisioning.</h3>\n            <p>AsterPay presents itself as one platform. The legal review cannot treat it as one activity. The run separates money movement, risk scoring, identity verification, model routing and grievance handling because each produces a different legal route.</p>',
    '<p class="eyebrow">Simulated diligence instruction · AsterPay</p>\n            <h3>AI-enabled merchant payments, identity verification and credit-risk decisioning.</h3>\n            <p>AsterPay is being reviewed for an enterprise rollout involving a licensed partner bank, merchant settlement, applicant scoring and third-party model services. The legal review cannot treat the platform as one activity. It separates money movement, risk scoring, identity verification, model routing and grievance handling because each produces a different legal route.</p>',
)

replace_once(
    '<div class="meta-cell"><strong>Decision status</strong><span>Review-ready, not final opinion</span></div>',
    '<div class="meta-cell"><strong>Review instruction</strong><span>Enterprise rollout and partner diligence</span></div>',
)

replace_once(
    '<h2>The builder is still a lawyer.</h2>\n          <p class="section-intro">My systems work grows out of litigation, legal drafting and operational responsibility. The technology is evidence that I can make legal reasoning structured and deployable inside a practice team.</p>',
    '<h2>Legal judgment is the foundation.</h2>\n          <p class="section-intro">My systems work grows out of litigation, legal drafting and operational responsibility. The technology is evidence that I can make legal reasoning structured, reviewable and deployable inside a practice team.</p>',
)

replace_once(
    '    .map-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }',
    '    .map-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }\n    .mobile-swipe-note { display: none; }',
)

replace_once(
    '    @media (max-width: 640px) {\n      .shell { width: min(100% - 24px, 1180px); }',
    '''    @media (max-width: 640px) {
      .shell { width: min(100% - 24px, 1180px); }
      .act2 h2 { font-size: clamp(2rem, 9.6vw, 2.75rem); line-height: 1.02; }
      .stage { margin-top: 40px; }
      .stage-title { gap: 10px; margin-bottom: 16px; }
      .activity-tabs {
        display: flex;
        overflow-x: auto;
        gap: 8px;
        padding-bottom: 8px;
        scroll-snap-type: x mandatory;
        -webkit-overflow-scrolling: touch;
      }
      .activity-tab { flex: 0 0 82%; scroll-snap-align: start; }
      .obligation-grid, .map-grid {
        display: flex;
        overflow-x: auto;
        gap: 10px;
        padding-bottom: 8px;
        scroll-snap-type: x mandatory;
        -webkit-overflow-scrolling: touch;
      }
      .obligation { flex: 0 0 88%; scroll-snap-align: start; }
      .map-card { flex: 0 0 82%; scroll-snap-align: start; }
      .mobile-swipe-note { display: block; margin: -4px 0 10px; color: #aaa69f; font-size: .72rem; }
      .architecture-table, .architecture-table tbody, .architecture-table tr, .architecture-table td { display: block; width: 100%; }
      .architecture-table thead { display: none; }
      .architecture-table { overflow: visible; background: transparent; }
      .architecture-table tr { margin-bottom: 12px; border: 1px solid #3a3c3e; background: #202326; }
      .architecture-table td { border: 0; border-top: 1px solid #3a3c3e; padding: 13px 14px; }
      .architecture-table td:first-child { border-top: 0; }
      .architecture-table td::before { display: block; margin-bottom: 5px; color: #d9b77a; font-size: .62rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }
      .architecture-table td:nth-child(1)::before { content: "Resolved issue"; }
      .architecture-table td:nth-child(2)::before { content: "Contract route"; }
      .architecture-table td:nth-child(3)::before { content: "Operational control"; }
      .architecture-table td:nth-child(4)::before { content: "Evidence / counsel route"; }
      .sticky-sandbox { display: none; }''',
)

text = text.replace('      .architecture-table { display: block; overflow-x: auto; }\n', '')
text = text.replace('      .sticky-sandbox { right: 12px; bottom: 12px; }\n', '')

replace_once(
    '          <div class="obligation-grid">',
    '          <p class="mobile-swipe-note">Swipe to inspect the routed obligations.</p>\n          <div class="obligation-grid">',
)
replace_once(
    '          <div class="map-grid">',
    '          <p class="mobile-swipe-note">Swipe to inspect the terminal harm categories.</p>\n          <div class="map-grid">',
)

PATH.write_text(text, encoding="utf-8")
print("AsterPay rendered-portfolio surgery applied.")
