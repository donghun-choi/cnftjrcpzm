const close_btn_for_recent = document.getElementsByClassName("close_btn_for_recent")[0];
const recent_five = document.getElementsByClassName("recent-five")[0];
const recent_five_view = document.getElementsByClassName("recent-five-view")[0];
const recent_five_container = document.getElementsByClassName("recent-container")[0];

recent_five.addEventListener("click", enable);
close_btn_for_recent.addEventListener("click", disable);

function enable() {
  recent_five.style.transitionDuration = "1s";
  recent_five.style.position = "fixed";
  recent_five.style.height = "90%";
  recent_five.style.top = "48px";
  recent_five.style.left = "50%";
  recent_five.style.transform = "translate(-50%)";
  recent_five.style.zIndex = "999999";

  recent_five_view.style.boxShadow = "0 0 1200px black";
  recent_five_view.style.borderRadius = "24px 24px 24px 24px";

  // container style
  recent_five_container.style.display = "none";

  close_btn_for_recent.style.display = "block";
  close_btn_for_recent.style.position = "fixed";
  close_btn_for_recent.style.zIndex = "9999999";
  setTimeout(handleObjWidth, 1000);
}
function handleObjWidth() {
  recent_five.style.width = "92%";
}

function disable() {
  recent_five.style.transitionDuration = " 1s";
  recent_five.style.position = "static";
  recent_five.style.height = "";
  recent_five.style.width = "";
  recent_five.style.top = "";
  recent_five.style.left = "";
  recent_five.style.transform = "";
  recent_five.style.zIndex = "";

  recent_five_view.style.boxShadow = "";
  recent_five_view.style.borderRadius = "";

  // container style
  recent_five_container.style.display = "flex";

  close_btn_for_recent.style.display = "none";
  close_btn_for_recent.style.position = "";
}
//
//
//
//
//
//
function getTheme() {
  return localStorage.getItem("theme") || "light";
}
function saveTheme(theme) {
  localStorage.setItem("theme", theme);
}

function applyTheme(theme) {
  document.body.className = theme;
}

function rotateTheme(theme) {
  if (theme === "light") {
    return "dark";
  }
  return "light";
}

const themeDisplay = document.getElementById("theme");
const themeToggler = document.getElementById("theme-toggle");

let theme = getTheme();
applyTheme(theme);
themeDisplay.innerText = theme;

themeToggler.onclick = () => {
  const newTheme = rotateTheme(theme);
  applyTheme(newTheme);
  themeDisplay.innerText = newTheme;
  saveTheme(newTheme);

  theme = newTheme;
};
