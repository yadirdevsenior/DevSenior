import tkinter as tk
from tkinter import ttk, messagebox

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
    
    def crear_vista_productos(self):
        frame_productos = ttk.Frame(self.notebook)
        self.notebook.add(frame_productos, text="Agregar Productos")
        
        ttk.Label(frame_productos, text="Nombre:").grid(row=0, column=0)
        self.nombre_var = tk.StringVar()
        ttk.Entry(frame_productos, textvariable=self.nombre_var).grid(row=0, column=1)
        
        ttk.Label(frame_productos, text="Precio Venta:").grid(row=1, column=0)
        self.precio_venta_var = tk.DoubleVar()
        ttk.Entry(frame_productos, textvariable=self.precio_venta_var).grid(row=1, column=1)
        
        ttk.Label(frame_productos, text="Precio Compra:").grid(row=2, column=0)
        self.precio_compra_var = tk.DoubleVar()
        ttk.Entry(frame_productos, textvariable=self.precio_compra_var).grid(row=2, column=1)
        
        ttk.Label(frame_productos, text="Cantidad:").grid(row=3, column=0)
        self.cantidad_var = tk.IntVar()
        ttk.Entry(frame_productos, textvariable=self.cantidad_var).grid(row=3, column=1)
        
        ttk.Button(frame_productos, text="Agregar Producto", command=self.agregar_producto).grid(row=4, column=0, columnspan=2)
        
        self.tree_productos = ttk.Treeview(frame_productos, columns=("Nombre", "Precio Venta", "Cantidad"), show='headings')
        self.tree_productos.heading("Nombre", text="Nombre")
        self.tree_productos.heading("Precio Venta", text="Precio Venta")
        self.tree_productos.heading("Cantidad", text="Cantidad")
        self.tree_productos.grid(row=5, column=0, columnspan=2)
    
    def agregar_producto(self):
        producto = {
            "nombre": self.nombre_var.get(),
            "precio_venta": self.precio_venta_var.get(),
            "precio_compra": self.precio_compra_var.get(),
            "cantidad": self.cantidad_var.get()
        }
        self.productos.append(producto)
        self.tree_productos.insert("", "end", values=(producto["nombre"], producto["precio_venta"], producto["cantidad"]))
        messagebox.showinfo("Éxito", "Producto agregado correctamente")
    
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
        
        self.tree_carrito = ttk.Treeview(frame_ventas, columns=("Nombre", "Cantidad", "Subtotal"), show='headings')
        self.tree_carrito.heading("Nombre", text="Nombre")
        self.tree_carrito.heading("Cantidad", text="Cantidad")
        self.tree_carrito.heading("Subtotal", text="Subtotal")
        self.tree_carrito.grid(row=4, column=0, columnspan=2)
    
    def agregar_al_carrito(self):
        for producto in self.productos:
            if producto['nombre'].lower() == self.buscar_var.get().lower():
                cantidad = self.cantidad_vender_var.get()
                if cantidad <= producto['cantidad']:
                    subtotal = cantidad * producto['precio_venta']
                    self.carrito.append({"nombre": producto['nombre'], "cantidad": cantidad, "subtotal": subtotal})
                    self.tree_carrito.insert("", "end", values=(producto['nombre'], cantidad, subtotal))
                    producto['cantidad'] -= cantidad
                    return
        messagebox.showerror("Error", "Producto no encontrado o cantidad insuficiente")
    
    def realizar_venta(self):
        total_venta = sum(item['subtotal'] for item in self.carrito)
        self.historial.append({"items": self.carrito, "total": total_venta})
        self.carrito = []
        self.tree_carrito.delete(*self.tree_carrito.get_children())
        messagebox.showinfo("Venta Realizada", f"Total Venta: {total_venta}")
    
    def crear_vista_historial(self):
        frame_historial = ttk.Frame(self.notebook)
        self.notebook.add(frame_historial, text="Historial de Compras")
        
        self.tree_historial = ttk.Treeview(frame_historial, columns=("Total",), show='headings')
        self.tree_historial.heading("Total", text="Total de la Venta")
        self.tree_historial.pack()
        
        ttk.Button(frame_historial, text="Actualizar Historial", command=self.actualizar_historial).pack()
    
    def actualizar_historial(self):
        self.tree_historial.delete(*self.tree_historial.get_children())
        for venta in self.historial:
            self.tree_historial.insert("", "end", values=(venta['total'],))

if __name__ == "__main__":
    root = tk.Tk()
    app = SupermercadoApp(root)
    root.mainloop()
