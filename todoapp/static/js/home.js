// script.js

const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu-content');
const overlay = document.getElementById('overlay');

mobileMenuBtn.addEventListener('click', function() {
    mobileMenu.classList.toggle('show');
    overlay.classList.toggle('show');
});

overlay.addEventListener('click', function() {
    mobileMenu.classList.remove('show');
    overlay.classList.remove('show');
});
