(function(){
 const banner=document.querySelector('.review-banner');
 const slides=[...banner.querySelectorAll('.review-banner__slide')];
 const dots=[...banner.querySelectorAll('.review-banner__dot')];
 const reduceMotion=window.matchMedia('(prefers-reduced-motion: reduce)');
 let current=0, timer;
 function show(i){current=i;slides.forEach((s,n)=>s.hidden=n!==i);dots.forEach((d,n)=>d.setAttribute('aria-pressed',String(n===i)));}
 function stop(){clearInterval(timer);}
 function start(){stop();if(!reduceMotion.matches&&!document.hidden)timer=setInterval(()=>show((current+1)%slides.length),6000);}
 dots.forEach((d,i)=>d.addEventListener('click',()=>{show(i);stop();}));
 banner.addEventListener('mouseenter',stop);banner.addEventListener('mouseleave',start);
 banner.addEventListener('focusin',stop);banner.addEventListener('focusout',e=>{if(!banner.contains(e.relatedTarget))start();});
 document.addEventListener('visibilitychange',()=>document.hidden?stop():start());
 reduceMotion.addEventListener('change',start);start();
})();
