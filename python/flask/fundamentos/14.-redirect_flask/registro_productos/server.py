from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    """
    Muestra el formulario de creación de usuario.
    """

    return render_template("index.html")

@app.route("/registrar", methods=["POST"])
def crear_usuario():
    """
    Recibe la información enviada mediante POST.

    Esta función se encarga de procesar los datos
    antes de realizar la redirección.
    """

    # ------------------------------------------
    # Obtener los datos enviados por el formulario
    # ------------------------------------------

    nombre = request.form["nombre"]

    precio = request.form["precio"]
    
    categoria = request.form["categoria"]
    

    # ------------------------------------------
    # Mostrar los datos en la terminal
    # ------------------------------------------

    print("===================================")

    print("Información recibida")

    print(f"Nombre: {nombre}")

    print(f"Precio: {precio}")

    print(f"Categoría: {categoria}")

    print("===================================")

    # ------------------------------------------
    # Redirigir a la página de éxito
    # ------------------------------------------

    return redirect(url_for("resultado"))

@app.route("/resultado")
def resultado():
    """
    Muestra un mensaje de éxito después de crear el usuario.
    """

    return render_template("resultado.html")

@app.route("/ayuda")
def ayuda():
    """
    Muestra la página de ayuda.
    """
    return render_template("ayuda.html")

if __name__ == "__main__":
    app.run(debug=True)