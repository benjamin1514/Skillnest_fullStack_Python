from conexion import Conexion

class Usuario: 
    def __init__(self, usuario_id=None, username=None, password=None, email=None, tipo_usuario=None):
        self.usuario_id = usuario_id
        self.username = username
        self.password = password
        self.email = email
        self.tipo_usuario = tipo_usuario
            
            
    @staticmethod
    def validarLogin(username_ingresado, password_ingresado):
        conexion = Conexion.conexion()
        cursor = conexion.cursor()
        
        sql_usuario = """
            SELECT u.id_usuario, u.username, u.password_hash, t.nombre_tipo 
            FROM usuarios u
            JOIN tipo_usuarios t ON u.id_tipo_usuario = t.id_tipo_usuario
            WHERE u.username = %s AND u.deleted = 0
        """
        cursor.execute(sql_usuario, (username_ingresado,))
        resultado = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        
        
        if not resultado:
            return "USUARIO_INCORRECTO"
            
        
        password_bd = resultado[2]
        if password_ingresado != password_bd:
            return "PASSWORD_INCORRECTO"
            
        return Usuario(
            usuario_id=resultado[0], 
            username=resultado[1],   
            tipo_usuario=resultado[3] 
        )

    def regristrar(self):
        conexion = Conexion.conexion()
        cursor = conexion.cursor()
        
        sql = """
                    INSERT INTO 
                    usuarios
                    (username, password_hash, email, id_tipo_usuario) 
                    VALUES 
                    (%s, %s, %s, %s)
            """
            
        valores = (self.username, self.password, self.email, self.tipo_usuario)
        
        cursor.execute(sql, valores)
        conexion.commit()
        
        cursor.close()
        conexion.close()
        
    @staticmethod
    def obtener_todos():
        conexion = Conexion.conexion()
        cursor = conexion.cursor()
        
        # Corregido: u.id_usuario en lugar de u.id
        sql = """
                SELECT u.id_usuario, u.username, t.nombre_tipo
                FROM usuarios u
                INNER JOIN tipo_usuarios t ON u.id_tipo_usuario = t.id_tipo_usuario
                WHERE u.deleted = 0
            """
        
        cursor.execute(sql)
        resultados = cursor.fetchall()
        
        lista_usuarios = []
        for fila in resultados:

            usua = Usuario(usuario_id=fila[0], username=fila[1], tipo_usuario=fila[2])
            lista_usuarios.append(usua)
            
        cursor.close()
        conexion.close()
        return lista_usuarios
    
    @staticmethod
    def buscar_por_id(id_buscar):
        conexion = Conexion.conexion()
        cursor = conexion.cursor()
        
        sql = """
                SELECT u.id_usuario, u.username, t.nombre_tipo
                FROM usuarios u
                INNER JOIN tipo_usuarios t ON u.id_tipo_usuario = t.id_tipo_usuario
                WHERE u.id_usuario = %s AND u.deleted = 0
            """
        
        cursor.execute(sql, (id_buscar,))
        resultado = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        
        if resultado:
            # Retornamos una instancia de la clase mapeada con los datos
            return Usuario(usuario_id=resultado[0], username=resultado[1], tipo_usuario=resultado[2])
        
        return None
    
    def modificar(self):
        conexion = Conexion.conexion()
        cursor = conexion.cursor()
        
        sql = "UPDATE usuarios SET username = %s, password_hash = %s WHERE id = %s"
        valores = (self.username, self.password, self.usuario_id)
        
        cursor.execute(sql, valores)
        conexion.commit()
        
        cursor.close()
        conexion.close()
        
    @staticmethod
    def eliminar(id_eliminar):
        conexion = Conexion.conexion()
        cursor = conexion.cursor()
        
        # Aplicamos borrado lógico cambiando el estado de la auditoría 'deleted'
        sql = "UPDATE usuarios SET deleted = 1 WHERE id_usuario = %s"
        
        cursor.execute(sql, (id_eliminar,))
        conexion.commit()
        
        # El cursor devuelve cuántas filas fueron afectadas
        filas_afectadas = cursor.rowcount
        
        cursor.close()
        conexion.close()
        
        # Si afectó a más de 0 filas, significa que el ID existía y se marcó como eliminado
        return filas_afectadas > 0
        
    