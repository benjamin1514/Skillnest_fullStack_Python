import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

# Clave secreta necesaria para usar session en Flask
app.secret_key = "clave_secreta_skillnest"

# Lista de predicciones para el juego
PREDICCIONES = [
    {"tipo": "buena", "texto": "¡Tendrás un éxito gigante en tu próximo examen de programación y tu código funcionará a la primera!"},
    {"tipo": "buena", "texto": "Encontrarás dinero en la calle y te invitarán la comida que más te gusta esta semana."},
    {"tipo": "mala", "texto": "Olvidarás cerrar una comilla en tu código y buscarás el error durante 2 horas."},
    {"tipo": "mala", "texto": "Se te derramará un vaso de agua justo al lado del teclado en un momento crítico."}
]

# 1. Ruta principal: Muestra el formulario
@app.route("/")
def index():
    return render_template("index.html")

# 2. Ruta procesadora: Guarda los datos en la sesión y redirige (Solo POST)
@app.route("/enviar", methods=["POST"])
def enviar():
    # Guardamos en sesión usando la sintaxis tradicional de corchetes []
    session["nombre"] = request.form["nombre"]
    session["signo"] = request.form["signo"]
    session["numero_favorito"] = request.form["numero_favorito"]
    
    # Seleccionamos una predicción al azar y la guardamos en la sesión
    prediccion_elegida = random.choice(PREDICCIONES)
    session["prediccion_texto"] = prediccion_elegida["texto"]
        

    # Redirigimos a la ruta GET
    return redirect(url_for("futuro"))

# 3. Ruta de resultado: Muestra la predicción leída desde la sesión
@app.route("/futuro")
def futuro():
    # Verificación: Si no hay un nombre en la sesión, devolvemos al usuario al inicio
    if "nombre" not in session:
        return redirect(url_for("index"))
        
    return render_template("futuro.html")

if __name__ == "__main__":
    app.run(debug=True)

    