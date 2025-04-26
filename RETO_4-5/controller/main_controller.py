from controllers.estudiante_controller import EstudianteController
from controllers.profesor_controller import ProfesorController
from controllers.curso_controller import CursoController
from controllers.horario_controller import HorarioController
from controllers.matricula_controller import MatriculaController

class MainController:
    def __init__(self):
        self.estudiante_controller = EstudianteController()
        self.profesor_controller = ProfesorController()
        self.curso_controller = CursoController()
        self.horario_controller = HorarioController()
        self.matricula_controller = MatriculaController()
    
    def iniciar(self):
        while True:
            print("\n--- SISTEMA DE GESTIÓN DE ACADEMIA ---")
            print("1. Gestión de Estudiantes")
            print("2. Gestión de Profesores")
            print("3. Gestión de Cursos")
            print("4. Gestión de Horarios")
            print("5. Gestión de Matrículas")
            print("6. Reportes y Consultas")
            print("0. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.estudiante_controller.menu_estudiantes()
            elif opcion == "2":
                self.profesor_controller.menu_profesores()
            elif opcion == "3":
                self.curso_controller.menu_cursos()
            elif opcion == "4":
                self.horario_controller.menu_horarios()
            elif opcion == "5":
                self.matricula_controller.menu_matriculas()
            elif opcion == "6":
                self.menu_reportes()
            elif opcion == "0":
                break
            else:
                print("Opción no válida")
    
    def menu_reportes(self):
        while True:
            print("\n--- REPORTES Y CONSULTAS ---")
            print("1. Cursos de un estudiante")
            print("2. Estudiantes en un curso")
            print("3. Horarios de un curso")
            print("4. Cursos de un profesor")
            print("5. Vista general del sistema")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.estudiante_controller.reporte_cursos_estudiante()
            elif opcion == "2":
                self.curso_controller.reporte_estudiantes_curso()
            elif opcion == "3":
                self.curso_controller.reporte_horarios_curso()
            elif opcion == "4":
                self.profesor_controller.reporte_cursos_profesor()
            elif opcion == "5":
                self.vista_general()
            elif opcion == "0":
                break
            else:
                print("Opción no válida")
    
    def vista_general(self):
        # Obtener datos para la vista general
        total_estudiantes = len(self.estudiante_controller.model.obtener_estudiantes())
        total_profesores = len(self.profesor_controller.model.obtener_profesores())
        total_cursos = len(self.curso_controller.model.obtener_cursos())
        
        print("\n--- VISTA GENERAL DEL SISTEMA ---")
        print(f"Estudiantes registrados: {total_estudiantes}")
        print(f"Profesores registrados: {total_profesores}")
        print(f"Cursos ofrecidos: {total_cursos}")
        
        # Mostrar últimos 5 estudiantes
        print("\nÚltimos estudiantes registrados:")
        estudiantes = self.estudiante_controller.model.obtener_estudiantes()[-5:]
        for e in estudiantes:
            print(f"- {e['nombre']} {e['apellido']}")
        
        # Mostrar próximas clases hoy
        # Implementar lógica para obtener clases del día actual