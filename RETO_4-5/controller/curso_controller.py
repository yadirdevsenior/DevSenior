from model.entidades.curso import Curso
from model.curso_model import CursoModel

class CursoController:
    
    def registrar_curso(self, nombre, descripcion, id_profesor):
        
        insert_curso = Curso(nombre, descripcion, id_profesor)
        self.model = CursoModel(insert_curso)
        
        if nombre and id_profesor:
            curso_id = self.model.crear_curso()
            if curso_id:
                self.view.mostrar_mensaje("Curso creado con éxito")
    
    def reporte_estudiantes_curso(self):
        id_curso = self.view.pedir_id_curso()
        if id_curso:
            # Implementar lógica para obtener estudiantes del curso
            pass
    
    def reporte_horarios_curso(self):
        id_curso = self.view.pedir_id_curso()
        if id_curso:
            # Implementar lógica para obtener horarios del curso
            pass