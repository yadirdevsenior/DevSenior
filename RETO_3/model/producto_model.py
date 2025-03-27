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
                CREATE TABLE IF NOT EXISTS Productos 
                (
                    IdProducto INTEGER,
                    NombreProducto VarChar(50),
                    CantidadProducto INTEGER,
                    PrecioVenta DECIMAL(18,2),
                    PrecioCompra DECIMAL(18,2),
                    PRIMARY KEY(IdProducto AUTOINCREMENT)
                )
            '''
        conexion.cursor.execute(sql)
        sql2 = '''SELECT * FROM Productos'''
        response = conexion.cursor.execute(sql2)
        result = response.fetchall()
        for item in  result:
            print(item)
        conexion.cerrar_conexion()
        
    def insertar_producto(self): 
        conexion = ConexionDB()
        sql = '''
                INSERT INTO Productos (NombreProducto, CantidadProducto, PrecioVenta, PrecioCompra)
                VALUES(?,?,?,?)
            '''
        conexion.cursor.execute(sql, (self.nombreProducto, self.cantidad, self.precioVenta, self.precioCompra))
        sql2 = '''SELECT Idproducto,
                         NombreProducto,
                         CantidadProducto,
                         PrecioVenta,
                         PrecioCompra 
                  FROM Productos'''
        response = conexion.cursor.execute(sql2)
        result = response.fetchall()
        conexion.cerrar_conexion()
        return result
    
    
    def obtener_productos(self):
        conexion = ConexionDB()
       
        sql2 = '''SELECT Idproducto,
                         NombreProducto,
                         CantidadProducto,
                         PrecioVenta,
                         PrecioCompra 
                  FROM Productos'''
        
        response = conexion.cursor.execute(sql2)
        result = response.fetchall()
        conexion.cerrar_conexion()
        return result
    
    def delete_producto(self, id_producto):
        conexion = ConexionDB()
        sql2 = '''DELETE FROM Productos WHERE IdProducto = ?'''
        conexion.cursor.execute(sql2, (id_producto,))
        conexion.conexion.commit()
        conexion.cerrar_conexion()
        
    def obtener_productos_nombre_db(self, nombre_producto):
   
        conexion = ConexionDB()
       
        sql2 = '''SELECT Idproducto,
                         NombreProducto,
                         CantidadProducto,
                         PrecioVenta,
                         PrecioCompra 
                  FROM Productos where NombreProducto = ?'''
        
        response = conexion.cursor.execute(sql2, (nombre_producto,))
        result = response.fetchall()
        conexion.cerrar_conexion()
        return result
    
    def actualizar_producto_db(self,cantidad, id_producto):
   
        conexion = ConexionDB()
       
        sql2 = '''UPDATE Productos SET CantidadProducto = ? WHERE IdProducto = ?'''
        
        response = conexion.cursor.execute(sql2, (cantidad, id_producto,))
        conexion.conexion.commit()
        conexion.cerrar_conexion()

    def obtener_productos_id_db(self, id_producto):
   
        conexion = ConexionDB()
       
        sql2 = '''SELECT Idproducto,
                         NombreProducto,
                         CantidadProducto,
                         PrecioVenta,
                         PrecioCompra 
                  FROM Productos where Idproducto = ?'''
        
        response = conexion.cursor.execute(sql2, (id_producto,))
        result = response.fetchall()
        conexion.cerrar_conexion()
        return result   