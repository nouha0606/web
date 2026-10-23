
from flask import Flask, render_template, request

app = Flask(__name__)


@app.get("/")
def accueil():
    return render_template("accueil.html")


@app.get("/presentation")
def presentation():
    return render_template(
        "presentation.html",
        prenom="Nouha",
        nom="Niri"
    )


@app.get("/loisirs")
def loisirs():
    return "Mes loisirs sont la musique, les voyages et le sport."


@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)


@app.get("/calcul")
def calcul():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
    except ValueError:
        return "Veuillez entrer des nombres entiers valides.", 400

    return f"{a} + {b} = {a + b}"


@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.get("/salut")
def salut():
    prenom = request.args.get("prenom", "inconnu")
    ville = request.args.get("ville", "nulle part")
    return f"Bonjour {prenom}, qui vient de {ville} !"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
