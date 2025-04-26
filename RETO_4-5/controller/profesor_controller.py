from models.profesor_model import ProfesorModel
from views.profesor_view import ProfesorView

class ProfesorController:
    def __init__(self):
        self.model = ProfesorModel()
        self.view = ProfesorView()
    
    def menu_profesores(self):
        while True:
            print("\n--- GESTIÓN DE PROFESORES ---")
            print("1. Registrar nuevo profesor")
            print("2. Listar todos los profesores")
            print("3. Buscar profesor por ID")
            print("4. Actualizar profesor")
            print("5. Eliminar profesor")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.registrar_profesor()
            elif opcion == "2":
                self.listar_profesores()
            elif opcion == "3":
                self.buscar_profesor()
            elif opcion == "4":
                self.actualizar_profesor()
            elif opcion == "5":
                self.eliminar_profesor()
            elif opcion == "0":
                break
            else:
                print("Opción no válida")
    
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