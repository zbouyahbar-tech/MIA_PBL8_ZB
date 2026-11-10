# 📒 Mon carnet de bord

**Nom :** Bouyahbar

**Prénom :** Zacharie

**Adresse de mon site :** https://zachariebouyahbar.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse :_ Le code serait à la fois sur GitHub et sur PythonAnywhere, mais ce n'est pas le même rôle, car GitHub ne fait que ranger le code et garder l'historique de chaque commit, alors que c'est le serveur de PythonAnywhere qui exécute ce code à chaque requête pour fabriquer la page, donc le code qui fabrique vraiment ma page se trouve sur PythonAnywhere, et mon ordinateur n'intervient plus du tout une fois le commit envoyé.

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Car mon site ne tourne pas sur mon ordinateur mais sur un serveur allumé en permanence et connecté à Internet, donc dès que mon voisin tape l'adresse, son navigateur envoie une requête à ce serveur qui lui renvoie la page, et c'est pour ça qu'il n'a rien à installer : un site Web serait en fait une « conversation entre le navigateur et le serveur », et un navigateur, tout le monde en a déjà un.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ Dans cette adresse, le nom de domaine est `www.google.com`, car c'est lui qui désigne le serveur à qui le navigateur s'adresse, et le chemin est `/maps`, car c'est lui qui désigne la page demandée à ce serveur.

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ Le serveur a envoyé ce message d'erreur (le code 404) pour dire que ce qui a été recherché n'a pas été trouvé, car il a bien reçu la requête mais il n'a aucune route pour ce chemin, et c'est aussi ce qui se passe avec `/Presentation` ou avec `/presentation/`, ce qui voudrait dire que pour Flask, une seule majuscule ou un seul `/` en plus suffit à faire un chemin complètement différent.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Dans ce cas, Flask refuse tout simplement de démarrer, avec l'erreur `AssertionError: View function mapping is overwriting an existing endpoint function: accueil`, car il ne saurait plus quelle fonction appeler pour quelle route, et donc ce n'est pas une seule page qui plante mais tout le site, tant qu'on n'a pas renommé une des deux fonctions.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur n'envoie que du texte avec des balises, ce qu'on voit avec « Afficher le code source » (Option + Cmd + U sur Safari), mais dès que le navigateur reçoit ce texte, il lit les balises et les transforme en vrai titre, en texte en gras, en liste ou en image, et c'est un fait très intéressant, car même quand j'oublie de fermer une balise, le navigateur n'affiche aucune erreur et se débrouille quand même pour afficher la page.

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ Pour la première, `<h1>` sert au titre principal de la page, puis `<p>` sert à un paragraphe, `<ul>` sert à ouvrir une liste à puces et `<li>` sert à chaque élément de cette liste, donc ces balises ne disent pas à quoi la page doit ressembler mais seulement comment elle est construite.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ Car la balise `<img>` ne contient pas l'image mais seulement son adresse complète chez Wikimedia, ce qui voudrait dire que mon serveur ne fait que donner l'adresse, et que c'est mon navigateur qui envoie lui-même une deuxième requête au serveur de Wikimedia pour aller chercher l'image.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Car si le code Python et le HTML sont séparés, chacun peut travailler dans son propre fichier, le développeur dans `flask_app.py` et le graphiste dans les templates et le CSS, sans risquer de casser le travail de l'autre, et donc non seulement le code serait plus lisible, mais ça serait même plus rapide à faire évoluer, car chez moi le menu n'est écrit qu'une seule fois dans `base.html` et toutes les pages le récupèrent.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Les `{{ prenom }}` sont remplacés par le serveur, car dans le code source de la page on lit directement « Zacharie Bouyahbar » et il n'y a plus aucun `{{ prenom }}`, donc le navigateur ne reçoit que le résultat final et ne voit jamais le template d'origine.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML donne la structure et le contenu de la page (les titres, les paragraphes, les liens), alors que le CSS ne donne que son apparence (les couleurs, la police, les marges), et c'est pour ça que je peux changer les couleurs de tout mon site dans `style.css` sans toucher une seule ligne de HTML.

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Pour la page `/presentation`, le navigateur doit télécharger au moins trois fichiers, la page HTML, `style.css` et le logo Python qui est chez Wikimedia, et il en demande même un quatrième tout seul, `favicon.ico`, qui n'existe pas sur mon site.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Car le navigateur garde le CSS en mémoire (dans le cache) pour ne pas avoir à le retélécharger à chaque page, donc il pourrait continuer à afficher l'ancienne version même après mon commit, et Ctrl + F5 (Cmd + Shift + R sur Mac) l'oblige à tout retélécharger depuis le serveur.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP veut dire HyperText Transfer Protocol, et c'est justement la règle de la « conversation entre le navigateur et le serveur », car c'est le navigateur qui envoie la requête et c'est le serveur qui renvoie la réponse, et jamais l'inverse, car le serveur ne parle que quand on lui pose une question.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ La page `/presentation` a déclenché quatre requêtes, `presentation` (la page HTML, code 200), `style.css` (200), `Python-logo-notext.svg` (l'image chez Wikimedia, 200) et `favicon.ico` (404), mais dans mon Access log on voit que Safari n'a demandé la favicon qu'à ma première visite, ce qui voudrait dire qu'il se souvient ensuite qu'elle n'existe pas et qu'il ne fait plus que trois requêtes.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ Le code `200` veut dire OK, donc que la requête a fonctionné, et le code `404` de la favicon veut dire Not Found, car mon site n'a pas d'icône et le serveur répond donc qu'il ne trouve pas le fichier demandé.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Car je ne modifie que la copie de la page qui est dans mon navigateur, sur mon ordinateur, alors que le fichier sur le serveur, lui, n'a pas changé, donc dès que je recharge la page ou que quelqu'un d'autre la demande, le serveur renvoie la version d'origine.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le paramètre s'appelle `search_query` et sa valeur est `chat`, car tout ce qui se trouve après le `?` est une paire nom=valeur.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ Car le code fait `int("bonjour")` et Python ne peut pas transformer « bonjour » en nombre, donc il lève l'erreur `ValueError: invalid literal for int() with base 10: 'bonjour'` et le serveur renvoie une erreur 500, et pour l'éviter, il faudrait vérifier la valeur avant de la convertir (par exemple avec un `try` / `except`) pour renvoyer un message clair au lieu de planter.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ Car si le serveur affiche tel quel ce que l'utilisateur envoie, l'utilisateur pourrait glisser du HTML et même du JavaScript dans la page, comme le bouton qui apparaissait avec `/bonjour/<button>Cliquez-moi`, et dans ce cas ce que l'utilisateur envoie au site pourrait devenir la cause de la perte du site, car un script pourrait voler les informations des autres visiteurs, alors qu'avec un template, les `<` et `>` sont transformés en `&lt;` et `&gt;` et s'affichent comme du simple texte.

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ En GET, les données apparaissent dans l'URL (`/salut?prenom=Zacharie&ville=Paris…`), alors qu'en POST l'URL reste `/salut` et les données passent dans le corps de la requête, qu'on ne voit que dans l'onglet Réseau (Charge utile), et c'est aussi pour ça qu'en POST, le navigateur demande s'il faut renvoyer le formulaire quand on recharge la page.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ Pour une recherche, je choisirais GET, car on pourrait copier le lien, le partager ou le mettre en favori, et pour une connexion, je choisirais POST, car le mot de passe n'apparaîtrait ni dans l'URL, ni dans l'historique, ni dans le journal du serveur.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Non, car les données ne sont plus dans l'URL mais elles voyagent quand même dans la requête, et on les lit très facilement dans l'onglet Réseau, ce qui reviendrait à dire que le POST cache les données de l'URL mais pas de la requête, et donc ce qui les protège vraiment pendant le trajet, c'est le HTTPS, pas le POST.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ Si on reprend la grille des familles de codes (2xx pour un succès, 3xx pour une redirection, 4xx pour une erreur du client et 5xx pour une erreur du serveur), une erreur 4xx voudrait dire que c'est le client qui a fait une mauvaise demande, comme une page qui n'existe pas (404) ou une page interdite (403), alors qu'une erreur 5xx voudrait dire que c'est le serveur qui est fautif, à cause d'un bug dans le code, comme le 500 de `/calcul?a=bonjour`, ou d'une panne.

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ Quand je vais sur `/home`, le serveur ne renvoie pas de page mais seulement le code `302` avec l'en-tête `Location: /`, et dès que le navigateur lit cet en-tête, il refait tout seul une deuxième requête vers `/`, donc c'est le navigateur qui fait la deuxième requête, et on voit bien les deux dans l'onglet Réseau.

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ Quand on tape une adresse en `http://`, le site nous renvoie vers sa version en `https://`, et c'est aussi une redirection qui nous renvoie vers notre page de profil juste après une connexion.

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ Sans que j'aie rien rempli, le serveur connaît mon adresse IP, mon navigateur et mon système (le `User-Agent` dit que je suis sur Safari, sur Mac) et mes langues préférées (`Accept-Language`), et il connaît même l'heure de ma visite et la page d'où je viens (`Referer`).

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ Dans le cas de Wikipédia, cet en-tête pourrait servir à m'afficher directement la page en français, ou à me proposer la version française, car le site saurait déjà quelle langue je préfère sans que j'aie à la choisir moi-même.

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ Dans mon Access log, la requête `GET /favicon.ico` a reçu un code `404` le 21/10/2026 à 12:20 UTC (14:20 à Paris), juste après ma première visite de la page d'accueil, car c'est Safari qui a demandé tout seul l'icône de l'onglet, et mon site n'en a pas.

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ Après cet exercice, la navigation anonyme n'aurait d'anonyme que le nom, car la navigation privée empêche seulement mon navigateur de garder l'historique et les cookies sur mon ordinateur, mais le serveur, lui, voit toujours mon IP, mon navigateur et mes langues, et il note tout dans son journal, et c'est là que tout se joue : elle est anonyme pour mon ordinateur mais pas du tout pour le serveur.

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ Une page HTML est faite pour être affichée à un humain par un navigateur, avec des titres et de la mise en forme, alors qu'une réponse JSON ne contient que des données brutes (des paires clé : valeur), faites pour être lues par un programme, comme mon `/api/heure` qui répond avec le `Content-Type` `application/json` au lieu de `text/html`.

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ Sur le serveur, c'est le Python de `flask_app.py` qui s'exécute, avec la route `/horloge` qui envoie la page et la route `/api/heure` qui calcule l'heure, alors que dans le navigateur, c'est le JavaScript entre les balises `<script>` qui s'exécute, car c'est lui qui appelle `fetch("/api/heure")` toutes les secondes et qui remplace le texte, donc la page n'est jamais rechargée et on ne voit dans l'onglet Réseau qu'une petite requête `heure` par seconde.

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ L'application Météo utiliserait une API, car elle envoie ma position ou une ville à un serveur, et elle reçoit en JSON la température, le ciel et les prévisions, qu'elle affiche ensuite à sa façon.

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ Donc finalement, quand on tape une adresse, le navigateur découpe l'URL, car le nom de domaine lui dit à quel serveur parler et le chemin quelle page demander, puis il envoie une requête HTTP avec ses en-têtes, et le serveur trouve la route qui correspond, exécute le code, fabrique la page HTML à partir d'un template et renvoie une réponse avec un code (200, 302, 404…), et dès que le navigateur lit cette page, il refait une requête pour chaque fichier dont elle a besoin, le CSS et les images, avant de tout assembler et d'afficher la page, donc afficher une page Web est bien une « conversation entre le navigateur et le serveur ».
>
> D'autres services pourraient être aussi qualifiés de « conversation entre le navigateur et le serveur », comme l'API de GitHub, qui a donc comme mon site des requêtes et des réponses, mais qui répond en JSON et qui renvoie par exemple, sur mon profil, le nombre de mes dépôts publics (trois).
