# ---------------------------------------------------------------
#  Tout le texte du site, en français et en anglais.
#  L("texte français", "English text") : la fonction contenu(lang)
#  garde la bonne langue et renvoie un dictionnaire prêt pour le template.
# ---------------------------------------------------------------

EMAIL = "zacharie.bouyahbar@2031.icam.fr"


def L(fr, en):
    return {"fr": fr, "en": en}


CONTENU = {
    "meta": {
        "titre": L("Zacharie Bouyahbar · Élève ingénieur & développeur d'applications",
                   "Zacharie Bouyahbar · Engineering student & app developer"),
        "description": L("Élève ingénieur à l'ICAM, je conçois des applications iPhone et Android, des outils d'IA et des jeux.",
                         "Engineering student at ICAM, I build iPhone and Android apps, AI tools and games."),
    },
    "menu": {
        "projets": L("Projets", "Work"),
        "parcours": L("Parcours", "Journey"),
        "apropos": L("À propos", "About"),
        "contact": L("Me contacter", "Contact me"),
    },
    "heros": {
        "etiquette": L("Élève ingénieur · ICAM Grand Paris Sud", "Engineering student · ICAM Grand Paris Sud"),
        "lignes": L(["J'imagine,", "je code,", "je livre."], ["I imagine,", "I code,", "I ship."]),
        "chapeau": L("Élève ingénieur généraliste et développeur d'applications iPhone et Android, je mène mes projets de la première idée jusqu'à l'App Store, avec l'IA comme outil de travail.",
                     "General engineering student and iPhone & Android developer, I take projects from the first idea all the way to the App Store, with AI as a working tool."),
        "bouton_projets": L("Voir mes projets", "See my work"),
        "bouton_contact": L("Me contacter", "Get in touch"),
        "defiler": L("Défiler", "Scroll"),
    },
    "bandeau": ["Swift", "SwiftUI", "Kotlin", "Python", "Whisper", "LLM", "SceneKit", "SpriteKit",
                "AES-256 · RSA-2048", "Eurocodes", "Flask", "three.js"],
    "apropos": {
        "etiquette": L("À propos", "About"),
        "texte": L("Élève ingénieur à l'ICAM Grand Paris Sud, je travaille depuis juillet 2025 dans la division IA d'ADERA-RD, où je développe Adera Scribe, publiée sur l'App Store. En stage chez ATHIS, j'ai réécrit de zéro leur application de calcul de structure, elle aussi en ligne sur l'App Store.",
                   "Engineering student at ICAM Grand Paris Sud, I have been working in ADERA-RD's AI division since July 2025, where I build Adera Scribe, live on the App Store. During my internship at ATHIS, I rewrote their structural engineering app from scratch, now live on the App Store too."),
        "doux": L("Allier la rigueur scientifique au sens du produit.", "Combining scientific rigour with a feel for the product."),
        "chiffres": [
            {"valeur": 3, "suffixe": "", "legende": L("applications publiées sur l'App Store", "apps live on the App Store")},
            {"valeur": 20000, "suffixe": "+", "legende": L("lignes de Swift pour ATHIS Construction", "lines of Swift for ATHIS Construction")},
            {"valeur": 16, "suffixe": "", "legende": L("jeux développés et testés", "games built and tested")},
            {"valeur": 860, "suffixe": "", "legende": L("niveaux générés pour Cascade", "generated levels in Cascade")},
        ],
    },
    "competences": {
        "etiquette": L("Ce que je fais", "What I do"),
        "titre": L("Du code à l'ingénierie", "From code to engineering"),
        "texte": L("Je touche à toute la chaîne : l'idée, l'interface, le code, la sécurité, la publication. Et à l'école, l'électronique, la mécanique et les matériaux.",
                   "I cover the whole chain: the idea, the interface, the code, security, release. And at school, electronics, mechanics and materials."),
        "liste": [
            {"titre": L("Applications mobiles", "Mobile apps"),
             "texte": L("Des applications iPhone et Android natives, de la maquette jusqu'à la publication sur l'App Store.",
                        "Native iPhone and Android apps, from the first mock-up to the App Store release."),
             "outils": "Swift · SwiftUI · Kotlin · Jetpack Compose · App Store Connect"},
            {"titre": L("IA & sécurité", "AI & security"),
             "texte": L("Transcription avec Whisper, comptes rendus rédigés par un LLM, chiffrement des données directement sur l'appareil.",
                        "Whisper transcription, LLM-written reports, data encrypted right on the device."),
             "outils": "Python · Whisper · LLM · AES-256 · RSA-2048"},
            {"titre": L("Jeux", "Games"),
             "texte": L("3D temps réel, moteurs de jeu et génération procédurale de niveaux vérifiés par un solveur.",
                        "Real-time 3D, game engines and procedurally generated levels checked by a solver."),
             "outils": "SceneKit · SpriteKit · Game Center · StoreKit"},
            {"titre": L("Ingénierie", "Engineering"),
             "texte": L("Projets d'école en électronique, mécanique et matériaux : drone stabilisé, commande de moteur, choix d'un composite.",
                        "School projects in electronics, mechanics and materials: a stabilised drone, motor control, choosing a composite."),
             "outils": "Arduino · LTspice · Eurocodes · Ashby"},
        ],
    },
    "projets": {
        "etiquette": L("Projets", "Work"),
        "titre": L("Ce que j'ai construit", "What I've built"),
        "texte": L("Trois applications publiées sur l'App Store, dont une application métier réécrite de zéro, et des jeux conçus de A à Z.",
                   "Three apps live on the App Store, including a professional app rewritten from scratch, and games designed end to end."),
        "voir": L("Voir le projet", "View project"),
        "fait": L("Ce que j'ai fait", "What I did"),
        "principaux": [
            {
                "nom": "Adera Scribe",
                "etiquette": L("ADERA-RD · IA · App Store", "ADERA-RD · AI · App Store"),
                "statut": L("Publiée sur l'App Store", "Live on the App Store"),
                "texte": L("Une application qui enregistre vos réunions et chiffre chaque enregistrement sur le téléphone. Un logiciel compagnon le transcrit, puis rédige un compte rendu adapté à votre métier, parmi une vingtaine de profils.",
                           "An app that records your meetings and encrypts every recording on the phone. A companion program transcribes it, then writes a report tailored to your profession, among about twenty profiles."),
                "fait": L(["Installateur Mac et Windows signé et notarisé par Apple",
                           "Une paire de clés par client, au lieu d'une clé partagée par tous",
                           "Portage Android natif en Kotlin",
                           "Lancement et optimisation de la fiche App Store"],
                          ["Mac and Windows installer, signed and notarised by Apple",
                           "One key pair per customer instead of a single shared key",
                           "Native Android port in Kotlin",
                           "Launch and App Store listing optimisation"]),
                "puces": ["SwiftUI", "AES-256-GCM", "RSA-2048", "Whisper", "Kotlin"],
                "lien": "https://apps.apple.com/fr/app/adera-scribe-réunion-ia/id6761719656",
                "lien_texte": L("Voir sur l'App Store", "View on the App Store"),
                "captures": ["scribe-1", "scribe-2", "scribe-3"],
            },
            {
                "nom": "ATHIS Construction",
                "etiquette": L("Stage · ATHIS · Bureau d'études", "Internship · ATHIS · Engineering firm"),
                "statut": L("Publiée sur l'App Store", "Live on the App Store"),
                "texte": L("L'application de calcul de structure d'ATHIS datait de 2016 et ne compilait plus. Je l'ai réécrite de zéro pour iPhone et iPad : calculs selon les Eurocodes et le BAEL, note de calcul exportée en PDF, et remplissage par IA (voix, photo de plan) qui fonctionne hors ligne.",
                           "ATHIS's structural engineering app dated from 2016 and no longer compiled. I rewrote it from scratch for iPhone and iPad: calculations following the Eurocodes and BAEL, PDF calculation reports, and AI-assisted input (voice, photo of a plan) that works offline."),
                "fait": L(["Environ 20 000 lignes de Swift",
                           "Formules vérifiées et réunies dans un document de référence",
                           "Tests unitaires sur les calculs",
                           "Interface iPhone et iPad"],
                          ["About 20,000 lines of Swift",
                           "Formulas checked and gathered in a reference document",
                           "Unit tests on the calculations",
                           "iPhone and iPad interface"]),
                "puces": ["SwiftUI", "Eurocodes 2 · 3 · 5 · 7", "BAEL", "PDF", "Tests"],
                "lien": "https://apps.apple.com/fr/app/construction-full/id416557937",
                "lien_texte": L("Voir sur l'App Store", "View on the App Store"),
                "captures": ["athis-1", "athis-2", "athis-3"],
            },
        ],
        "jeux": [
            {
                "nom": "Cascade",
                "etiquette": L("Jeu · Puzzle · App Store", "Game · Puzzle · App Store"),
                "statut": L("Publié sur l'App Store", "Live on the App Store"),
                "texte": L("Un puzzle de réactions en chaîne : 860 niveaux générés automatiquement et vérifiés par un solveur, répartis en 18 mondes, avec un défi quotidien.",
                           "A chain-reaction puzzle: 860 automatically generated levels, each checked by a solver, across 18 worlds, plus a daily challenge."),
                "puces": ["SpriteKit", L("Solveur", "Solver"), L("Génération procédurale", "Procedural generation")],
                "icone": "cascade",
                "captures": ["cascade-1", "cascade-2", "cascade-3"],
                "lien": "https://apps.apple.com/fr/app/cascade-puzzle-en-chaîne/id6780939956",
                "lien_texte": L("Voir sur l'App Store", "View on the App Store"),
            },
            {
                "nom": "Médina Rush",
                "etiquette": L("Jeu · 3D · iOS", "Game · 3D · iOS"),
                "texte": L("Une course infinie en 3D : Bala, un âne sur un tapis volant, traverse quatre décors marocains. Modèles 3D, sons et icône sont générés par le code.",
                           "A 3D endless runner: Bala, a donkey on a flying carpet, races through four Moroccan settings. 3D models, sounds and icon are all generated by code."),
                "puces": ["SceneKit", "Game Center", "FR · EN · AR"],
                "icone": "medina-rush",
                "captures": [],
            },
            {
                "nom": "Salon de Jeu",
                "etiquette": L("Jeu · Cartes · iOS", "Game · Cards · iOS"),
                "texte": L("La bataille corse et le blackjack, contre l'IA ou à plusieurs sur le même téléphone. Cartes et sons sont dessinés par le code.",
                           "Slapjack-style Bataille Corse and blackjack, against the AI or with friends on one phone. Cards and sounds are drawn by code."),
                "puces": ["Swift 6", "SpriteKit", L("IA adverse", "AI opponent")],
                "icone": "salon-de-jeu",
                "captures": [],
            },
            {
                "nom": "CardMeet",
                "etiquette": L("App · Réseau · iOS", "App · Networking · iOS"),
                "texte": L("Une carte de visite numérique qu'on échange entre téléphones proches, même sans réseau, avec un App Clip, le scan des cartes papier et six langues.",
                           "A digital business card swapped between nearby phones, even offline, with an App Clip, paper-card scanning and six languages."),
                "puces": ["SwiftUI", "App Clip", "OCR", "vCard 4.0"],
                "icone": "cardmeet",
                "captures": [],
            },
        ],
        "statut_jeux": L("En développement", "In development"),
        "aussi_titre": L("Et aussi", "Also"),
        "aussi": [
            {"nom": "Fléchés du Jour", "icone": "fleches-du-jour", "texte": L("Des mots fléchés générés chaque jour", "Arrow-word puzzles generated daily")},
            {"nom": "Familles du Jour", "icone": "familles-du-jour", "texte": L("16 mots à ranger en 4 familles", "Sort 16 words into 4 groups")},
            {"nom": "Grille Foot", "icone": "grille-foot", "texte": L("Une grille de culture foot 3 × 3", "A 3 × 3 football trivia grid")},
            {"nom": "Le Tirage", "icone": "le-tirage", "texte": L("Le défi des chiffres et des lettres", "A daily numbers-and-letters challenge")},
            {"nom": "Sur le Front", "icone": "sur-le-front", "texte": L("Faire deviner en inclinant le téléphone", "A tilt-the-phone guessing party game")},
            {"nom": "Dépar'tle", "icone": "departle", "texte": L("Retrouver le département français", "Guess the French département")},
            {"nom": "Ciné du Jour", "icone": "cine-du-jour", "texte": L("Deviner le film à partir d'indices", "Guess the film from clues")},
            {"nom": "Mots Mêlés", "icone": "mots-meles", "texte": L("Des mots mêlés quotidiens, 16 thèmes", "Daily word search, 16 themes")},
            {"nom": "Peloton", "icone": "peloton", "texte": L("Manager d'une course cycliste rétro", "Retro cycling stage-race manager")},
            {"nom": "Atouts", "icone": "atouts", "texte": L("Un roguelike autour de la belote", "A belote card roguelike")},
            {"nom": "Cosmos Tycoon", "icone": "cosmos-tycoon", "texte": L("Un jeu de gestion spatial", "A space idle game")},
            {"nom": L("Et deux prototypes", "And two prototypes"), "icone": None, "texte": L("Bataille navale en ligne, Numo (calcul mental)", "Online battleship, Numo (mental maths)")},
        ],
    },
    "ecole": {
        "etiquette": L("Projets d'ingénierie", "Engineering projects"),
        "titre": L("À l'école", "At school"),
        "texte": L("À l'ICAM, on apprend par projets (PBL) : un problème concret, une équipe, quelques semaines.",
                   "At ICAM, we learn through projects (PBL): a real problem, a team, a few weeks."),
        "liste": [
            {"titre": L("Drone stabilisé", "Self-stabilising drone"), "texte": L("Stabilisation automatique avec Arduino, capteurs inertiels et à effet Hall, commande PWM.", "Automatic stabilisation with Arduino, inertial and Hall-effect sensors, PWM control."), "code": "EEE PBL2"},
            {"titre": L("Commande de moteur", "Motor control"), "texte": L("Une commande PWM analogique avec un pont en H L298, à la place d'un Arduino.", "Analog PWM control with an L298 H-bridge, replacing an Arduino."), "code": "EEE PBL4"},
            {"titre": L("Ampli réparé", "Amplifier repair"), "texte": L("Diagnostic et réparation d'un module d'amplification, simulé sous LTspice.", "Diagnosing and repairing an amplifier module, simulated in LTspice."), "code": "EEE PBL3"},
            {"titre": L("Poutre de pare-chocs", "Bumper beam"), "texte": L("Choix d'un composite en fibre de carbone à l'aide des diagrammes d'Ashby.", "Choosing a carbon-fibre composite with Ashby charts."), "code": "PL10"},
            {"titre": "TriBac", "texte": L("Une application iOS avec widget, née d'une démarche de design thinking sur le tri des déchets.", "An iOS app with a widget, born from a design-thinking project on waste sorting."), "code": "MEO PBL4"},
            {"titre": L("Ce site", "This website"), "texte": L("Flask, déploiement continu de GitHub vers PythonAnywhere, fond 3D en three.js.", "Flask, continuous deployment from GitHub to PythonAnywhere, a three.js 3D background."), "code": "MIA PBL8"},
        ],
    },
    "parcours": {
        "etiquette": L("Parcours", "Journey"),
        "titre": L("Mon parcours", "My journey"),
        "etapes": [
            {"date": L("Depuis juin 2026", "Since June 2026"), "titre": L("Associé & développeur d'applications", "Shareholder & app developer"), "lieu": "F.B.C.O. SAS · Paris"},
            {"date": L("Mai – juin 2026", "May – June 2026"), "titre": L("Stage · développeur d'applications", "Internship · app developer"), "lieu": L("ATHIS · Paris 7e · réécriture d'ATHIS Construction", "ATHIS · Paris · rebuilding ATHIS Construction")},
            {"date": L("Depuis juillet 2025", "Since July 2025"), "titre": L("Division IA", "AI division"), "lieu": L("ADERA-RD · développement d'Adera Scribe", "ADERA-RD · building Adera Scribe")},
            {"date": "2025 – 2031", "titre": L("Cycle ingénieur généraliste", "General engineering degree"), "lieu": L("ICAM Grand Paris Sud · parcours ouvert bachelor international", "ICAM Grand Paris Sud · international bachelor track")},
            {"date": "2024 – 2025", "titre": L("Classe préparatoire PCSI", "PCSI preparatory class"), "lieu": L("Lycée Claude Bernard · Paris", "Lycée Claude Bernard · Paris")},
            {"date": "2024", "titre": L("Baccalauréat", "Baccalauréat"), "lieu": L("Mathématiques et physique-chimie, option maths expertes", "Maths and physics-chemistry, advanced maths option")},
        ],
    },
    "loisirs": {
        "etiquette": L("En dehors du code", "Off the keyboard"),
        "liste": [
            {"titre": L("Football", "Football"), "texte": L("12 ans en club", "12 years in a club")},
            {"titre": "Piano", "texte": L("Pour le plaisir", "For the joy of it")},
            {"titre": L("Sciences", "Science"), "texte": L("Comprendre comment ça marche", "Understanding how things work")},
        ],
    },
    "contact": {
        "etiquette": L("Contact", "Contact"),
        "titre": L("Construisons quelque chose.", "Let's build something."),
        "texte": L("Un projet d'application, un stage, une question ? Écrivez-moi, je réponds vite.",
                   "An app idea, an internship, a question? Drop me a line, I reply fast."),
        "bouton": L("M'écrire", "Email me"),
    },
    "pied": {
        "credit": L("Site fait main · Flask · three.js", "Handmade · Flask · three.js"),
    },
}


def _choisir(valeur, lang):
    """Parcourt le contenu et ne garde que la langue demandée."""
    if isinstance(valeur, dict):
        if set(valeur) == {"fr", "en"}:
            return valeur[lang]
        return {cle: _choisir(v, lang) for cle, v in valeur.items()}
    if isinstance(valeur, list):
        return [_choisir(v, lang) for v in valeur]
    return valeur


def contenu(lang):
    return _choisir(CONTENU, lang)
