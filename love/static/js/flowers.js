const container = document.querySelector(".flowers");

for (let i = 0; i < 25; i++) {
    const flower = document.createElement("img");
    flower.src = "/static/images/flower.png"; // PNG path
    flower.classList.add("flower");
    flower.style.left = Math.random() * 100 + "vw";
    flower.style.animationDuration = 5 + Math.random() * 6 + "s";
    flower.style.opacity = Math.random();
    container.appendChild(flower);
}

