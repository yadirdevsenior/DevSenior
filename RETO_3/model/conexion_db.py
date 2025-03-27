import sqlite3
import os


class ConexionDB:
    def __init__(self):
        self.base_datos = os.path.abspath('./DevSenior/RETO_3/database/supermercado.db')
        print('conexion database',self.base_datos)
       # if os.path.isfile(self.base_datos):
            
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
        
    def cerrar_conexion(self):
        self.conexion.commit()
        self.conexion.close()
