from models.horario_model import HorarioModel
from views.horario_view import HorarioView

class HorarioController:
    
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