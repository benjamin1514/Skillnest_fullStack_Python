from flask import Flask, render_template

app = Flask(__name__)

# Agregadas las propiedades 'nivel' y 'pais'
jugadores = [
    {"nombre": "CyberWarrior", "puntaje": 9100, "nivel": 45, "pais": "Chile"},
    {"nombre": "ShadowNinja", "puntaje": 8200, "nivel": 38, "pais": "México"},
    {"nombre": "PixelMaster", "puntaje": 7500, "nivel": 30, "pais": "Argentina"},
    {"nombre": "AlexGamer", "puntaje": 5000, "nivel": 22, "pais": "España"},
    {"nombre": "UltraNoob", "puntaje": 3000, "nivel": 5, "pais": "Colombia"}
]

@app.route("/ranking")
def ranking():
    return render_template("ranking.html", jugadores=jugadores, color=None)

@app.route("/ranking/<int:cantidad>")
def ranking_limitado(cantidad):
    return render_template("ranking.html", jugadores=jugadores[:cantidad], color=None)

@app.route("/ranking/<int:cantidad>/<color>")
def ranking_color(cantidad, color):
    return render_template("ranking.html", jugadores=jugadores[:cantidad], color=color)

if __name__ == "__main__":
    app.run(debug=True)