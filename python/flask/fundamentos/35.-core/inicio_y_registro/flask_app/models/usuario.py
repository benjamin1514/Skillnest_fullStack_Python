import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
nombre_regex = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$')

class Usuario:
    def __init__(self, data):
        self.id_usuario = data["id_usuario"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validar_usuario(datos):
        es_valido = True

        if not datos["nombre"].strip():
            flash("El nombre es obligatorio.", "nombre")
            es_valido = False
        elif len(datos["nombre"].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "nombre")
            es_valido = False
        elif not nombre_regex.match(datos["nombre"].strip()):
            flash("El nombre solo puede contener letras.", "nombre")
            es_valido = False

        if not datos["apellido"].strip():
            flash("El apellido es obligatorio.", "apellido")
            es_valido = False
        elif len(datos["apellido"].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "apellido")
            es_valido = False
        elif not nombre_regex.match(datos["apellido"].strip()):
            flash("El apellido solo puede contener letras.", "apellido")
            es_valido = False

        if not datos["email"].strip():
            flash("El email es obligatorio.", "email")
            es_valido = False
        elif not email_regex.match(datos["email"].strip()):
            flash("El email no tiene un formato válido.", "email")
            es_valido = False

        if not datos["password"]:
            flash("La contraseña es obligatoria.", "password")
            es_valido = False
        elif len(datos["password"]) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "password")
            es_valido = False

        if "confirm_password" in datos and datos["password"] != datos["confirm_password"]:
            flash("Las contraseñas no coinciden.", "confirm_password")
            es_valido = False

        return es_valido

    @classmethod
    def guardar(cls, datos):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
        """
        return connectToMySQL("esquema_inicio_sesion").query_db(query, datos)

    @classmethod
    def buscar_por_email(cls, datos):
        query = """
            SELECT * FROM usuarios WHERE email = %(email)s;
        """
        resultado = connectToMySQL("esquema_inicio_sesion").query_db(query, datos)
        if resultado:
            return cls(resultado[0])
        return None

    @classmethod
    def buscar_por_id(cls, datos):
        query = """
            SELECT * FROM usuarios WHERE id_usuario = %(id_usuario)s;
        """
        resultado = connectToMySQL("esquema_inicio_sesion").query_db(query, datos)
        if resultado:
            return cls(resultado[0])
        return None

    @classmethod
    def existe_email(cls, datos):
        query = """
            SELECT id_usuario FROM usuarios WHERE email = %(email)s;
        """
        resultado = connectToMySQL("esquema_inicio_sesion").query_db(query, datos)
        return len(resultado) > 0 if resultado else False