# ==========================================================
# MODELO MASCOTA
# ==========================================================

from mysqlconnection import connectToMySQL


# ==========================================================
# CLASE MASCOTA
# ==========================================================

class Mascota:
    """
    Representa un registro de la tabla mascotas.
    """

    def __init__(self, data):
        """
        Convierte un diccionario de MySQL en un objeto Mascota.
        """

        self.id = data["id"]

        self.nombre = data["nombre"]

        self.tipo = data["tipo"]

        self.color = data["color"]

        self.created_at = data["created_at"]

        self.updated_at = data["updated_at"]


    # ======================================================
    # OBTENER TODAS LAS MASCOTAS
    # ======================================================

    @classmethod
    def get_all(cls):
        """
        Devuelve todas las mascotas de la base de datos.
        """

        query = """
            SELECT *
            FROM mascotas;
        """


        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query)


        mascotas = []


        for mascota in resultados:

            mascotas.append(
                cls(mascota)
            )


        return mascotas


    # ======================================================
    # OBTENER MASCOTA POR ID
    # ======================================================

    @classmethod
    def get_by_id(cls, id):
        """
        Busca una mascota utilizando su ID.

        El ID recibido desde Python se envía como parámetro
        de una sentencia preparada.
        """

        # --------------------------------------------------
        # QUERY
        # --------------------------------------------------

        query = """
            SELECT *
            FROM mascotas
            WHERE id = %(id_mascota)s;
        """


        # --------------------------------------------------
        # DATOS VARIABLES
        # --------------------------------------------------

        data = {
            "id_mascota": id
        }


        # --------------------------------------------------
        # EJECUTAR CONSULTA
        # --------------------------------------------------

        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(
            query,
            data
        )


        # --------------------------------------------------
        # COMPROBAR RESULTADO
        # --------------------------------------------------

        if resultados:

            return cls(
                resultados[0]
            )


        return None
    
    @classmethod
    def get_by_name(cls, nombre):
        query = """
            SELECT *
            FROM mascotas
            WHERE nombre = %(nombre_mascota)s;
        """
        data = {
            "nombre_mascota": nombre
        }
        
        results = connectToMySQL("primera_flask").query_db(query, data)
        
        # Si la consulta devuelve al menos un registro, retornamos la instancia
        if results:
            return cls(results[0])
        
        # Si no encontró ninguna coincidencia, retornamos None
        return None
    
    @classmethod
    def get_by_tipo(cls, tipo):
        query = """
            SELECT *
            FROM mascotas
            WHERE tipo = %(tipo_mascota)s;
        """
        data = {
            "tipo_mascota": tipo
        }
        
        results = connectToMySQL("primera_flask").query_db(query, data)
        
        # Creamos una lista para almacenar todas las mascotas encontradas
        mascotas = []
        
        if results:
            for fila in results:
                mascotas.append(cls(fila))
                
        return mascotas  # 👈 Retorna una lista [], ideal para el {% for %} en Jinja2
