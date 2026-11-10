// ---------------------------------------------------------------
//  Animations de la page (hors 3D)
// ---------------------------------------------------------------
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// Défilement fluide (Lenis), sauf si l'utilisateur préfère moins d'animations
if (window.Lenis && !reduceMotion) {
    const lenis = new window.Lenis({ duration: 1.15, smoothWheel: true });
    function boucle(temps) {
        lenis.raf(temps);
        requestAnimationFrame(boucle);
    }
    requestAnimationFrame(boucle);

    // Les liens internes (#projets…) défilent en douceur
    document.querySelectorAll('a[href^="#"]').forEach((lien) => {
        lien.addEventListener("click", (ev) => {
            const cible = document.querySelector(lien.getAttribute("href"));
            if (cible) {
                ev.preventDefault();
                lenis.scrollTo(cible, { offset: -80 });
            }
        });
    });
}

// Titres du héros : les lignes montent une fois la page chargée
requestAnimationFrame(() => document.documentElement.classList.add("charge"));

// Compteur qui défile jusqu'à sa valeur (20000 s'affiche « 20 000 » en français)
const format = new Intl.NumberFormat(document.documentElement.lang || "fr");

function ecrire(el, valeur) {
    el.textContent = format.format(valeur) + (el.dataset.suffixe || "");
}

function compter(el) {
    const fin = Number(el.dataset.valeur);
    const duree = 1600;
    const debut = performance.now();
    function etape(maintenant) {
        const p = Math.min((maintenant - debut) / duree, 1);
        const doux = 1 - Math.pow(1 - p, 4);
        ecrire(el, Math.round(fin * doux));
        if (p < 1) requestAnimationFrame(etape);
    }
    requestAnimationFrame(etape);
}

// Les visuels de projet s'inclinent en 3D en suivant la souris
if (!reduceMotion && window.matchMedia("(hover: hover)").matches) {
    document.querySelectorAll("[data-incliner]").forEach((zone) => {
        const cible = zone.querySelector(".ecrans, .icone-flottante");
        if (!cible) return;
        zone.addEventListener("pointermove", (ev) => {
            const r = zone.getBoundingClientRect();
            const x = (ev.clientX - r.left) / r.width - 0.5;
            const y = (ev.clientY - r.top) / r.height - 0.5;
            cible.style.transform = `rotateY(${x * 14}deg) rotateX(${-y * 10}deg)`;
        });
        zone.addEventListener("pointerleave", () => {
            cible.style.transform = "";
        });
    });
}

// Les blocs apparaissent quand ils entrent à l'écran
const observateur = new IntersectionObserver(
    (entrees) => {
        entrees.forEach((entree) => {
            if (!entree.isIntersecting) return;
            entree.target.classList.add("visible");
            entree.target.querySelectorAll("[data-valeur]").forEach((el) => {
                if (reduceMotion) {
                    ecrire(el, Number(el.dataset.valeur));
                } else {
                    compter(el);
                }
            });
            observateur.unobserve(entree.target);
        });
    },
    { threshold: 0.18 }
);

document.querySelectorAll(".reveler").forEach((el, i) => {
    // Petit décalage entre les éléments voisins
    el.style.transitionDelay = `${(i % 3) * 0.08}s`;
    observateur.observe(el);
});
