import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "clave_secreta_destino"

PREDICCIONES = [
    {
        "tipo": "buena",
        "texto": "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría."
    },
    {
        "tipo": "buena",
        "texto": "Un proyecto importante te traerá gran éxito profesional y financiero este año."
    },
    {
        "tipo": "mala",
        "texto": "Olvidarás cerrar una comilla en tu código y buscarás el error durante 2 horas."
    },
    {
        "tipo": "mala",
        "texto": "Se te derramará un vaso de agua justo al lado del teclado en un momento crítico."
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    # Coincide 100% con los atributos name="..." de index.html
    session["nombre"] = request.form["nombre"]
    session["edad"] = request.form["edad"]
    session["color"] = request.form["color"]
    session["animal"] = request.form["animal"]
    
    # Número aleatorio de la suerte (10 al 99)
    session["numero_suerte"] = random.randint(10, 99)
    
    # Selección de predicción aleatoria
    prediccion = random.choice(PREDICCIONES)
    session["prediccion_texto"] = prediccion["texto"]
    session["prediccion_tipo"] = prediccion["tipo"]

    return redirect(url_for("futuro"))

@app.route("/futuro")
def futuro():
    if "nombre" not in session:
        return redirect(url_for("index"))
    return render_template("futuro.html")

@app.route("/reiniciar")
def reiniciar():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)