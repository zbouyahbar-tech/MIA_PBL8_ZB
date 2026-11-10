// ---------------------------------------------------------------
//  Fond 3D du site (three.js)
//  - un monogramme « Z » fait de trois plaques arrondies
//  - un champ de petites plaques qui dérivent en diagonale
//  Le Z suit la souris et se disloque en fragments au défilement.
// ---------------------------------------------------------------
import * as THREE from "three";
import { RoundedBoxGeometry } from "three/addons/geometries/RoundedBoxGeometry.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

const canvas = document.getElementById("scene");
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const isSmall = window.innerWidth < 760;
// Le Z n'apparaît que sur l'accueil ; les pages de l'atelier gardent seulement les fragments
const avecMonogramme = document.body.dataset.page === "accueil";

const COULEUR = new THREE.Color("#c9d0d2");
const FOND = new THREE.Color("#000000");

// --- Rendu, scène, caméra -------------------------------------
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, isSmall ? 1.5 : 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(FOND, 1);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 0.9;

const scene = new THREE.Scene();
scene.fog = new THREE.Fog(FOND, 12, 32);

const pmrem = new THREE.PMREMGenerator(renderer);
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;

const camera = new THREE.PerspectiveCamera(32, window.innerWidth / window.innerHeight, 0.1, 100);
camera.position.set(0, 0, 14);

const lumiere = new THREE.DirectionalLight(0xffffff, 1.25);
lumiere.position.set(-4, 6, 8);
scene.add(lumiere);
scene.add(new THREE.AmbientLight(0xffffff, 0.15));

const matiere = new THREE.MeshStandardMaterial({ color: COULEUR, roughness: 0.34, metalness: 0.1 });

// --- Le monogramme Z ------------------------------------------
// Trois plaques plates séparées par un petit espace : un Z « en fragments »
const monogramme = new THREE.Group();
const epaisseur = 0.8;   // largeur d'un trait du Z
const profondeur = 0.3;  // épaisseur des plaques
const largeur = 3.4;
const hauteur = 3.8;
const espace = 0.24;

const barreGeo = new RoundedBoxGeometry(largeur, epaisseur, profondeur, 5, 0.12);
const haut = new THREE.Mesh(barreGeo, matiere);
haut.position.set(0, hauteur / 2 - epaisseur / 2, 0);
const bas = new THREE.Mesh(barreGeo, matiere);
bas.position.set(0, -hauteur / 2 + epaisseur / 2, 0);

// La diagonale relie le coin intérieur droit du haut au coin intérieur gauche du bas
const debut = new THREE.Vector2(largeur / 2 - epaisseur * 0.55, hauteur / 2 - epaisseur - espace);
const fin = new THREE.Vector2(-largeur / 2 + epaisseur * 0.55, -hauteur / 2 + epaisseur + espace);
const diagGeo = new RoundedBoxGeometry(debut.distanceTo(fin), epaisseur, profondeur, 5, 0.12);
const diagonale = new THREE.Mesh(diagGeo, matiere);
diagonale.rotation.z = Math.atan2(debut.y - fin.y, debut.x - fin.x);

const pieces = [haut, diagonale, bas];
// Direction dans laquelle chaque pièce s'éloigne quand on défile
const eclatement = [
  new THREE.Vector3(0.6, 1.6, 0.8),
  new THREE.Vector3(-0.4, 0.1, 1.6),
  new THREE.Vector3(-0.8, -1.5, 0.5),
];
pieces.forEach((p) => {
  p.userData.base = p.position.clone();
  p.userData.baseRot = p.rotation.clone();
  monogramme.add(p);
});

monogramme.rotation.set(-0.36, 0.48, 0.06);
scene.add(monogramme);

// --- Le champ de fragments qui dérivent -----------------------
const nbFragments = isSmall ? 22 : 44;
const fragGeo = new RoundedBoxGeometry(1, 0.12, 0.42, 3, 0.05);
const matiereFragments = new THREE.MeshStandardMaterial({ color: "#7d8587", roughness: 0.5, metalness: 0.05 });
const fragments = new THREE.InstancedMesh(fragGeo, matiereFragments, nbFragments);
const etats = [];
const zone = { x: 30, y: 18, zMin: -20, zMax: -7 };
const direction = new THREE.Vector3(0.55, 0.42, 0).normalize();
const factice = new THREE.Object3D();

for (let i = 0; i < nbFragments; i++) {
  etats.push({
    x: (Math.random() - 0.5) * zone.x,
    y: (Math.random() - 0.5) * zone.y,
    z: zone.zMin + Math.random() * (zone.zMax - zone.zMin),
    echelle: 0.5 + Math.random() * 1.3,
    vitesse: 0.2 + Math.random() * 0.35,
    phase: Math.random() * Math.PI * 2,
  });
}
scene.add(fragments);

function placerFragments(t, dt) {
  for (let i = 0; i < nbFragments; i++) {
    const e = etats[i];
    if (!reduceMotion) {
      e.x += direction.x * e.vitesse * dt;
      e.y += direction.y * e.vitesse * dt;
    }
    // On fait réapparaître de l'autre côté ce qui sort du cadre
    if (e.x > zone.x / 2) e.x -= zone.x;
    if (e.y > zone.y / 2) e.y -= zone.y;
    factice.position.set(e.x, e.y, e.z);
    factice.rotation.set(-0.95, 0.0, 0.62 + Math.sin(t * 0.3 + e.phase) * 0.05);
    factice.scale.set(e.echelle, 1, e.echelle * 0.8);
    factice.updateMatrix();
    fragments.setMatrixAt(i, factice.matrix);
  }
  fragments.instanceMatrix.needsUpdate = true;
}

// --- Souris et défilement --------------------------------------
const souris = new THREE.Vector2(0, 0);
const sourisLissee = new THREE.Vector2(0, 0);
window.addEventListener("pointermove", (ev) => {
  souris.set((ev.clientX / window.innerWidth) * 2 - 1, (ev.clientY / window.innerHeight) * 2 - 1);
});

let progression = 0; // 0 en haut de page, 1 après un écran de défilement
function lireDefilement() {
  progression = Math.min(window.scrollY / window.innerHeight, 1.5);
}
window.addEventListener("scroll", lireDefilement, { passive: true });
lireDefilement();

function placerMonogramme() {
  // Sur ordinateur le Z est à droite du titre, sur téléphone il passe au-dessus
  const large = window.innerWidth >= 900;
  monogramme.position.set(large ? 3.3 : 0, large ? 0.1 : 2.1, 0);
  monogramme.scale.setScalar(large ? 1 : 0.56);
}
placerMonogramme();

window.addEventListener("resize", () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
  placerMonogramme();
});

// --- Boucle d'animation ----------------------------------------
const horloge = new THREE.Clock();

function animer() {
  const dt = Math.min(horloge.getDelta(), 0.05);
  const t = horloge.elapsedTime;

  sourisLissee.lerp(souris, 0.05);
  const p = Math.min(progression, 1);
  const douce = p * p * (3 - 2 * p); // accélération en douceur

  monogramme.rotation.x = -0.36 + sourisLissee.y * 0.18 + (reduceMotion ? 0 : Math.sin(t * 0.5) * 0.04);
  monogramme.rotation.y = 0.48 + sourisLissee.x * 0.3 + douce * 0.9;
  monogramme.position.y += ((window.innerWidth >= 900 ? 0.1 : 2.1) + (reduceMotion ? 0 : Math.sin(t * 0.8) * 0.08) - monogramme.position.y) * 0.1;

  pieces.forEach((piece, i) => {
    const dir = eclatement[i];
    piece.position.copy(piece.userData.base).addScaledVector(dir, douce * 2.4);
    piece.rotation.x = piece.userData.baseRot.x + douce * (i - 1) * 0.9;
    piece.rotation.y = piece.userData.baseRot.y + douce * (1 - i) * 0.6;
  });

  // Le Z s'éloigne jusqu'à disparaître dans le brouillard, puis n'est plus dessiné
  monogramme.position.z = -douce * 22;
  monogramme.visible = avecMonogramme && progression < 1.05;

  camera.position.x = sourisLissee.x * 0.35;
  camera.position.y = -sourisLissee.y * 0.25 - douce * 0.8;
  camera.lookAt(0, -douce * 0.8, 0);

  placerFragments(t, dt);
  renderer.render(scene, camera);
  requestAnimationFrame(animer);
}

animer();
document.documentElement.classList.add("scene-prete");
