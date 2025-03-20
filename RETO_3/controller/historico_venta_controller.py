
from model.historico_model import historicoModel

class HistoricoController:
    def __init__(self):
        self.productos = historicoModel('','','')
    def crear_tabla(self):
        self.productos.crear_tabla()
    def insertar(self, data): 
        historico= historicoModel(data.get("CantidadItem"), data.get("Total"), data.get(" Ganancias")) 
        return historico.insertar_historico_ventas()
    