from models.estudiante_model import EstudianteModel
from views.estudiante_view import EstudianteView

class EstudianteController:
    def __init__(self):
        self.model = EstudianteModel()
        self.view = EstudianteView()
    
    def menu_estudiantes(self):
        while True:
            print("\n--- GESTIÓN DE ESTUDIANTES ---")
            print("1. Registrar nuevo estudiante")
            print("2. Listar todos los estudiantes")
            print("3. Buscar estudiante por ID")
            print("4. Actualizar estudiante")
            print("5. Eliminar estudiante")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.registrar_estudiante()
            elif opcion == "2":
                self.listar_estudiantes()
            elif opcion == "3":
                self.buscar_estudiante()
            elif opcion == "4":
                self.actualizar_estudiante()
            elif opcion == "5":
                self.eliminar_estudiante()
            elif opcion == "0":
                break
            else:
                print("Opción no válida")
    
    def registrar_estudiante(self):
        nombre, apellido, email, telefono, fecha_nac = self.view.obtener_datos_estudiante()
        if nombre and apellido and email:
            estudiante_id = self.model.crear_estudiante(nombre, apellido, email, telefono, fecha_nac)
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
            # Implementar lógica para obtener cursos del estudiante
            pass