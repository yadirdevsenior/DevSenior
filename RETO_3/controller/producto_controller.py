from model.producto_model import ProductoModel

class ProductosController: 
    def __init__(self):
         self.productos = ProductoModel('','','','')
    def crear_tabla(self):
        self.productos.crear_tabla()
    
    def insertar(self, data): 
        productos= ProductoModel(data.get("nombreProducto"), data.get("precioCompra"), data.get("precioVenta"), data.get("cantidad")) 
        return productos.insertar_producto()
    
    def obtener(self):
        return self.productos.obtener_productos()
    
    def eliminar(self,id_producto):
        return self.productos.delete_producto(id_producto)
        
        