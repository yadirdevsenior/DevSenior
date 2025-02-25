from .conexion_db import ConexionDB

class ProductoModel:
    def __init__(self, nombreProducto, precioCompra, precioVenta, cantidad):
      self.nombreProducto = nombreProducto
      self.precioCompra = precioCompra
      self.precioVenta = precioVenta
      self.cantidad = cantidad
      
    
    def crear_tabla(self):
        conexion = ConexionDB()
        
        sql = '''
                CREATE TABLE productos 
                (
                    IdProducto INTEGER,
                    NombreProducto INT,
                    PrecioCompra DECIMAL(18,2),
                    Cantida INTEGER,
                    PRIMARY KEY(IdProducto AUTOINCREMENT)
                )
            '''
        conexion.cursor.execute(sql)
        sql2 = '''SELECT * FROM productos'''
        response = conexion.cursor.execute(sql2)
        result = response.fetchall()
        for item in  result:
            print(item)
        conexion.cerrar_conexion()
        
      