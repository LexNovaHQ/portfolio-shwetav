(function(){
  var page=document.body.getAttribute('data-page')||'home';
  var liveUrl='https://sandbox.lexnovahq.com/interface-diligence/diligence-system/';
  var contactUrl='legal-architecture-in-operation.html#contact';
  var emailAddress='shwetav.alpna.singh@gmail.com';
  var fixes=document.createElement('link');
  fixes.rel='stylesheet';
  fixes.href='assets/editorial-multipage-fixes.css';
  document.head.appendChild(fixes);
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
    var routes={foundation:'legal-grammar.html',matrix:'applied-legal-architecture.html','act2-threat-matrix':'applied-legal-architecture.html#act2-threat-matrix','act2-living-document':'applied-legal-architecture.html#act2-living-document','tooling-layer':'legal-architecture-in-operation.html','delivery-system':'legal-architecture-in-operation.html',contact:contactUrl};
    document.querySelectorAll('a[href^="#"]').forEach(function(a){
      var id=(a.getAttribute('href')||'').slice(1); if(!id)return;
      var target=document.getElementById(id);
      if(target&&target.offsetParent!==null)return;
      if(routes[id])a.setAttribute('href',routes[id]);
    });
    document.querySelectorAll('a').forEach(function(a){
      var label=(a.textContent||'').trim().toLowerCase();
      if(label==='contact'){
        a.setAttribute('href',page==='act3'?'#contact':contactUrl);
        a.setAttribute('data-contact-link','true');
      }
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
      var b1=document.getElementById('act1-act2-bridge');
      if(b1&&!b1.querySelector('.page-return-link')){
        var l1=document.createElement('a');l1.className='page-return-link';l1.href='index.html';l1.textContent='← Return Home';
        (b1.querySelector('.journey-bridge-actions')||b1).appendChild(l1);
      }
    } else if(page==='act2'){
      var b2=document.getElementById('act2-act3-bridge');
      if(b2&&!b2.querySelector('.page-return-link')){
        var l2=document.createElement('a');l2.className='page-return-link';l2.href='legal-grammar.html';l2.textContent='← Return to Legal Grammar';
        (b2.querySelector('.journey-bridge-actions')||b2).appendChild(l2);
      }
    }
  }
  function buildFooter(){
    var footer=document.querySelector('footer'); if(!footer)return;
    footer.innerHTML='<div class="editorial-footer"><div class="editorial-footer-brand"><strong>The Interface</strong><span>Law × Technology · AI Governance · Privacy · Systems</span></div><div><div class="editorial-footer-links"><a href="https://linkedin.com/in/shwetabh-singh" target="_blank" rel="noopener">LinkedIn</a><a href="mailto:'+emailAddress+'" data-email-link="true">Email</a><a href="'+(page==='act3'?'#contact':contactUrl)+'" data-contact-link="true">Contact</a><span>© 2026 Shwetav Singh</span></div><div class="editorial-footer-note">Public, synthetic and scrubbed proof only.</div></div></div>';
  }
  function wireContactAndEmail(){
    document.addEventListener('click',function(event){
      var contact=event.target.closest('a[data-contact-link="true"]');
      if(contact){
        event.preventDefault();
        if(page==='act3'){
          var target=document.getElementById('contact');
          if(target){target.scrollIntoView({behavior:'smooth',block:'start'});history.replaceState(null,'','#contact');}
          else window.location.href=contactUrl;
        }else window.location.href=contactUrl;
        return;
      }
      var email=event.target.closest('a[data-email-link="true"]');
      if(email){
        email.setAttribute('href','mailto:'+emailAddress);
        window.location.href='mailto:'+emailAddress;
      }
    });
  }
  function menu(){var btn=document.querySelector('.editorial-menu-toggle'),nav=document.getElementById('editorial-nav');if(!btn||!nav)return;btn.addEventListener('click',function(){var open=nav.classList.toggle('open');btn.setAttribute('aria-expanded',open?'true':'false');});}
  function spy(){var links=[].slice.call(document.querySelectorAll('[data-local-target]'));if(!links.length)return;function update(){var cur=0;links.forEach(function(l,i){var n=document.getElementById(l.getAttribute('data-local-target'));if(n&&n.getBoundingClientRect().top<window.innerHeight*.38)cur=i;});links.forEach(function(l,i){l.classList.toggle('active',i===cur);});}window.addEventListener('scroll',update,{passive:true});update();}
  function init(){
    if(!document.getElementById('main')||!document.querySelector('#main>section')){setTimeout(init,60);return;}
    assignIds(); buildRail(); rewriteLinks(); addTransition(); buildFooter(); wireContactAndEmail(); menu(); spy();
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();