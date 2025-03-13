from view.ventana import SupermercadoApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = SupermercadoApp(root)
    root.mainloop()
   
#     ProductosController.crear_tabla()
#     data={
#          'nombreProducto':'CocaCola',
#          'precioCompra': 1.5,
#          'precioVenta': 2.5,
#          'cantidad': 100
#    }
#     ProductosController.insertar(data)
if __name__=="__main__":
    main()
    

    
