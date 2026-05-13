import mysql.connector

class DaoServer:
    def __init__(self):
        # Configuració de la connexió a la BBDD
        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "root",
            "database": "edutask_db"
        }

    def _get_connection(self):
        return mysql.connector.connect(**self.db_config)

    def login(self, username, password):
        try:
            conn = self._get_connection()
            cursor = conn.cursor(dictionary=True)
            # Obtenim l'usuari i el seu rol (1: Professor, 2: Alumne)
            sql = "SELECT id, username, email, id_role FROM Usuarios WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()
            conn.close()
            return user
        except Exception as e:
            print(f"Error DAO Login: {e}")
            return None

    def get_tasques(self):
        try:
            conn = self._get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT t.id, t.titulo, t.descripcion, c.nombre as curso FROM Tareas t JOIN Cursos c ON t.id_curso = c.id"
            cursor.execute(sql)
            tasques = cursor.fetchall()
            conn.close()
            return tasques
        except Exception as e:
            print(f"Error DAO Tasques: {e}")
            return []