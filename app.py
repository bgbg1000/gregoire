from flask import Flask, send_from_directory
from flask import Flask, render_template, request, url_for, flash, redirect, session ,send_from_directory
import random
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index ():
    games=["a","resoveur_equation"]
    return render_template("index.html", games=games)
mb= int(random.randint(1,9))
@app.route("/a", methods=['GET', 'POST'])
def a():
    
    global mb
    result = None
    if request.method == 'POST':
        nb = request.form['nombre']
        if int(nb) == int(mb):
            result = "success"
        else:
            result = "false"
    return render_template("a.html", result=result)

@app.route("/resolveur_equation", methods=["GET", "POST"])
def res_equa():
    x = None
    erreur = None

    if request.method == "POST":
        eq = request.form.get("eq")

        gauche, droite = eq.split("=")

        gauche = gauche.replace("x", "*x")
        droite = droite.replace("x", "*x")

        def calc(expr, x):
            return eval(expr, {"x": x})

        g1 = calc(gauche, 1)
        g0 = calc(gauche, 0)
        d1 = calc(droite, 1)
        d0 = calc(droite, 0)

        a = g1 - g0
        b = g0
        c = d1 - d0
        d = d0

        A = a - c
        B = d - b

        if A == 0:
            erreur = "Aucune solution"
        else:
            x = B / A

    return render_template("b.html", x=x, erreur=erreur)


    

if __name__ == "__main__":

    app.run()













