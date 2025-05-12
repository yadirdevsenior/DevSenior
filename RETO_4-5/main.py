from controller.estudiante_controller import EstudianteController 

def main():
    estudiante = EstudianteController()
    estudiante.registrar_estudiante('jhon sebastian', 'jhon@gmail.com', '2000-08-08')



if __name__== "__main__":
    main()
    