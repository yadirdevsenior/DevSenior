from models.profesor_model import ProfesorModel
from views.profesor_view import ProfesorView

class ProfesorController:
    
    def registrar_profesor(self):
        nombre, apellido, email, telefono, especialidad = self.view.obtener_datos_profesor()
        if nombre and apellido and email:
            profesor_id = self.model.crear_profesor(nombre, apellido, email, telefono, especialidad)
            if profesor_id:
                self.view.mostrar_mensaje("Profesor registrado con éxito")
    
    def listar_profesores(self):
        profesores = self.model.obtener_profesores()
        self.view.mostrar_profesores(profesores)
    
    def reporte_cursos_profesor(self):
        id_profesor = self.view.pedir_id_profesor()
        if id_profesor:
            cursos = self.model.obtener_cursos_profesor(id_profesor)
            self.view.mostrar_cursos_profesor(cursos)