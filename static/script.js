const openFormBtn = document.getElementById('open-form');
const closeFormBtn = document.getElementById('close-form');
const overlay = document.getElementById('overlay');

  openFormBtn.addEventListener('click', () => {
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden'; // Disable background scrolling
  });

  closeFormBtn.addEventListener('click', () => {
      overlay.classList.remove('active');
      document.body.style.overflow = ''; // Enable background scrolling
  });