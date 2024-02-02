document.addEventListener("DOMContentLoaded", function () {
    const a = document.querySelectorAll(".a");
    const b = document.querySelectorAll(".b");
    const c = document.querySelectorAll(".c");

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
            }
        });
    }, { threshold: 0.5 }); // Половина элемента видима

    a.forEach(box => {
        observer.observe(box);
    });

    b.forEach(box => {
        observer.observe(box);
    });

    c.forEach(box => {
        observer.observe(box);
    });
});