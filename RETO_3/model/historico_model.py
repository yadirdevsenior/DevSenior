from .conexion_db import ConexionDB
import uuid

class historicoModel:
    def __init__(self, cantidad_item, total, ganancias):
      self.cantidad_item = cantidad_item
      self.total = total
      self.ganancias = ganancias
      
      
    
    def crear_tabla(self):
        conexion = ConexionDB()
        
        sql = '''
                CREATE TABLE IF NOT EXISTS HistoricoVentas
                
                (
                    IdHistorico INTEGER,
                    CantidadItem INTEGER,
                    Total DECIMAL(18,2),
                    Ganancias DECIMAL(18,2),
                    NoFactura TEXT UNIQUE NOT NULL,
                    PRIMARY KEY(IdHistorico AUTOINCREMENT)
                )
            '''
        conexion.cursor.execute(sql)
        sql2 = '''SELECT * FROM HistoricoVentas'''
        response = conexion.cursor.execute(sql2)
        result = response.fetchall()
        for item in  result:
            print(item)
        conexion.cerrar_conexion()
        
    def insertar_historico_ventas(self): 
        conexion = ConexionDB()
        sql = '''
                INSERT INTO HistoricoVentas (CantidadItem, Total, Ganancias, NoFactura)
                VALUES(?,?,?,?)
            '''
        numero_factura = str(uuid.uuid4())
        conexion.cursor.execute(sql, ( self.cantidad_item, self.total, self.ganancias, numero_factura))
        conexion.conexion.commit()
        sql2 = '''SELECT CantidadItem, 
                        Total , 
                        Ganancias,
                        NoFactura
                  FROM HistoricoVentas'''
        response = conexion.cursor.execute(sql2)
        result = response.fetchall()
        conexion.cerrar_conexion()
        return result
    