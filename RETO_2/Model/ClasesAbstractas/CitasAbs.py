from abc import ABC, abstractmethod
class CitasAbs:
    def __init__ (self,fecha,hora,servicio,veterinario):
        self.fecha=fecha
        self.hora=hora
        self.servicio=servicio
        self.veterinario=veterinario
     
    @abstractmethod
    def actualizar_cita(self, **kwargs):
        pass

    def mostrar_info(self):
        print(f"Cita:{self.fecha}{self.hora}-{self.servicio}-con {self.veterinario}")
