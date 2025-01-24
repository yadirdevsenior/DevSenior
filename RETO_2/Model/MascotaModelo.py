class MascotaModelo:
    def __init__(self,nombre,raza,especie,edad):
        self.nombre=nombre
        self.raza=raza
        self.especie=especie
        self.edad=edad  
        self.historial_citas=[]
        self.historial_servicios=[]

    def agregar_cita(self,cita):
        self.historial_citas.append(cita)
    
    def agregar_servicio(self,servicio):
        self.historial_servicios.append(servicio)
    def obtener_historial_citas(self):
        return self.historial_citas
    def obtener_historial_servicios(self):
        return self.historial_servicios
    