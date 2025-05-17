from models.matricula_model import MatriculaModel
from models.estudiante_model import EstudianteModel
from models.curso_model import CursoModel
from views.matricula_view import MatriculaView

class MatriculaController:
    def __init__(self):
        self.model = MatriculaModel()
        self.estudiante_model = EstudianteModel()
        self.curso_model = CursoModel()
        self.view = MatriculaView()
    
    def menu_matriculas(self):
        while True:
            print("\n--- GESTIÓN DE MATRÍCULAS ---")
            print("1. Matricular estudiante en curso")
            print("2. Ver matrículas de estudiante")
            print("3. Ver estudiantes en curso")
            print("4. Eliminar matrícula")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.matricular_estudiante()
            elif opcion == "2":
                self.ver_matriculas_estudiante()
            elif opcion == "3":
                self.ver_estudiantes_curso()
            elif opcion == "4":
                self.eliminar_matricula()
            elif opcion == "0":
                break
            else:
                print("Opción no válida")
    
    def matricular_estudiante(self):
        id_estudiante = self.view.pedir_id_estudiante()
        id_curso = self.view.pedir_id_curso()
        
        if id_estudiante and id_curso:
            # Verificar que existan ambos
            estudiante = self.estudiante_model.obtener_estudiante_por_id(id_estudiante)
            curso = self.curso_model.obtener_curso_por_id(id_curso)
            
            if not estudiante:
                self.view.mostrar_mensaje("Estudiante no encontrado")
                return
            
            if not curso:
                self.view.mostrar_mensaje("Curso no encontrado")
                return
            
            matricula_id = self.model.matricular_estudiante(id_estudiante, id_curso)
            if matricula_id:
                self.view.mostrar_mensaje(f"Estudiante {estudiante['nombre']} matriculado en {curso['nombre_curso']} con éxito")
    
    def ver_matriculas_estudiante(self):
        id_estudiante = self.view.pedir_id_estudiante()
        if id_estudiante:
            matriculas = self.model.obtener_matriculas_estudiante(id_estudiante)
            estudiante = self.estudiante_model.obtener_estudiante_por_id(id_estudiante)
            if estudiante:
                self.view.mostrar_matriculas_estudiante(matriculas, estudiante)
    
    def ver_estudiantes_curso(self):
        id_curso = self.view.pedir_id_curso()
        if id_curso:
            estudiantes = self.model.obtener_estudiantes_curso(id_curso)
            curso = self.curso_model.obtener_curso_por_id(id_curso)
            if curso:
                self.view.mostrar_estudiantes_curso(estudiantes, curso)
    
    def eliminar_matricula(self):
        id_matricula = self.view.pedir_id_matricula()
        if id_matricula:
            if self.model.eliminar_matricula(id_matricula):
                self.view.mostrar_mensaje("Matrícula eliminada con éxito")
            else:
                self.view.mostrar_mensaje("Error al eliminar matrícula")