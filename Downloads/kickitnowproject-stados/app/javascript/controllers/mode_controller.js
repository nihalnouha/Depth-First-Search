import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  connect() {
    const sunImg = 'https://res.cloudinary.com/ddiq9sddp/image/upload/v1707409516/sun_rolj04.png'
    const moonImg = 'https://res.cloudinary.com/ddiq9sddp/image/upload/v1707409516/moon_o73l3g.png'
    const switchImg = document.getElementById('dark-switch');

    // Set the default theme to dark if no setting is found in local storage
    const currentTheme = localStorage.getItem('mode') || 'dark';
    document.body.className = 'theme-' + currentTheme;

    switchImg.src = currentTheme === 'dark' ? sunImg : moonImg;

    switchImg.addEventListener('click', function () {
      const currentTheme = localStorage.getItem('mode') || 'dark';

      if (currentTheme === 'dark') {
          document.body.className = 'theme-light';
          
          localStorage.setItem('mode', 'light');
          switchImg.src = moonImg;
      } else {
        document.body.className = 'theme-dark';
        localStorage.setItem('mode', 'dark');
        switchImg.src = sunImg;
      }
    });
  }
}
