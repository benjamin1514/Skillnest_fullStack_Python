import pymysql
import pymysql.cursors
import os

class MySQLConnection:
    def __init__(self, db):
        self.connection = pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=db,
            charset='utf8mb4',  # Garantiza soporte para tildes y caracteres especiales
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data or {})
                query_type = query.strip().lower()

                if query_type.startswith("select"):
                    return cursor.fetchall()
                elif query_type.startswith("insert"):
                    return cursor.lastrowid
                else:  # UPDATE, DELETE u otras consultas de modificación
                    return True
            except Exception as e:
                print(f"Error MySQL: {e}")
                return False
            finally:
                self.connection.close()

def connectToMySQL(db=None):
    if db is None:
        db = os.getenv("DB_NAME", "esquema_bookhub")
    return MySQLConnection(db)