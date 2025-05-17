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
    
    def obtener_productos_nombre(self, nombre_producto):
        return self.productos.obtener_productos_nombre_db(nombre_producto)
    
    def actualizar_producto(self, detalle_venta):
        for item in detalle_venta:
            datos_actual = self.productos.obtener_productos_id_db(item["Idproducto"])
            for item2 in datos_actual:
                cantidad= item2[2]-item["CantidadProducto"]
                self.productos.actualizar_producto_db(cantidad,item["Idproducto"])
    