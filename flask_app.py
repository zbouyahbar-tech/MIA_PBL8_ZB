# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask, render_template, request

app = Flask(__name__)

# Mes loisirs, utilisés par les pages /presentation et /loisirs
LOISIRS = ["Coder des applications et des jeux", "Le sport", "La musique"]


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return render_template("accueil.html")


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
@app.get("/presentation")
def presentation():
    return render_template("presentation.html", prenom="Zacharie", nom="Bouyahbar",
                           loisirs=LOISIRS)


@app.get("/loisirs")
def loisirs():
    return render_template("loisirs.html", loisirs=LOISIRS)


@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    # Avec un template (et non un f"..."), le HTML envoyé par le visiteur est neutralisé
    return render_template("bonjour.html", prenom=prenom)


@app.get("/calcul")
def calcul():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    op = request.args.get("op", "plus")
    if op == "plus":
        return f"{a} + {b} = {a + b}"
    if op == "moins":
        return f"{a} - {b} = {a - b}"
    if op == "fois":
        return f"{a} × {b} = {a * b}"
    if op == "divise":
        if b == 0:
            return "Division par zéro impossible !"
        return f"{a} ÷ {b} = {a / b}"
    return "Opération inconnue : choisissez op=plus, moins, fois ou divise."


# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
