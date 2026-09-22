# ==========================================================
# SERVIDOR FLASK
# ==========================================================

from flask import Flask, render_template

from mascota import Mascota


# ==========================================================
# CREAR APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    """
    Muestra todas las mascotas.
    """

    mascotas = Mascota.get_all()

    return render_template(
        "index.html",
        mascotas=mascotas
    )


# ==========================================================
# RUTA PARA BUSCAR MASCOTA POR ID
# ==========================================================

@app.route("/mascota/<int:id>")
def mostrar_mascota(id):
    """
    Recibe un ID desde la URL y busca la mascota
    correspondiente en la base de datos.
    """

    mascota = Mascota.get_by_id(id)


    # ------------------------------------------------------
    # Si no existe la mascota, mostramos un mensaje.
    # ------------------------------------------------------

    if mascota is None:

        return "Mascota no encontrada", 404


    # ------------------------------------------------------
    # Mostrar mascota encontrada.
    # ------------------------------------------------------

    return render_template(
        "mascota.html",
        mascota=mascota
    )
    
    
@app.route("/mascota/nombre/<nombre>")
def mostrar_mascota_por_nombre(nombre):
    # Consultamos la base de datos usando el parámetro capturado de la URL
    mascota_encontrada = Mascota.get_by_name(nombre)
    
    return render_template(
        "mascota_detalle.html", 
        mascota=mascota_encontrada, 
        nombre_buscado=nombre
    )
    
@app.route("/mascota/tipo/<tipo>")
def mostrar_mascotas_por_tipo(tipo):
    # Consultamos la base de datos usando el parámetro capturado de la URL
    mascotas_encontradas = Mascota.get_by_tipo(tipo)
    
    return render_template(
        "mascotas_por_tipo.html", 
        mascotas=mascotas_encontradas, 
        tipo_buscado=tipo
    )


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)
