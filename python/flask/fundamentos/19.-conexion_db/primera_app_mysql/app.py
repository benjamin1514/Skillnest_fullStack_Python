# ==========================================================
# SERVIDOR FLASK + MYSQL
# ==========================================================


from flask import Flask, render_template

from mascota import Mascota

from usuarios import Usuarios


# ==========================================================
# CREAR APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    mascotas = Mascota.get_all()
    usuarios = Usuarios.get_all() # O Usuario.get_all() según el nombre de tu clase

    return render_template(
        "index.html",
        mascotas=mascotas,
        usuarios=usuarios
    )

# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)
