document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.member-card');

    // Opsi untuk Intersection Observer
    const observerOptions = {
        threshold: 0.1, // Animasi mulai saat 10% kartu terlihat
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Menambahkan delay bertingkat agar munculnya tidak barengan (efek domino)
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, index * 150); // Delay 150ms antar kartu jika muncul bersamaan
                
                // Berhenti mengamati kartu yang sudah muncul
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    cards.forEach(card => {
        observer.observe(card);
    });
});
