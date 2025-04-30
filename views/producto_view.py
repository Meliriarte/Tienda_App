import customtkinter as ctk
from controllers.producto_controller import ProductoController
from CTkMessagebox import CTkMessagebox

class ProductoView(ctk.CTkFrame):
    """Vista para la gestión de productos"""
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # Crear el contenedor principal
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título
        self.title_label = ctk.CTkLabel(
            self.container, 
            text="Gestión de Productos", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.pack(pady=10)
        
        # Frame para el formulario
        self.form_frame = ctk.CTkFrame(self.container)
        self.form_frame.pack(fill="x", padx=20, pady=10)
        
        # Centrar el formulario
        form_container = ctk.CTkFrame(self.form_frame)
        form_container.pack(pady=10, padx=20, anchor="center")
        
        # Campos del formulario
        self.lbl_nombre = ctk.CTkLabel(form_container, text="Nombre:")
        self.lbl_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        
        self.entry_nombre = ctk.CTkEntry(form_container, width=300)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        
        self.lbl_precio = ctk.CTkLabel(form_container, text="Precio:")
        self.lbl_precio.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        self.entry_precio = ctk.CTkEntry(form_container, width=300)
        self.entry_precio.grid(row=1, column=1, padx=10, pady=10)
        
        # Botón para guardar
        self.btn_guardar = ctk.CTkButton(
            form_container, 
            text="Guardar Producto", 
            command=self.guardar_producto
        )
        self.btn_guardar.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
        
        # Frame para la lista de productos
        self.list_frame = ctk.CTkFrame(self.container)
        self.list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Título de la lista
        self.list_title = ctk.CTkLabel(
            self.list_frame, 
            text="Productos Registrados", 
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.list_title.pack(pady=10)
        
        # Crear la tabla (usando un widget Text para simular una tabla)
        self.tabla = ctk.CTkTextbox(self.list_frame, height=200)
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Cargar los productos existentes
        self.cargar_productos()
    
    def guardar_producto(self):
        """Guarda un nuevo producto en la base de datos"""
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        
        # Validar que los campos no estén vacíos
        if not nombre or not precio:
            CTkMessagebox(
                title="Error", 
                message="Todos los campos son obligatorios", 
                icon="cancel"
            )
            return
        
        # Validar que el precio sea un número
        try:
            precio_float = float(precio)
            if precio_float <= 0:
                raise ValueError("El precio debe ser mayor que cero")
        except ValueError:
            CTkMessagebox(
                title="Error", 
                message="El precio debe ser un número mayor que cero", 
                icon="cancel"
            )
            return
        
        # Intentar guardar el producto
        producto = ProductoController.crear_producto(nombre, precio)
        
        if producto:
            CTkMessagebox(
                title="Éxito", 
                message=f"Producto '{nombre}' guardado correctamente", 
                icon="check"
            )
            # Limpiar los campos
            self.entry_nombre.delete(0, 'end')
            self.entry_precio.delete(0, 'end')
            # Recargar la lista de productos
            self.cargar_productos()
        else:
            CTkMessagebox(
                title="Error", 
                message="No se pudo guardar el producto. Verifique que no exista uno con el mismo nombre.", 
                icon="cancel"
            )
    
    def cargar_productos(self):
        """Carga y muestra los productos existentes"""
        # Limpiar la tabla
        self.tabla.delete('1.0', 'end')
        
        # Obtener todos los productos
        productos = ProductoController.obtener_todos_productos()
        
        # Mostrar encabezados
        self.tabla.insert('end', f"{'ID':<5} {'Nombre':<30} {'Precio':<10}\n")
        self.tabla.insert('end', "-" * 50 + "\n")
        
        # Mostrar cada producto
        for producto in productos:
            self.tabla.insert('end', f"{producto.id:<5} {producto.nombre:<30} ${producto.precio:.2f}\n")
