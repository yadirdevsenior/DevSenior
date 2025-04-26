from models.curso_model import CursoModel
from views.curso_view import CursoView

class CursoController:
    def __init__(self):
        self.model = CursoModel()
        self.view = CursoView()
    
    def menu_cursos(self):
        while True:
            print("\n--- GESTIÓN DE CURSOS ---")
            print("1. Registrar nuevo curso")
            print("2. Listar todos los cursos")
            print("3. Buscar curso por ID")
            print("4. Actualizar curso")
            print("5. Eliminar curso")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.registrar_curso()
            elif opcion == "2":
                self.listar_cursos()
            elif opcion == "3":
                self.buscar_curso()
            elif opcion == "4":
                self.actualizar_curso()
            elif opcion == "5":
                self.eliminar_curso()
            elif opcion == "0":
                break
            else:
                print("Opción no válida")
    
    def registrar_curso(self):
        nombre, descripcion, duracion, id_profesor = self.view.obtener_datos_curso()
        if nombre and id_profesor:
            curso_id = self.model.crear_curso(nombre, descripcion, duracion, id_profesor)
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