from .conexion_db import ConexionDB

class historicoModel:
    def __init__(self, IdProducto, total, ganancias):
      self.IdProducto = IdProducto
      self.total = total
      self.ganancias = ganancias
      
      
    
    def crear_tabla(self):
        conexion = ConexionDB()
        
        sql = '''
                CREATE TABLE HistoricoVentas
                (
                    IdHistorico INTEGER,
                    IdProducto INTEGER,
                    total DECIMAL(18,2),
                    ganancias DECIMAL(18,2),
                    NoFactura TEXT UNIQUE NOT NULL,
                    PRIMARY KEY(IdHistorico AUTOINCREMENT),
                   FOREIGN KEY(IdProducto) REFERENCES Productos(IdProducto)
                )
            '''
        conexion.cursor.execute(sql)
        sql2 = '''SELECT * FROM HistoricoVentas'''
        response = conexion.cursor.execute(sql2)
        result = response.fetchall()
        for item in  result:
            print(item)
        conexion.cerrar_conexion()
        