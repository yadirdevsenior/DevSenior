from model.database.conexion_db import ConexionDB
from model.entidades.curso import Curso

class CursoModel:
    def __init__(self, curso = Curso):
        self.db = ConexionDB()
        self.connection = self.db.get_conexion()
        self.curso = curso
        
    def crear_curso(self):
        query = "INSERT INTO cursos (nombre, descripcion, id_profesor) VALUES (%s, %s, %s)"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (self.curso.nombre,
                                   self.curso.descripcion,
                                   self.curso.id_profesor
                                   ))
            self.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error al crear curso: {e}")
            return None
    
    def obtener_cursos(self):
        query = """
        SELECT c.*, p.nombre as nombre_profesor, p.apellido as apellido_profesor 
        FROM cursos c
        JOIN profesores p ON c.id_profesor = p.id_profesor
        """
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener cursos: {e}")
            return []
    
    def obtener_curso_por_id(self, id_curso):
        query = """
        SELECT c.*, p.nombre as nombre_profesor, p.apellido as apellido_profesor 
        FROM cursos c
        JOIN profesores p ON c.id_profesor = p.id_profesor
        WHERE c.id_curso = %s
        """
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (id_curso,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener curso: {e}")
            return None