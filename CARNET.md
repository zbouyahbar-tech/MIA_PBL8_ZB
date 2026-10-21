# 📒 Mon carnet de bord

**Nom :** Bouyahbar

**Prénom :** Zacharie

**Adresse de mon site :** https://zachariebouyahbar.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse :_ Le code est rangé sur GitHub (avec tout l'historique), mais celui qui fabrique vraiment la page, c'est la copie qui tourne sur le serveur de PythonAnywhere. GitHub Actions l'y envoie à chaque commit. Mon ordinateur n'intervient pas.

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Parce que tout est en ligne : le site tourne sur un serveur connecté à Internet. N'importe qui qui tape l'URL envoie une demande à ce serveur, et son navigateur affiche la réponse. Le navigateur suffit, il n'y a rien à installer.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ Le nom de domaine est `www.google.com` et le chemin est `/maps`.

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ Ça veut dire que la page demandée n'existe pas (erreur 404). C'est le serveur qui l'envoie : il a bien reçu la demande, mais il n'a aucune route pour ce chemin. Même chose pour `/Presentation` (avec une majuscule) et `/presentation/` (avec un `/` à la fin) : pour Flask, ce sont d'autres chemins.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Flask refuse de démarrer, avec l'erreur `AssertionError: View function mapping is overwriting an existing endpoint function: accueil`. Ce n'est pas juste une page qui plante : c'est tout le site qui affiche une erreur, tant qu'on n'a pas renommé une des deux fonctions.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie juste du texte avec des balises (on le voit avec « Afficher le code source », Option + Cmd + U sur Safari). Le navigateur lit ces balises et les transforme en vrai titre, texte en gras, liste, image… Même quand j'oublie de fermer une balise, il n'affiche pas d'erreur : il se débrouille.

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ `<h1>` = le titre principal, `<p>` = un paragraphe, `<ul>` = une liste à puces, `<li>` = un élément de cette liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ La balise `<img>` contient l'adresse complète de l'image chez Wikimedia. Mon serveur donne seulement l'adresse : c'est mon navigateur qui va chercher l'image directement sur le serveur de Wikimedia.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Chacun travaille dans son fichier : le développeur s'occupe du Python dans `flask_app.py`, le graphiste modifie le HTML et le CSS sans risquer de casser le code. C'est aussi plus lisible, et on peut réutiliser un même modèle (chez moi, `base.html` contient le menu de toutes les pages).

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Par le serveur. Dans le code source de la page, on lit directement « Zacharie Bouyahbar » et il n'y a plus aucun `{{ prenom }}`. Le navigateur ne reçoit que le résultat final.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML donne la structure et le contenu (titres, paragraphes, liens). Le CSS donne l'apparence (couleurs, police, marges). Je peux changer les couleurs de tout mon site dans `style.css` sans toucher au HTML.

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Au moins 3 : la page HTML, `style.css` et le logo Python (chez Wikimedia). Le navigateur demande aussi tout seul `favicon.ico`, qui n'existe pas sur mon site.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Le navigateur garde le CSS en mémoire (le cache) pour ne pas le retélécharger à chaque page, donc il peut afficher l'ancienne version. Ctrl + F5 (Cmd + Shift + R sur Mac) l'oblige à tout retélécharger.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HyperText Transfer Protocol. Le navigateur envoie la requête, le serveur envoie la réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ 3, parfois 4 : `presentation` (la page HTML, 200), `style.css` (200), `Python-logo-notext.svg` (l'image, chez Wikimedia, 200), et `favicon.ico` (404). Dans mon Access log, on voit que Safari n'a demandé la favicon qu'à ma première visite : ensuite il se souvient qu'elle n'existe pas.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ `200` = OK, tout s'est bien passé. `404` = Not Found : mon site n'a pas d'icône, donc le serveur répond qu'il ne trouve pas le fichier.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Je modifie seulement la copie de la page qui est dans mon navigateur, sur mon ordinateur. Le fichier sur le serveur n'a pas changé : quand je recharge, ou quand quelqu'un d'autre visite le site, le serveur renvoie la version d'origine.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le paramètre s'appelle `search_query` et sa valeur est `chat`.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ Le code fait `int("bonjour")`, et Python ne peut pas transformer « bonjour » en nombre : `ValueError: invalid literal for int() with base 10: 'bonjour'`. Le serveur renvoie alors une erreur 500. Pour l'éviter, il faudrait vérifier la valeur avant de la convertir (par exemple avec un `try` / `except`) et renvoyer un message d'erreur clair au lieu de planter.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ Parce que le visiteur peut glisser du HTML, et même du JavaScript, dans la page : avec `/bonjour/<button>Cliquez-moi`, un vrai bouton apparaissait. Avec un script, quelqu'un pourrait envoyer un lien piégé et voler des informations aux autres visiteurs. Avec un template, les `<` et `>` sont transformés en `&lt;` et `&gt;` : ils s'affichent comme du texte et ne sont plus interprétés.

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ En GET, les données apparaissent dans l'URL (`/salut?prenom=Zacharie&ville=Paris…`). En POST, l'URL reste `/salut` : les données sont dans le corps de la requête (onglet Réseau → Charge utile). Et en POST, si on recharge la page, le navigateur demande s'il faut renvoyer le formulaire.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ Pour une recherche : GET, pour pouvoir copier le lien, le partager ou le mettre en favori. Pour une connexion : POST, pour que le mot de passe n'apparaisse pas dans l'URL, l'historique ou les journaux du serveur.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Non. Elles ne sont pas dans l'URL, mais elles voyagent quand même dans la requête, et on les lit très facilement dans l'onglet Réseau. Ce qui les protège pendant le trajet, c'est le HTTPS (le chiffrement), pas le POST.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ `4xx` : c'est le client qui a fait une mauvaise demande (page qui n'existe pas = 404, page interdite = 403). `5xx` : c'est le serveur qui a un problème, un bug dans le code (comme le 500 avec `a=bonjour`) ou une panne.

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ Quand je vais sur `/home`, le serveur répond `302` avec l'en-tête `Location: /`, sans envoyer de page. Le navigateur lit cet en-tête et refait tout seul une deuxième requête vers `/`. C'est donc le navigateur qui fait la deuxième requête : dans l'onglet Réseau, on en voit bien deux.

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ Quand on tape une adresse en `http://`, le site nous renvoie vers la version `https://`. Ou après une connexion, quand le site nous renvoie vers notre page d'accueil ou notre profil.

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ Mon adresse IP, mon navigateur et mon système (le `User-Agent` dit que je suis sur Safari, sur Mac), et mes langues préférées (`Accept-Language`). Il connaît aussi l'heure de ma visite et la page d'où je viens (`Referer`).

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ À m'afficher directement la page en français (ou à me proposer la version française), sans que j'aie à choisir la langue.

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ `GET /favicon.ico` → `404`, le 21/10/2026 à 12:20 UTC (14:20 à Paris), juste après ma première visite de la page d'accueil. C'est Safari qui a demandé tout seul l'icône de l'onglet, et mon site n'en a pas.

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ Ce n'est pas vraiment anonyme. La navigation privée empêche seulement mon navigateur de garder l'historique et les cookies sur mon ordinateur. Le serveur, lui, voit toujours mon IP, mon navigateur, mes langues… et il note tout dans son journal.

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ Une page HTML est faite pour être affichée à un humain par un navigateur, avec de la mise en forme. Le JSON, ce sont des données brutes (des paires clé : valeur), sans mise en forme, faites pour être lues par un programme (une appli, du JavaScript…). Mon `/api/heure` répond avec le `Content-Type` `application/json`, et non `text/html`.

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ Sur le serveur : le Python de `flask_app.py`, c'est-à-dire la route `/horloge` qui envoie la page, et la route `/api/heure` qui calcule l'heure. Dans le navigateur : le JavaScript entre les balises `<script>`, qui appelle `fetch("/api/heure")` toutes les secondes et remplace le texte. La page n'est jamais rechargée : dans l'onglet Réseau, on voit seulement une petite requête `heure` par seconde.

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ L'appli Météo : elle envoie ma position (ou une ville) à un serveur, et elle reçoit en JSON la température, le ciel et les prévisions, qu'elle affiche ensuite à sa façon.

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ Le navigateur découpe l'adresse : le nom de domaine lui dit à quel serveur parler, et le chemin quelle page demander. Il envoie une requête HTTP (par exemple `GET /presentation`), avec des en-têtes qui donnent son navigateur, ses langues, etc. Sur le serveur, un programme (chez moi Flask) trouve la route qui correspond, exécute le code et fabrique la page HTML, souvent à partir d'un template. Il renvoie une réponse avec un code : 200 si tout va bien, 404 si la page n'existe pas, 302 pour une redirection… Le navigateur lit le HTML, voit qu'il lui faut aussi le CSS et les images, et refait une requête pour chacun. Enfin, il assemble le tout et affiche la page. Et le serveur a tout noté dans son journal.
