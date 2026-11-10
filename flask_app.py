# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask, render_template, request, redirect, abort, jsonify
from datetime import datetime
from zoneinfo import ZoneInfo

from contenu import contenu, EMAIL

app = Flask(__name__)


def page(template, **variables):
    """Affiche une page de l'atelier avec le menu et le pied du site (en français)."""
    return render_template(template, t=contenu("fr"), lang="fr", email=EMAIL, **variables)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return render_template("index.html", t=contenu("fr"), lang="fr", email=EMAIL, accueil=True)


# La même page en anglais : seul le texte change, le template est le même
@app.get("/en")
def accueil_anglais():
    return render_template("index.html", t=contenu("en"), lang="en", email=EMAIL, accueil=True)


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
# Mes loisirs, utilisés par les pages /presentation et /loisirs (exercices 2 et 4)
LOISIRS = ["Le football, 12 ans en club", "Le piano", "Les sciences"]


# Exercices 2 à 5 : ma page de présentation, fabriquée à partir d'un template
@app.get("/presentation")
def presentation():
    return page("presentation.html", prenom="Zacharie", nom="Bouyahbar", loisirs=LOISIRS)


@app.get("/loisirs")
def loisirs():
    return page("loisirs.html", loisirs=LOISIRS)


# Exercice 7 : une information dans le chemin
@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    # Avec un template (et non un f"..."), le HTML envoyé par le visiteur est neutralisé
    return page("bonjour.html", prenom=prenom)


# Exercice 7 : des paramètres après le "?"
@app.get("/calcul")
def calcul():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
    except ValueError:
        # Sans ce contrôle, int("bonjour") faisait planter le serveur (erreur 500) :
        # on répond plutôt 400, « la demande du client est incorrecte », avec un message clair
        return page("calcul.html", resultat=None), 400
    op = request.args.get("op", "plus")
    if op == "plus":
        resultat = f"{a} + {b} = {a + b}"
    elif op == "moins":
        resultat = f"{a} - {b} = {a - b}"
    elif op == "fois":
        resultat = f"{a} × {b} = {a * b}"
    elif op == "divise":
        resultat = f"{a} ÷ {b} = {a / b:g}" if b != 0 else "Division par zéro impossible !"
    else:
        resultat = "Opération inconnue : choisissez op=plus, moins, fois ou divise."
    return page("calcul.html", resultat=resultat)


# Exercice 8 : les formulaires
@app.get("/formulaire")
def formulaire():
    return page("formulaire.html")


@app.route("/salut", methods=["GET", "POST"])
def salut():
    if request.method == "POST":
        donnees = request.form  # POST : les données sont dans le corps de la requête
    else:
        donnees = request.args  # GET : les données sont dans l'URL, après le "?"
    prenom = donnees.get("prenom") or "inconnu"
    ville = donnees.get("ville") or "nulle part"
    couleur = donnees.get("couleur", "teal")
    # On n'accepte que les couleurs proposées par le formulaire
    if couleur not in ["tomato", "teal", "royalblue"]:
        couleur = "teal"
    return page("salut.html", prenom=prenom, ville=ville, couleur=couleur, methode=request.method)


# Exercice 9 — 3xx : une redirection
@app.get("/home")
def home():
    return redirect("/")


# Exercice 9 — 4xx : un accès interdit
@app.get("/secret")
def secret():
    abort(403)


# Une page d'erreur 404 personnalisée
@app.errorhandler(404)
def page_introuvable(erreur):
    return page("404.html"), 404


# Une page d'erreur 403 personnalisée
@app.errorhandler(403)
def acces_interdit(erreur):
    return page("403.html"), 403


# Exercice 10 : ce que le serveur sait de vous
@app.get("/moi")
def moi():
    return page(
        "moi.html",
        ip=request.headers.get("X-Real-IP", request.remote_addr),
        navigateur=request.headers.get("User-Agent"),
        langues=request.headers.get("Accept-Language"),
        entetes=request.headers,
    )


# Exercice 11 : une API qui répond en JSON
@app.get("/api/heure")
def api_heure():
    maintenant = datetime.now(ZoneInfo("Europe/Paris"))
    return jsonify({
        "heure": maintenant.strftime("%H:%M:%S"),
        "date": maintenant.strftime("%d/%m/%Y"),
        "message": "Bonjour depuis mon API !",
    })


@app.get("/horloge")
def horloge():
    return page("horloge.html")


# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
