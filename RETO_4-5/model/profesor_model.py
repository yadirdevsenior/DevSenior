from conexion_db import AcademiaDB

class ProfesorModel:
    def __init__(self):
        self.db = AcademiaDB()
        self.connection = self.db.get_connection()
    
    def crear_profesor(self, nombre, apellido, email, telefono=None, especialidad=None):
        query = "INSERT INTO profesores (nombre, apellido, email, telefono, especialidad) VALUES (%s, %s, %s, %s, %s)"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (nombre, apellido, email, telefono, especialidad))
            self.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error al crear profesor: {e}")
            return None
    
    def obtener_profesores(self):
        query = "SELECT * FROM profesores"
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener profesores: {e}")
            return []
    
    def obtener_profesor_por_id(self, id_profesor):
        query = "SELECT * FROM profesores WHERE id_profesor = %s"
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (id_profesor,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener profesor: {e}")
            return None
    
    def obtener_cursos_profesor(self, id_profesor):
        query = "SELECT * FROM cursos WHERE id_profesor = %s"
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (id_profesor,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener cursos del profesor: {e}")
            return []