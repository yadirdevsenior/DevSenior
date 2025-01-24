from Controller.CitasController import CitasController
from Controller.ClienteController import ClienteController
from Controller.MascotaController import MascotaController

def mostrar_menu_principal():
    print("\n==============================")
    print("     SISTEMA DE VETERINARIA     ")
    print("==============================")
    print("1. Registrar Cliente")
    print("2. Registrar Mascota")
    print("3. Programar Cita")
    print("4. Consultar Historial de Mascotas")
    print("5. Actualizar citas")
    print("6. Salir")
    print("==============================")
    opcion = input("Selecciona una opción: ")
    return opcion

def view():

    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            ClienteController().registrar_cliente_controller()
        elif opcion == "2":
            MascotaController().registrar_mascota()
        elif opcion == "3":
            CitasController().programar_cita()
        elif opcion == "4":
            CitasController().consultar_historial()
        elif opcion == "5":
            CitasController().actualizar_cita()
        elif opcion == "6":
            print("\nGracias por utilizar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresa una opción correcta.")

