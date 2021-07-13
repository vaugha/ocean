const text = document.getElementById("iso");
let shadow = "";
for (let i = 0; i < 20; i++) {
  shadow += (shadow ? "," : "") + -i + "px " + i + "px 0 #d9d9d9";
}
text.style.textShadow = shadow;
