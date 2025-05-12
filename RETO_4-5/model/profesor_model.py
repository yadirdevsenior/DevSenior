from model.database.conexion_db import ConexionDB
from model.entidades.profesor import Profesor

class ProfesorModel:
    def __init__(self, profesor = Profesor):
        self.db = ConexionDB()
        self.profesor = profesor
        self.connection = self.db.get_conexion()
    
    def crear_profesor(self):
        query = "INSERT INTO profesores (nombre, correo, especialidad) VALUES (%s, %s, %s)"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (self.profesor.nombre, 
                                   self.profesor.correo,
                                   self.profesor.especialidad
                                   ))
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