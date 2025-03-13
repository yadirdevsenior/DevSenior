from model.producto_model import ProductoModel

class ProductosController:
    def crear_tabla():
        productos = ProductoModel('','','','')
        productos.crear_tabla()
    
    def insertar(data):
        
        productos= ProductoModel(data.get("nombreProducto"), data.get("precioCompra"), data.get("precioVenta"), data.get("cantidad")) 
        return productos.insertar_producto()