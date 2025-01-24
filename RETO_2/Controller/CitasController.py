from Model.CitasModelo import CitasModelo
from Model.ClienteModelo import ClienteModelo
from utils.Validaciones import validar_fecha,validar_hora
from datetime import datetime

class CitasController:
    
    def __init__(self):
        self.cliente_modelo = ClienteModelo("","","")
    
    def programar_cita(self):
        print("\n--Programar cita---")
        cliente = self.cliente_modelo.obtener_clientes()
        if not cliente:
            print("No hay clientes registrados. Debe registrar primero un cliente.")
            return
        nombre_cliente=input("ingrese el nombre del propietario :")
        cliente = next((c for c in cliente if c.nombre==nombre_cliente),None)

        if cliente:
            nombre_mascota=input("Ingrese el nombre de la mascota:")
            mascota=next((m for m in cliente.mascotas if m.nombre==nombre_mascota),None)

            if mascota:
                 fecha = input("Fecha de la cita (YYYY-MM-DD): ")
                 while not validar_fecha(fecha):
                     print("Fecha no valida. Use el formato YYYY-MM-DD.")
                     fecha = input("Fecha de la cita (YYYY-MM-DD): ")
                     
                 hora = input("Hora de la cita (HH:MM): ")
                 while not validar_hora(hora):
                         print("Hora no valida. Use el formato HH:MM.")
                         hora = input("Hora de la cita (HH:MM): ")
                 servicio=input("Servicio(consulta,vacunacion,desparacitacion,etc):")
                 veterinario=input("Ingrese nombre veterinario asignado:")
                 cita=CitasModelo(fecha,hora,servicio,veterinario)
                 mascota.agregar_cita(cita)
                 print(f"Cita programada para mascota {mascota.nombre} el {fecha} a las {hora} con veterinario {veterinario}")
            else:
                print("Mascota no encontrada") 
        else:
            print("Cliente no encontrado")
            
    def actualizar_cita(self):
        try:
            
            clientes = self.cliente_modelo.obtener_clientes()
            
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
            
            cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
            if not cliente:
                raise ValueError("Cliente no encontrado.")

            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")
            
            if not mascota.historial_citas:
                raise ValueError("No hay citas registradas para esta mascota")
            
            print("Citas disponibles para actualizar:")
            for i, cita in enumerate(mascota.historial_citas):
                print(f"{i + 1}: Fecha: {cita.fecha}. Hora: {cita.hora}. Servicio: {cita.servicio}. Veterinario: {cita.veterinario}")
                
            indice = int(input("Seleccione el número de la cita a actualizar: ").strip()) -1
            if indice < 0 or indice >= len(mascota.historial_citas):
                raise ValueError("Selección invalida")
            
            cita = mascota.historial_citas[indice]
            
            print("Deje en blanco los campos que no desea actualizar")
            nueva_fecha = input("Nueva fecha (AAAA-MM-DD): ").strip()
            nueva_hora = input("Nueva hora (HH:MM): ").strip()
            nuevo_servicio = input("Nuevo servicio: ").strip()
            nuevo_veterinario = input("Nuevo veterinario: ").strip()
            
            if nueva_fecha:
                datetime.strptime(nueva_fecha, "%Y-%m-%d")
                cita.actualizar(fecha = nueva_fecha)
            if nueva_hora:
                datetime.strptime(nueva_hora, "%H:%M")
                cita.actualizar(hora = nueva_hora)
            if nuevo_servicio:
                cita.actualizar(servicio = nuevo_servicio)
            if nuevo_veterinario:
                cita.actualizar(veterinario = nuevo_veterinario)
            
            print("¡Cita actualizada con éxito!")
        except ValueError as e:
            print(f"Error: {e}")

    def consultar_historial(self):
        print("\n--Historial de citas---")
        cliente = self.cliente_modelo.obtener_clientes()
        if not cliente:
            print("No hay clientes registrados. Debe registrar primero un cliente.")
            return
        nombre_cliente=input("ingrese el nombre del propietario :")
        cliente=next((c for c in cliente if c.nombre==nombre_cliente),None)

        if cliente:
            nombre_mascota=input("Ingrese el nombre de la mascota:")
            mascota=next((m for m in cliente.mascotas if m.nombre==nombre_mascota),None)

            if mascota:
                print("\nHisotrial de citas y servicios para :", mascota.nombre)
                print("-"*50)
                print("Citas programadas:")
                for cita in mascota.historial_citas:
                    cita.mostrar_info()
                print("-"*50)
            else:
                print("Mascota no encontrada") 
        else:
            print("Cliente no encontrado")
            
                   


        

   