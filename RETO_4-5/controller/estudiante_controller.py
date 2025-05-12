from model.entidades.estudiante import Estudiante
from model.estudiante_model import EstudianteModel

class EstudianteController:
    
    def registrar_estudiante(self, nombre, correo, fecha_nacimiento):
        id = None
        insert_estudiante = Estudiante(id, nombre, correo, fecha_nacimiento)
        self.model = EstudianteModel(insert_estudiante)
        
        estudiante_id = self.model.crear_estudiante()
        if estudiante_id:
            self.view.mostrar_mensaje("Estudiante registrado con éxito")
    
    def listar_estudiantes(self):
        estudiantes = self.model.obtener_estudiantes()
        self.view.mostrar_estudiantes(estudiantes)
    
    def buscar_estudiante(self):
        id_estudiante = self.view.pedir_id_estudiante()
        if id_estudiante:
            estudiante = self.model.obtener_estudiante_por_id(id_estudiante)
            if estudiante:
                self.view.mostrar_estudiante(estudiante)
            else:
                self.view.mostrar_mensaje("Estudiante no encontrado")
    
    def reporte_cursos_estudiante(self):
        id_estudiante = self.view.pedir_id_estudiante()
        if id_estudiante:
            pass