var icon = document.getElementById("icon");

icon.onclick = function () {
  document.body.classList.toggle("dark_mode");
  document.body.classList.toggle("light_mode");
  if (document.body.classList.contains("dark_mode")) {
    icon.classList.remove("fa-solid", "fa-moon");
    icon.classList.add("fa-regular", "fa-sun");
    localStorage.setItem('mode', 'dark');
  } else {
    icon.classList.remove("fa-regular", "fa-sun");
    icon.classList.add("fa-solid", "fa-moon");
    localStorage.setItem('mode', 'light');
  }
};

document.addEventListener('DOMContentLoaded', () => {
    const mode = localStorage.getItem('mode');
    if (mode === 'dark') {
        document.body.classList.add('dark_mode');
        icon.classList.remove("fa-solid", "fa-moon");
        icon.classList.add("fa-regular", "fa-sun");
    } else {
        document.body.classList.add('light_mode');
        icon.classList.remove("fa-regular", "fa-sun");
        icon.classList.add("fa-solid", "fa-moon");
    }
});
