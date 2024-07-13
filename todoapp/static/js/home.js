// script.js

document.addEventListener('DOMContentLoaded', function() {
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.createElement('div');
  const overlay = document.createElement('div');
  
  mobileMenu.classList.add('mobile-menu');
  mobileMenu.innerHTML = `
      <div class="user-info">
          <span class="username">Usuario</span>
          <a href="#" class="logout-btn">Cerrar Sesión</a>
      </div>
  `;
  document.body.appendChild(mobileMenu);

  overlay.classList.add('overlay');
  document.body.appendChild(overlay);

  mobileMenuBtn.addEventListener('click', function() {
      mobileMenu.classList.toggle('show');
      overlay.classList.toggle('show');
  });

  overlay.addEventListener('click', function() {
      mobileMenu.classList.remove('show');
      overlay.classList.remove('show');
  });
});
