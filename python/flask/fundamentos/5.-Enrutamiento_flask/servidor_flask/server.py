from flask import Flask

app = Flask(__name__)

# Ruta válida para la página de inicio
@app.route('/')
def inicio():
    return "<h1>¡Bienvenido al Servidor!</h1><p>Esta es una ruta válida funcionando correctamente.</p>"

@app.route('/exito')
def exito():    
    return "<h1>¡Éxito!</h1><p>Has accedido a una ruta válida.</p>"

# Manejador de error 404 personalizado (Partes 1, 2 y 5)
@app.errorhandler(404)
def pagina_no_encontrada(error):
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>404 - Página No Encontrada</title>
    </head>
    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #282c34; color: #ffffff; text-align: center; padding: 50px;">
        <h1 style="color: #ff6b6b; font-size: 3em;">⚠️ 404 - Página no encontrada</h1>
        
        <p style="font-size: 1.3em; color: #abb2bf;">
            Lo sentimos, el recurso solicitado no existe. Se lo llevaron los duendes del servidor 🧙‍♂️.
        </p>

        <blockquote style="font-style: italic; color: #e5c07b; margin: 30px auto; max-width: 500px; border-left: 4px solid #e5c07b; padding-left: 15px;">
            "No todos los que vagan están perdidos... pero en esta URL definitivamente sí."
        </blockquote>

        <a href="/" style="display: inline-block; margin-top: 20px; padding: 12px 24px; background-color: #98c379; color: #282c34; text-decoration: none; font-weight: bold; border-radius: 6px;">
            👈 Volver al inicio
        </a>
    </body>
    </html>
    """
    # Se devuelve el contenido HTML junto con el código HTTP 404
    return html_content, 404

if __name__ == "__main__":
    app.run(debug=True)