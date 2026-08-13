from flask import Flask, render_template, redirect, url_for 

app = Flask(__name__)


@app.route("/")
def inicio():
    return redirect(url_for("ranking"))

jugadores = [

    {
        "nombre": "AlexGamer",
        "puntaje": 5000,
        "pais": "México",
        "nivel": "Intermedio"
    },

    {
        "nombre": "PixelMaster",
        "puntaje": 7500,
        "pais": "Colombia",
        "nivel": "Avanzado"
    },

    {
        "nombre": "ShadowNinja",
        "puntaje": 8200,
        "pais": "Argentina",
        "nivel": "Avanzado"
    },

    {
        "nombre": "CyberWarrior",
        "puntaje": 9100,
        "pais": "Chile",
        "nivel": "Experto"
    },

    {
        "nombre": "UltraNoob",
        "puntaje": 3000,
        "pais": "México",
        "nivel": "Principiante"
    }

]

@app.route("/ranking")
def ranking():

    return render_template(

        "ranking.html",

        jugadores=jugadores

    )

if __name__ == "__main__":

    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)