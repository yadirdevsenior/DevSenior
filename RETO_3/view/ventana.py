import tkinter as tk
from tkinter import ttk, messagebox
from controller.producto_controller import ProductosController
from controller.historico_venta_controller import HistoricoController
class SupermercadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Ventas - Supermercado")
        self.root.geometry("800x500")
        
        self.productos = []  # Lista de productos
        self.carrito = []  # Carrito de compras
        self.historial = []  # Historial de ventas
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)
        
        self.crear_vista_productos()
        self.crear_vista_ventas()
        self.crear_vista_historial()
        self.productos_controller = ProductosController()
        self.historico_controller = HistoricoController()
    
    def crear_vista_productos(self):
        frame_productos = ttk.Frame(self.notebook)
        self.notebook.add(frame_productos, text="Agregar Productos")
        
        label_nombre = ttk.Label(frame_productos, text="Nombre:")
        label_nombre.config(font=('Arial Narrow',12,'bold'))
        label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        self.nombre_var = tk.StringVar()
        entry_nombre = ttk.Entry(frame_productos, textvariable=self.nombre_var)
        entry_nombre.config(width=55, font=('Arial Narrow',12))
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        
        label_precio_venta = ttk.Label(frame_productos, text="Precio Venta:")
        label_precio_venta.config(font=('Arial Narrow',12,'bold'))
        label_precio_venta.grid(row=1, column=0, padx=10, pady=10)
        
        self.precio_venta_var = tk.DoubleVar()
        entry_precio_venta = ttk.Entry(frame_productos, textvariable=self.precio_venta_var)
        entry_precio_venta.config(width=55, font=('Arial Narrow',12))
        entry_precio_venta.grid(row=1, column=1, padx=10, pady=10)
        
        label_precio_compra = ttk.Label(frame_productos, text="Precio Compra:")
        label_precio_compra.config(font=('Arial Narrow',12,'bold'))
        label_precio_compra.grid(row=2, column=0, padx=10, pady=10)
        
        self.precio_compra_var = tk.DoubleVar()
        entry_precio_compra = ttk.Entry(frame_productos, textvariable=self.precio_compra_var)
        entry_precio_compra.config(width=55, font=('Arial Narrow',12))
        entry_precio_compra.grid(row=2, column=1, padx=10, pady=10)
        
        label_cantidad = ttk.Label(frame_productos, text="Cantidad:")
        label_cantidad.config(font=('Arial Narrow',11,'bold'))
        label_cantidad.grid(row=3, column=0, padx=10, pady=10)
        
        self.cantidad_var = tk.IntVar()
        entry_cantidad = ttk.Entry(frame_productos, textvariable=self.cantidad_var)
        entry_cantidad.config(width=55, font=('Arial Narrow',12))
        entry_cantidad.grid(row=3, column=1, padx=10, pady=10)
        
        style = ttk.Style()
        style.configure("Eliminar.TButton", foreground="#900C3F", font=("Arial", 12, "bold"))
        self.boton_agregar = ttk.Button(frame_productos, text="Agregar Producto", command=self.agregar_producto, style="Eliminar.TButton")
        self.boton_agregar.grid(row=4, column=0, padx=10, pady=10)
        self.boton_agregar.config(cursor='hand2')
        self.boton_eliminar = ttk.Button(frame_productos, text="Eliminar Producto", command=self.eliminar_producto, style="Eliminar.TButton")
        self.boton_eliminar.grid(row=4, column=1, padx=10, pady=10)
        self.boton_eliminar.config(cursor='hand2')
        
        self.tree_productos = ttk.Treeview(frame_productos, columns=("Id Producto","Nombre", "Precio Venta", "Cantidad"), show='headings')
        self.tree_productos.heading("Id Producto", text="Id Producto")
        self.tree_productos.heading("Nombre", text="Nombre")
        self.tree_productos.heading("Precio Venta", text="Precio Venta")
        self.tree_productos.heading("Cantidad", text="Cantidad")
        self.tree_productos.grid(row=5, column=0, columnspan=2)
        productos = ProductosController()
        obtener_productos = productos.obtener()
        for item in obtener_productos:
              self.tree_productos.insert("", "end", values=(item[0], item[1], item[4], item[2], item[3]))
    def agregar_producto(self):
        producto = {
            "nombreProducto": self.nombre_var.get(),
            "precioVenta": self.precio_venta_var.get(),
            "precioCompra": self.precio_compra_var.get(),
            "cantidad": self.cantidad_var.get()
        }
        self.productos_controller.crear_tabla()
        result = self.productos_controller.insertar(producto)
        self.productos.append(producto)
        for item in result:
              self.tree_productos.insert("", "end", values=(item[0],item[1], item[4], item[2], item[3]))
        messagebox.showinfo("Éxito", "Producto agregado correctamente")
    
    def limpiar_treeview(self):
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)

    def eliminar_producto(self):
        productos = ProductosController()
        selected_item = self.tree_productos.selection()
        
        if len(selected_item) == 0:
            messagebox.showinfo("Info", "Debe seleeccionar un producto")
        else:
            id_producto = self.tree_productos.item(selected_item[0])['values']
            productos.eliminar(id_producto[0])
            self.limpiar_treeview()
            productos =productos.obtener()
            for item in productos:
                self.tree_productos.insert("", "end", values=(item[0], item[1], item[4], item[2], item[3]))
            
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
    
    def crear_vista_ventas(self):
        frame_ventas = ttk.Frame(self.notebook)
        self.notebook.add(frame_ventas, text="Realizar Venta")
        
        ttk.Label(frame_ventas, text="Buscar Producto:").grid(row=0, column=0)
        self.buscar_var = tk.StringVar()
        ttk.Entry(frame_ventas, textvariable=self.buscar_var).grid(row=0, column=1)
        
        ttk.Label(frame_ventas, text="Cantidad a vender:").grid(row=1, column=0)
        self.cantidad_vender_var = tk.IntVar()
        ttk.Entry(frame_ventas, textvariable=self.cantidad_vender_var).grid(row=1, column=1)
        
        ttk.Button(frame_ventas, text="Agregar al Carrito", command=self.agregar_al_carrito).grid(row=2, column=0, columnspan=2)
        ttk.Button(frame_ventas, text="Vender", command=self.realizar_venta).grid(row=3, column=0, columnspan=2)
        
        self.tree_carrito = ttk.Treeview(frame_ventas, columns=("Idproducto","Nombre", "Cantidad", "Subtotal"), show='headings')
        self.tree_carrito.heading("Idproducto", text="Id")
        self.tree_carrito.heading("Nombre", text="Nombre")
        self.tree_carrito.heading("Cantidad", text="Cantidad")
        self.tree_carrito.heading("Subtotal", text="Subtotal")
        self.tree_carrito.grid(row=4, column=0, columnspan=2)
    
    def agregar_al_carrito(self):
        nombre_producto = self.buscar_var.get()
        cantidad = self.cantidad_vender_var.get()
        producto = self.productos_controller.obtener_productos_nombre(nombre_producto)
        for item in producto:
            if item[1] == nombre_producto and item[2] >= cantidad:
                subtotal = item[3] * cantidad
                self.carrito.append({"Idproducto": item[0],"NombreProducto": nombre_producto, "CantidadProducto": cantidad, "subtotal": subtotal})
                self.tree_carrito.insert("", "end", values=(item[0],nombre_producto, cantidad, subtotal))
                item[2] -= cantidad
                return
        
        messagebox.showerror("Error", "Producto no disponible o cantidad insuficiente")
    
    def crear_vista_historial(self):
        frame_historial = ttk.Frame(self.notebook)
        self.notebook.add(frame_historial, text="Historial de Ventas")
        
        self.tree_historial = ttk.Treeview(frame_historial, columns=("Items", "Total", "Ganancias"), show='headings')
        self.tree_historial.heading("Items", text="Items")
        self.tree_historial.heading("Total", text="Total")
        self.tree_historial.heading("Ganancias", text="Ganancias")
        self.tree_historial.pack(fill='both', expand=True)
        
        self.actualizar_historial(self)
    
    def actualizar_historial(self, total_venta):
        for row in self.tree_historial.get_children():
            self.tree_historial.delete(row)
        
        for venta in self.historial:
            items = ", ".join([f"{item['NombreProducto']} x{item['CantidadProducto']}" for item in venta["items"]])
            total = venta["total"]
            ganancias = sum([(item['subtotal'] - next(p['PrecioCompra'] * item['CantidadProducto'] for p in self.productos if p['NombreProducto'] == item['NombreProducto'])) for item in venta["items"]])
            self.tree_historial.insert("", "end", values=(items, total, ganancias))

        self.historico_controller.insertar(self.carrito,total_venta, ganancias)
    def realizar_venta(self):
        if not self.carrito:
            messagebox.showerror("Error", "No hay productos en el carrito para vender")
            return
        
        total_venta = sum(item['subtotal'] for item in self.carrito)
        detalle_venta = "\n".join([f"{ item['Idproducto']} - {item['NombreProducto']} {item['CantidadProducto']} - ${item['subtotal']:.2f}" for item in self.carrito])
        
        factura = f"Factura:\n{detalle_venta}\n\nTotal: ${total_venta:.2f}"
        messagebox.showinfo("Venta Realizada", factura)
        self.productos_controller.actualizar_producto(self.carrito)
        self.historico_controller.crear_tabla()
        self.historial.append({"items": self.carrito, "total": total_venta })
        self.carrito = []
        self.tree_carrito.delete(*self.tree_carrito.get_children())
        self.actualizar_historial(total_venta)
    
   


