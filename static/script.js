// simple smooth cursor particles (no annoying movement)

const particles = [];
for (let i = 0; i < 8; i++) {
    let p = document.createElement("div");
    p.className = "cursor-particle";
    document.body.appendChild(p);
    particles.push(p);
}

document.addEventListener("mousemove", e => {
    particles.forEach((p, i) => {
        setTimeout(() => {
            p.style.left = e.clientX + "px";
            p.style.top = e.clientY + "px";
        }, i * 20);
    });
});