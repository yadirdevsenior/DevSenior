from model.database.conexion_db import ConexionDB
from model.entidades.estudiante import Estudiante
class EstudianteModel:
    def __init__(self, estudiante = Estudiante):
        self.db = ConexionDB()
        self.estudiante = estudiante
        self.connection = self.db.get_conexion()
    
    def crear_estudiante(self):
        query = "INSERT INTO estudiantes (nombre, correo, fecha_nacimiento) VALUES (%s, %s, %s)"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (self.estudiante.nombre, 
                                   self.estudiante.correo, 
                                   self.estudiante.fecha_nacimiento
                                   ))
            
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
    