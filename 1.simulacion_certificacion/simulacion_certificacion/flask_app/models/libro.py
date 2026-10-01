from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Libro:

  db_name = 'esquema_bookhub'

  def __init__(self, data):
    self.id_libro = data['id_libro']
    self.titulo = data['titulo']
    self.autor = data['autor']
    self.descripcion = data['descripcion']
    self.id_genero = data['id_genero']
    self.id_usuario = data['id_usuario']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

    # Atributos adicionales para joins
    self.genero = data.get('genero')
    self.creador_nombre = data.get('creador_nombre')

  @classmethod
  def save(cls, data):
    query = """
            INSERT INTO libros (titulo, autor, descripcion, id_genero, id_usuario)
            VALUES (%(titulo)s, %(autor)s, %(descripcion)s, %(id_genero)s, %(id_usuario)s);
        """
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def get_all_by_user(cls, data):
    """Obtiene los libros agregados a la lista personal del usuario (Mis Libros)"""
    query = """
            SELECT l.*, g.genero, CONCAT(u.nombre, ' ', u.apellido) AS creador_nombre
            FROM usuario_libros ul
            JOIN libros l ON ul.id_libro = l.id_libro
            JOIN generos g ON l.id_genero = g.id_genero
            JOIN usuarios u ON l.id_usuario = u.id_usuario
            WHERE ul.id_usuario = %(id_usuario)s;
        """
    results = connectToMySQL(cls.db_name).query_db(query, data)
    libros = []
    if results:
      for row in results:
        libros.append(cls(row))
    return libros

  @classmethod
  def get_all_community(cls, data):
    """Obtiene los libros de la comunidad que el usuario NO ha agregado a su lista"""
    query = """
            SELECT l.*, g.genero, CONCAT(u.nombre, ' ', u.apellido) AS creador_nombre
            FROM libros l
            JOIN generos g ON l.id_genero = g.id_genero
            JOIN usuarios u ON l.id_usuario = u.id_usuario
            WHERE l.id_libro NOT IN (
                SELECT id_libro FROM usuario_libros WHERE id_usuario = %(id_usuario)s
            );
        """
    results = connectToMySQL(cls.db_name).query_db(query, data)
    libros = []
    if results:
      for row in results:
        libros.append(cls(row))
    return libros

  @classmethod
  def get_by_id(cls, data):
    query = """
            SELECT l.*, g.genero, CONCAT(u.nombre, ' ', u.apellido) AS creador_nombre
            FROM libros l
            JOIN generos g ON l.id_genero = g.id_genero
            JOIN usuarios u ON l.id_usuario = u.id_usuario
            WHERE l.id_libro = %(id_libro)s;
        """
    results = connectToMySQL(cls.db_name).query_db(query, data)
    if not results:
      return False
    return cls(results[0])

  @classmethod
  def add_to_my_list(cls, data):
    """Agrega un libro existente a la lista 'Mis Libros' del usuario"""
    query = """
            INSERT INTO usuario_libros (id_usuario, id_libro)
            VALUES (%(id_usuario)s, %(id_libro)s);
        """
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def remove_from_my_list(cls, data):
    """Quita un libro de la lista personal del usuario"""
    query = """
            DELETE FROM usuario_libros 
            WHERE id_usuario = %(id_usuario)s AND id_libro = %(id_libro)s;
        """
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def update(cls, data):
    query = """
            UPDATE libros 
            SET titulo = %(titulo)s, autor = %(autor)s, descripcion = %(descripcion)s, id_genero = %(id_genero)s
            WHERE id_libro = %(id_libro)s AND id_usuario = %(id_usuario)s;
        """
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def delete(cls, data):
    query = (
        'DELETE FROM libros WHERE id_libro = %(id_libro)s AND id_usuario ='
        ' %(id_usuario)s;'
    )
    return connectToMySQL(cls.db_name).query_db(query, data)

  @staticmethod
  def validar_libro(libro):
    is_valid = True

    if len(libro['titulo'].strip()) < 2:
      flash('El título debe tener al menos 2 caracteres.', 'libro')
      is_valid = False

    if len(libro['autor'].strip()) < 2:
      flash('El autor debe tener al menos 2 caracteres.', 'libro')
      is_valid = False

    if not libro.get('id_genero'):
      flash('Debes seleccionar un género.', 'libro')
      is_valid = False

    if len(libro['descripcion'].strip()) < 5:
      flash('La descripción debe tener al menos 5 caracteres.', 'libro')
      is_valid = False

    return is_valid