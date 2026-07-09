from flask import Flask
app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>¡Hola Mundo!</h1> <br> <p>este es un parrafo</p>"

@app.route("/exito")
def exito():
    return "¡Éxito!"

@app.route("/saludar/<name>")
def saludar(name):
    return f"Hola {name}"

@app.route("/color/<nombre>/<color>")
def color_favorito(nombre, color):

    return f"Hola {nombre}, tu color favorito es {color}"

@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):

    return f"¡Hola {nombre}!" * veces

@app.route("/producto/<int:id>")
def producto(id):
    
    sql = """
            SELECT *
            FROM productos
            WHERE id = 15;
        """
@app.route("/despedida/<nombre>")
def despedida(nombre):
    return f"¡Hasta luego {nombre}! ¡Esperamos verte pronto!"

@app.route("/presentacion/<nombre>/<int:edad>")
def presentacion(nombre, edad):
    return f"Hola {nombre}, tienes {edad} años."

@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    sumas = num1 + num2
    return f"La suma es {sumas}"

@app.route("/multiplicacion/<int:num1>/<int:num2>")
def multiplicacion(num1, num2):
    multiplicaciones = num1 * num2
    return f"La Multiplicación es {multiplicaciones}"

@app.route("/paridad/<int:numero>")
def pares(numero):
    if numero % 2 == 0:
        return f"El número {numero} es par"
    else:
        return f"El número {numero} es impar"
    
@app.route("/")
def index():
    pass
    
if __name__ == "__main__":
    app.run(debug=True)
    
    

    
