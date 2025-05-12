from model.database.conexion_db import ConexionDB
from model.entidades.horario import Horario

class HorarioModel:
    def __init__(self, horario = Horario):
        self.db = ConexionDB()
        self.connection = self.db.get_conexion()
        self.horario = horario
    
    def agregar_horario(self):
        query = "INSERT INTO horarios (id_curso, dia_semana, hora_inicio, hora_fin) VALUES (%s, %s, %s, %s)"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (self.horario.id_curso,
                                   self.horario.dia_semana,
                                   self.horario.hora_inicio,
                                   self.horario.hora_fin))
            self.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error al agregar horario: {e}")
            return None
    
    def obtener_horarios_curso(self, id_curso):
        query = "SELECT * FROM horarios WHERE id_curso = %s ORDER BY dia_semana, hora_inicio"
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (id_curso,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener horarios: {e}")
            return []
    
    def obtener_horarios_dia(self, dia_semana):
        query = """
        SELECT h.*, c.nombre_curso, p.nombre as nombre_profesor, p.apellido as apellido_profesor
        FROM horarios h
        JOIN cursos c ON h.id_curso = c.id_curso
        JOIN profesores p ON c.id_profesor = p.id_profesor
        WHERE h.dia_semana = %s
        ORDER BY h.hora_inicio
        """
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (dia_semana,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener horarios del día: {e}")
            return []