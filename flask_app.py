# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask, render_template, redirect

from contenu import contenu, EMAIL

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return render_template("index.html", t=contenu("fr"), lang="fr", email=EMAIL)


# La même page en anglais : seul le texte change, le template est le même
@app.get("/en")
def accueil_anglais():
    return render_template("index.html", t=contenu("en"), lang="en", email=EMAIL)


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
# Ma présentation et mes loisirs sont maintenant des sections de l'accueil :
# ces anciennes adresses renvoient vers la bonne section.
@app.get("/presentation")
def presentation():
    return redirect("/#apropos")


@app.get("/loisirs")
def loisirs():
    return redirect("/#loisirs")


# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
