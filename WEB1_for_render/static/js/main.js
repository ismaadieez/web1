document.addEventListener('DOMContentLoaded', function(){
  // Smooth scroll para enlaces internos (si los hubiera)
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener('click', e=>{
      e.preventDefault();
      document.querySelector(a.getAttribute('href')).scrollIntoView({behavior:'smooth'});
    });
  });
});
