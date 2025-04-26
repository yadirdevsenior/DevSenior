import mysql.connector
from mysql.connector import Error


class AcademiaDB:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='academia',
                user='root',
                password=''
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")

    def __del__(self):
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.connection.close()
            print("Conexión a MySQL cerrada")
