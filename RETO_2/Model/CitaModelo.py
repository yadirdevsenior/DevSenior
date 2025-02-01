from datetime import datetime
from RETO_2.Model.ClasesAbstractas.CitasAbs import CitasAbs

class CitaModelo(CitasAbs):
    def actualizar(self):
        try: 
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
            
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)
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
            
            if nuevo_servicio == "":
                nuevo_servicio = mascota.historial_citas[indice].servicio

            if nueva_fecha == "":
                nueva_fecha = mascota.historial_citas[indice].fecha

            if nueva_hora == "":
                nueva_hora= mascota.historial_citas[indice].hora

            if nuevo_veterinario == "":
                nuevo_veterinario = mascota.historial_citas[indice].veterinario





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
    
