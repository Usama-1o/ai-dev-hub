let count = 0;

const btn = document.getElementById("btn");
const countText = document.getElementById("count");

btn.addEventListener("click", () => {
  count++;
  countText.innerText = count;
});
