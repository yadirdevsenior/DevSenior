from Model.MascotaModelo import MascotaModelo
from Model.ClienteModelo import ClienteModelo

class MascotaController:
    def __init__(self):
        self.cliente_modelo = ClienteModelo("", "", "")
    
    def registrar_mascota(self):
        print("\n--Registro de la mascota---")
        clientes = self.cliente_modelo.obtener_clientes()
        if not clientes:
            print("No hay clientes registrados.")
            return

        nombre_cliente = input("Ingrese el nombre del propietario: ")
        cliente = next((c for c in clientes if c._nombre == nombre_cliente), None)

        if cliente:
            nombre_mascota = input("Ingrese el nombre de la mascota: ")
            especie = input("Ingrese la especie de la mascota (perro, gato, etc.): ")
            raza = input("Ingrese la raza de la mascota: ")
            edad = input("Ingrese la edad de la mascota: ")
            mascota = MascotaModelo(nombre_mascota, raza, especie, edad)
            cliente.agregar_mascota(mascota)
            print(f"Mascota '{nombre_mascota}' registrada para el cliente '{nombre_cliente}' con éxito.")
        else:
            print("Cliente no encontrado.")
