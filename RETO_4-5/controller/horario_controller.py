from models.horario_model import HorarioModel
from views.horario_view import HorarioView

class HorarioController:
    def __init__(self):
        self.model = HorarioModel()
        self.view = HorarioView()
    
    def menu_horarios(self):
        while True:
            print("\n--- GESTIÓN DE HORARIOS ---")
            print("1. Agregar horario a curso")
            print("2. Ver horarios de un curso")
            print("3. Ver horarios por día")
            print("4. Actualizar horario")
            print("5. Eliminar horario")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.agregar_horario()
            elif opcion == "2":
                self.ver_horarios_curso()
            elif opcion == "3":
                self.ver_horarios_dia()
            elif opcion == "4":
                self.actualizar_horario()
            elif opcion == "5":
                self.eliminar_horario()
            elif opcion == "0":
                break
            else:
                print("Opción no válida")
    
    def agregar_horario(self):
        id_curso, dia_semana, hora_inicio, hora_fin = self.view.obtener_datos_horario()
        if id_curso and dia_semana and hora_inicio and hora_fin:
            horario_id = self.model.agregar_horario(id_curso, dia_semana, hora_inicio, hora_fin)
            if horario_id:
                self.view.mostrar_mensaje("Horario agregado con éxito")
    
    def ver_horarios_curso(self):
        id_curso = self.view.pedir_id_curso()
        if id_curso:
            horarios = self.model.obtener_horarios_curso(id_curso)
            self.view.mostrar_horarios(horarios)
    
    def ver_horarios_dia(self):
        dia = self.view.pedir_dia_semana()
        if dia:
            horarios = self.model.obtener_horarios_dia(dia)
            self.view.mostrar_horarios(horarios, f"Horarios del {dia}")
    
    def actualizar_horario(self):
        id_horario = self.view.pedir_id_horario()
        if id_horario:
            # Implementar lógica para actualizar horario
            pass
    
    def eliminar_horario(self):
        id_horario = self.view.pedir_id_horario()
        if id_horario:
            # Implementar lógica para eliminar horario
            pass