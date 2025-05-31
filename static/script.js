const openFormBtn = document.getElementById('open-form');
const closeFormBtn = document.getElementById('close-form');
const overlay = document.getElementById('overlay');
const sliders = ['bmi', 'menthlth', 'physhlth'];

// Open form overlay
  openFormBtn.addEventListener('click', () => {
      overlay.classList.add('active');
      overlay.style.display = 'flex'; // Show overlay
      document.body.style.overflow = 'hidden'; // Disable background scrolling
  });

// Close form overlay
  closeFormBtn.addEventListener('click', () => {
      overlay.classList.remove('active');
      overlay.style.display = 'none'; // Hide overlay
      document.body.style.overflow = ''; // Enable background scrolling
  });

  function nextSection(currentSection) {
      document.getElementById(`section-${currentSection}`).classList.remove('active');
      document.getElementById(`section-${currentSection + 1}`).classList.add('active');
      document.querySelectorAll('.progress-step')[currentSection].classList.add('active');
      document.getElementById('progress-fill').style.width = `${(currentSection + 1) * 33.33}%`;
    }

    function prevSection(currentSection) {
      document.getElementById(`section-${currentSection}`).classList.remove('active');
      document.getElementById(`section-${currentSection - 1}`).classList.add('active');
      document.querySelectorAll('.progress-step')[currentSection - 1].classList.remove('active');
      document.getElementById('progress-fill').style.width = `${(currentSection - 1) * 33.33}%`;
    }

    // Slider sync
    sliders.forEach(id => {
      const input = document.getElementById(id);
      const slider = document.getElementById(`${id}-slider`);
      
      input.addEventListener('input', (e) => {
        slider.value = e.target.value;
      });
      
      slider.addEventListener('input', (e) => {
        input.value = e.target.value;
      });
    });
