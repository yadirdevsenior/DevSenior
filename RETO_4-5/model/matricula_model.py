from conexion_db import AcademiaDB

class MatriculaModel:
    def __init__(self):
        self.db = AcademiaDB()
        self.connection = self.db.get_connection()
    
    def matricular_estudiante(self, id_estudiante, id_curso):
        query = "INSERT INTO matriculas (id_estudiante, id_curso, fecha_matricula) VALUES (%s, %s, CURDATE())"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (id_estudiante, id_curso))
            self.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error al matricular estudiante: {e}")
            return None
    
    def obtener_matriculas_estudiante(self, id_estudiante):
        query = """
        SELECT m.*, c.nombre_curso 
        FROM matriculas m
        JOIN cursos c ON m.id_curso = c.id_curso
        WHERE m.id_estudiante = %s
        """
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (id_estudiante,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener matrículas del estudiante: {e}")
            return []
    
    def obtener_estudiantes_curso(self, id_curso):
        query = """
        SELECT e.* 
        FROM estudiantes e
        JOIN matriculas m ON e.id_estudiante = m.id_estudiante
        WHERE m.id_curso = %s
        """
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (id_curso,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener estudiantes del curso: {e}")
            return []
    
    def eliminar_matricula(self, id_matricula):
        query = "DELETE FROM matriculas WHERE id_matricula = %s"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (id_matricula,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar matrícula: {e}")
            return False