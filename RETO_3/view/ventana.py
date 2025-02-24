import tkinter as tk
from tkinter import ttk, messagebox


class SupermercadoApp:
 
    # Constructor de la clase
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Sistema de Supermercado")
        self.root.geometry("600x400")
        # root sirve para crear la ventana principal
        # Variables de instancia
        self.productos = {}
        self.historial_compras = []
        # Creación de la interfaz gráfica (el notebook sirve para gestionar las pestañas)
        self.notebook = ttk.Notebook(root)
        # Creación de los frames
        self.frame_productos = ttk.Frame(self.notebook)
        self.frame_ventas = ttk.Frame(self.notebook)
        self.frame_historial = ttk.Frame(self.notebook)
        # Añadir los frames al notebook
        self.notebook.add(self.frame_productos, text="Gestión de Productos")
        self.notebook.add(self.frame_ventas, text="Realizar Venta")
        self.notebook.add(self.frame_historial, text="Historial de Compras")
        self.notebook.pack(expand=True, fill='both')
        # Creación de las vistas
        self.crear_vista_productos()
        self.crear_vista_ventas()
        self.crear_vista_historial()
        self.crear_botones_navegacion()
    #
    def crear_vista_productos(self):
        
        ttk.Label(self.frame_productos, text="Nombre del Producto:").pack()
        self.entry_nombre = ttk.Entry(self.frame_productos)
        self.entry_nombre.pack()
        # Crea una etiqueta y un campo de entrada para el precio
        ttk.Label(self.frame_productos, text="Precio:").pack()
        self.entry_precio = ttk.Entry(self.frame_productos)
        self.entry_precio.pack()
        
        ttk.Label(self.frame_productos, text="Cantidad:").pack() 
        self.entry_cantidad = ttk.Entry(self.frame_productos)
        self.entry_cantidad.pack()
        # Crea un botón para agregar productos
        ttk.Button(self.frame_productos, text="Agregar Producto", command=self.agregar_producto).pack()
    
    def agregar_producto(self): # Método para agregar productos
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        cantidad = self.entry_cantidad.get()
        # Verifica que los datos ingresados sean válidos
        if nombre and precio.isdigit() and cantidad.isdigit():
            self.productos[nombre] = {"precio": int(precio), "cantidad": int(cantidad)}
            messagebox.showinfo("Éxito", f"Producto {nombre} agregado correctamente")
        else:
            messagebox.showerror("Error", "Ingrese datos válidos")
    
    def crear_vista_ventas(self):# Método para crear la vista de ventas
        ttk.Label(self.frame_ventas, text="Seleccione Producto:").pack() 

        self.producto_seleccionado = ttk.Combobox(self.frame_ventas, values=list(self.productos.keys()))
        self.producto_seleccionado.pack()
        
        ttk.Label(self.frame_ventas, text="Cantidad:").pack()
        self.entry_cantidad_venta = ttk.Entry(self.frame_ventas)
        self.entry_cantidad_venta.pack()
        # Crea un botón para realizar la venta
        ttk.Button(self.frame_ventas, text="Realizar Venta", command=self.realizar_venta).pack()
        
        self.texto_factura = tk.Text(self.frame_ventas, height=10)
        self.texto_factura.pack()
    
    def realizar_venta(self): # Método para realizar la venta
        producto = self.producto_seleccionado.get()
        cantidad = self.entry_cantidad_venta.get()
        
        if producto in self.productos and cantidad.isdigit():
            cantidad = int(cantidad)
            if self.productos[producto]["cantidad"] >= cantidad:
                total = cantidad * self.productos[producto]["precio"]
                self.historial_compras.append(f"{producto} x{cantidad} = ${total}")
                self.productos[producto]["cantidad"] -= cantidad
                
                factura = f"\nFactura:\n{producto} x{cantidad} = ${total}\nTotal: ${total}\n"
                self.texto_factura.delete("1.0", tk.END)
                self.texto_factura.insert(tk.END, factura)
                
                messagebox.showinfo("Factura", factura)
            else:
                messagebox.showerror("Error", "Stock insuficiente")
        else:
            messagebox.showerror("Error", "Datos inválidos")
    # Método para crear la vista de historial
    def crear_vista_historial(self):
        ttk.Button(self.frame_historial, text="Actualizar Historial", command=self.mostrar_historial).pack()
        self.texto_historial = tk.Text(self.frame_historial, height=10)
        self.texto_historial.pack()
    
    def mostrar_historial(self):
        self.texto_historial.delete("1.0", tk.END)
        for compra in self.historial_compras:
            self.texto_historial.insert(tk.END, compra + "\n")
    
    def crear_botones_navegacion(self):
        frame_botones = ttk.Frame(self.root)
        frame_botones.pack(side=tk.BOTTOM, fill=tk.X)
        # Crea botones para navegar entre las pestañas
        ttk.Button(frame_botones, text="Gestión de Productos",  command=lambda : self.notebook.select(self.frame_productos)).pack(side=tk.LEFT, expand=True)
        ttk.Button(frame_botones, text="Realizar Venta", command=lambda: self.notebook.select(self.frame_ventas)).pack(side=tk.LEFT, expand=True)
        ttk.Button(frame_botones, text="Historial de Compras", command=lambda: self.notebook.select(self.frame_historial)).pack(side=tk.LEFT, expand=True)
        #lambda es una función anónima que se utiliza para llamar a una función con argumentos
# Método principal que crea la ventana principal y la ejecuta
root = tk.Tk()
app = SupermercadoApp(root)
root.mainloop()

