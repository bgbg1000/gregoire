from flask import Flask, send_from_directory
from flask import Flask, render_template, request, url_for, flash, redirect, session ,send_from_directory
import random
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index ():
    games=["a","b","c"]
    return render_template("index.html", games=games)
mb= int(random.randint(1,3))
print(mb)
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
    

if __name__ == "__main__":

    app.run()
