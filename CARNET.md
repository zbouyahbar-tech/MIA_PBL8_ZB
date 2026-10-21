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

   > _Ma réponse :_ 

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ 

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ 

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ 

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ 

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ 

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ 

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ 

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ 

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ 

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ 

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ 

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ 

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ 

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ 

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ 

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ 

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ 

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ 

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ 

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ 
