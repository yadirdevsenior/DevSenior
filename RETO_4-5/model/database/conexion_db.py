import mysql.connector
from mysql.connector import Error


class ConexionDB:
    
    __instancia = None
    
    def __new__(cls):
        
        if cls.__instancia is None:
            cls.__instancia = super(ConexionDB, cls).__new__(cls)
        return cls.__instancia
    
    def __init__(self):
        
        if not hasattr(self, '_conexion'):
            try:
                self._conexion = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='Academia'
                )
                if self._conexion.is_connected():
                    print('conexion establecida')
            except Error as ex:
                print('Error de conexion a la base de datos')
    
    def get_conexion(self):
        return self._conexion if self._conexion.is_connected() else None
        