
from model.historico_model import historicoModel

class HistoricoController:
    def __init__(self):
        self.productos = historicoModel('','','')
    def crear_tabla(self):
        self.productos.crear_tabla()
    def insertar(self,items, total, ganancias):
        cantidad_item = items
        historico= historicoModel(cantidad_item, total, ganancias) 
        return historico.insertar_historico_ventas()
    