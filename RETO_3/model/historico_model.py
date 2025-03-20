from .conexion_db import ConexionDB

class historicoModel:
    def __init__(self, CantidadItem, Total, Ganancias):
      self.CantidadItem = CantidadItem
      self.Total = Total
      self.Ganancias = Ganancias
      
      
    
    def crear_tabla(self):
        conexion = ConexionDB()
        
        sql = '''
                CREATE TABLE HistoricoVentas
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
                INSERT INTO HistoricoVentas (CantidadItem, Total, Ganancias)
                VALUES(?,?,?)
            '''
        conexion.cursor.execute(sql, ( self.CantidadItem, self.Total, self.Ganancias))
        sql2 = '''SELECT CantidadItem, 
                        Total , 
                        Ganancias
                  FROM HistoricoVentas'''
        response = conexion.cursor.execute(sql2)
        result = response.fetchall()
        conexion.cerrar_conexion()
        return result
    