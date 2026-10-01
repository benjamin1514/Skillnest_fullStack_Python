from flask_app.config.mysqlconnection import connectToMySQL


class Genero:

  db_name = 'esquema_bookhub'

  def __init__(self, data):
    self.id_genero = data['id_genero']
    self.genero = data['genero']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM generos ORDER BY genero ASC;'
    results = connectToMySQL(cls.db_name).query_db(query)
    generos = []
    if results:
      for row in results:
        generos.append(cls(row))
    return generos