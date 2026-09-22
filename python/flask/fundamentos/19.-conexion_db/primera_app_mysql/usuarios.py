from mysqlconnection import connectToMySQL

class Usuarios:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.correo = data["correo"]
        self.edad = data["edad"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL("primera_flask").query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append(cls(usuario))
        return usuarios