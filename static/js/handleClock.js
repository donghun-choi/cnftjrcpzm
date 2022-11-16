const secondHand = document.querySelector(".second-hand");
const minsHand = document.querySelector(".min-hand");
const hourHand = document.querySelector(".hour-hand");
const timeText = document.querySelector(".timetext");

function setDate() {
  const now = new Date();

  const hour = now.getHours();
  const mins = now.getMinutes();
  const seconds = now.getSeconds();
  const milliseconds = now.getMilliseconds();

  const secondsDegrees = (seconds / 60) * 360 + 90 + (milliseconds / 10000) * 60;
  secondHand.style.transform = `rotate(${secondsDegrees}deg)`;

  const minsDegrees = (mins / 60) * 360 + (seconds / 60) * 6 + 90;
  minsHand.style.transform = `rotate(${minsDegrees}deg)`;

  const hourDegrees = (hour / 12) * 360 + (mins / 60) * 30 + 90;
  hourHand.style.transform = `rotate(${hourDegrees}deg)`;

  timeText.innerHTML = `${hour < 10 ? `0${hour}` : hour}:${mins < 10 ? `0${mins}` : mins}:${seconds < 10 ? `0${seconds}` : seconds}`;
}

setInterval(setDate, 1);

setDate();
