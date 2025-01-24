from Model.ClienteModelo import ClienteModelo
from Model.MascotaModelo import MascotaModelo
from utils.Validaciones import Validad_telefono
from datetime import datetime

class ClienteController: 
    
    def __init__(self):
        pass
    
    def registrar_cliente_controller(self):
        
        print("\n*****************REGISTRO DE CLIENTE*****************")
        
        nombre= input("Ingrese el nombre del cliente:")
        telefono=input("Ingrese el telefono del cliente:")
        
        while not Validad_telefono(telefono):
            print("Telefono no valido. Intente nuevamente")
            telefono=input("Ingrese el telefono del cliente:")
            
        direccion=input("Ingrese la direccion del cliente:")
        cliente=ClienteModelo(nombre,telefono,direccion)
        
        print("\n*****************REGISTRO DE MASCOTA*****************")
        
        nombre_mascota=input("Ingrese el nombre de la mascota:")
        especie=input("Ingrese la especie de la mascota(perro,gato,etc):")
        raza=input("Ingrese la raza de la mascota:")
        edad=input("Ingrese la edad de la mascota:")
        mascota=MascotaModelo(nombre_mascota,raza,especie,edad)
        cliente.agregar_mascota(mascota)
        cliente.registrar_cliente_model(cliente)
        print(f"\nCliente {nombre} registrado con exito ")
        
    def obtener_clientes_controller(self):
        return ClienteModelo.obtener_clientes()
