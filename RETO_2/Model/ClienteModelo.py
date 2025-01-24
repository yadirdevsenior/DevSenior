from Model.ClasesAbstractas.PersonaModelo import PersonaModelo

class ClienteModelo(PersonaModelo):

    clientes = []

    def __init__(self,nombre,telefono,direccion):
        super().__init__(nombre,telefono,direccion)
        self.mascotas=[]
        
    def registrar_cliente_model(self, cliente):
        self.clientes.append(cliente)
        
    def agregar_mascota(self,mascota):
        self.mascotas.append(mascota)
        
    def obtener_clientes(self):
        return self.clientes

    def mostrar_info(self):
        print(f"Nombre: {self._nombre} \nTelefono: {self._telefono} \nDireccion: {self._direccion}")
