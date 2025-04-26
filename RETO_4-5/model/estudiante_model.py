from conexion_db import AcademiaDB
class EstudianteModel:
    def __init__(self):
        self.db = AcademiaDB()
        self.connection = self.db.get_connection()
    
    def crear_estudiante(self, nombre, apellido, email, telefono=None, fecha_nacimiento=None):
        query = "INSERT INTO estudiantes (nombre, apellido, email, telefono, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s)"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (nombre, apellido, email, telefono, fecha_nacimiento))
            self.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error al crear estudiante: {e}")
            return None
    
    def obtener_estudiantes(self):
        query = "SELECT * FROM estudiantes"
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener estudiantes: {e}")
            return []
    
    def obtener_estudiante_por_id(self, id_estudiante):
        query = "SELECT * FROM estudiantes WHERE id_estudiante = %s"
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (id_estudiante,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener estudiante: {e}")
            return None
    