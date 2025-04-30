import customtkinter as ctk
from controllers.venta_controller import VentaController
from controllers.cliente_controller import ClienteController
from controllers.producto_controller import ProductoController
from CTkMessagebox import CTkMessagebox

class VentaView(ctk.CTkFrame):
    """Vista para el registro y listado de ventas"""
    
    def __init__(self, parent, modo_listado=False):
        super().__init__(parent)
        
        # Guardar el modo (registro o listado)
        self.modo_listado = modo_listado
        
        # Crear el contenedor principal
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título
        self.title_label = ctk.CTkLabel(
            self.container, 
            text="Listado de Ventas" if modo_listado else "Registro de Ventas", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.pack(pady=10)
        
        if not modo_listado:
            # Frame para el formulario (solo en modo registro)
            self.form_frame = ctk.CTkFrame(self.container)
            self.form_frame.pack(fill="x", padx=20, pady=10)
            
            # Centrar el formulario
            form_container = ctk.CTkFrame(self.form_frame)
            form_container.pack(pady=10, padx=20, anchor="center")
            
            # Cargar clientes y productos para los combobox
            self.clientes = ClienteController.obtener_todos_clientes()
            self.productos = ProductoController.obtener_todos_productos()
            
            # Convertir a listas para los combobox
            self.clientes_nombres = [f"{c.id} - {c.nombre}" for c in self.clientes]
            self.productos_nombres = [f"{p.id} - {p.nombre} (${p.precio:.2f})" for p in self.productos]
            
            # Campos del formulario
            self.lbl_cliente = ctk.CTkLabel(form_container, text="Cliente:")
            self.lbl_cliente.grid(row=0, column=0, padx=10, pady=10, sticky="e")
            
            self.combo_cliente = ctk.CTkComboBox(
                form_container, 
                values=self.clientes_nombres,
                width=300
            )
            if self.clientes_nombres:
                self.combo_cliente.set(self.clientes_nombres[0])
            else:
                self.combo_cliente.set("No hay clientes disponibles")
            self.combo_cliente.grid(row=0, column=1, padx=10, pady=10)
            
            self.lbl_producto = ctk.CTkLabel(form_container, text="Producto:")
            self.lbl_producto.grid(row=1, column=0, padx=10, pady=10, sticky="e")
            
            self.combo_producto = ctk.CTkComboBox(
                form_container, 
                values=self.productos_nombres,
                width=300,
                command=self.actualizar_precio
            )
            if self.productos_nombres:
                self.combo_producto.set(self.productos_nombres[0])
                # Extraer el precio del producto seleccionado
                self.precio_actual = self.obtener_precio_producto()
            else:
                self.combo_producto.set("No hay productos disponibles")
                self.precio_actual = 0
            self.combo_producto.grid(row=1, column=1, padx=10, pady=10)
            
            self.lbl_cantidad = ctk.CTkLabel(form_container, text="Cantidad:")
            self.lbl_cantidad.grid(row=2, column=0, padx=10, pady=10, sticky="e")
            
            self.entry_cantidad = ctk.CTkEntry(form_container, width=300)
            self.entry_cantidad.insert(0, "1")  # Valor por defecto
            self.entry_cantidad.grid(row=2, column=1, padx=10, pady=10)
            self.entry_cantidad.bind("<KeyRelease>", self.calcular_total)
            
            # Mostrar el precio unitario y total
            self.lbl_precio_unitario = ctk.CTkLabel(form_container, text="Precio unitario:")
            self.lbl_precio_unitario.grid(row=3, column=0, padx=10, pady=10, sticky="e")
            
            self.lbl_precio_valor = ctk.CTkLabel(
                form_container, 
                text=f"${self.precio_actual:.2f}",
                font=ctk.CTkFont(weight="bold")
            )
            self.lbl_precio_valor.grid(row=3, column=1, padx=10, pady=10, sticky="w")
            
            self.lbl_total = ctk.CTkLabel(form_container, text="Total:")
            self.lbl_total.grid(row=4, column=0, padx=10, pady=10, sticky="e")
            
            self.lbl_total_valor = ctk.CTkLabel(
                form_container, 
                text=f"${self.precio_actual:.2f}",  # Inicialmente igual al precio unitario
                font=ctk.CTkFont(size=16, weight="bold")
            )
            self.lbl_total_valor.grid(row=4, column=1, padx=10, pady=10, sticky="w")
            
            # Botón para guardar
            self.btn_guardar = ctk.CTkButton(
                form_container, 
                text="Registrar Venta", 
                command=self.guardar_venta
            )
            self.btn_guardar.grid(row=5, column=0, columnspan=2, padx=10, pady=20)
        
        # Frame para la lista de ventas (en ambos modos)
        self.list_frame = ctk.CTkFrame(self.container)
        self.list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Título de la lista
        self.list_title = ctk.CTkLabel(
            self.list_frame, 
            text="Historial de Ventas", 
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.list_title.pack(pady=10)
        
        # Crear la tabla (usando un widget Text para simular una tabla)
        self.tabla = ctk.CTkTextbox(self.list_frame, height=300)
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Cargar las ventas existentes
        self.cargar_ventas()
    
    def obtener_precio_producto(self):
        """Obtiene el precio del producto seleccionado"""
        if not self.productos_nombres:
            return 0
            
        seleccion = self.combo_producto.get()
        try:
            # Extraer el ID del producto de la selección
            producto_id = int(seleccion.split(" - ")[0])
            # Buscar el producto por ID
            for producto in self.productos:
                if producto.id == producto_id:
                    return producto.precio
        except:
            pass
        return 0
    
    def actualizar_precio(self, event=None):
        """Actualiza el precio mostrado cuando cambia el producto seleccionado"""
        self.precio_actual = self.obtener_precio_producto()
        self.lbl_precio_valor.configure(text=f"${self.precio_actual:.2f}")
        self.calcular_total()
    
    def calcular_total(self, event=None):
        """Calcula y muestra el total de la venta"""
        try:
            cantidad = int(self.entry_cantidad.get())
            if cantidad <= 0:
                cantidad = 1
            total = self.precio_actual * cantidad
            self.lbl_total_valor.configure(text=f"${total:.2f}")
        except:
            self.lbl_total_valor.configure(text="$0.00")
    
    def guardar_venta(self):
        """Guarda una nueva venta en la base de datos"""
        # Verificar que haya clientes y productos
        if not self.clientes or not self.productos:
            CTkMessagebox(
                title="Error", 
                message="No hay clientes o productos disponibles para registrar una venta", 
                icon="cancel"
            )
            return
        
        # Obtener los datos del formulario
        seleccion_cliente = self.combo_cliente.get()
        seleccion_producto = self.combo_producto.get()
        cantidad = self.entry_cantidad.get()
        
        try:
            # Extraer los IDs
            cliente_id = int(seleccion_cliente.split(" - ")[0])
            producto_id = int(seleccion_producto.split(" - ")[0])
            cantidad = int(cantidad)
            
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que cero")
        except ValueError as e:
            CTkMessagebox(
                title="Error", 
                message=f"Error en los datos: {e}", 
                icon="cancel"
            )
            return
        
        # Intentar guardar la venta
        venta = VentaController.crear_venta(cliente_id, producto_id, cantidad)
        
        if venta:
            CTkMessagebox(
                title="Éxito", 
                message=f"Venta registrada correctamente", 
                icon="check"
            )
            # Recargar la lista de ventas
            self.cargar_ventas()
        else:
            CTkMessagebox(
                title="Error", 
                message="No se pudo registrar la venta", 
                icon="cancel"
            )
    
    def cargar_ventas(self):
        """Carga y muestra las ventas existentes"""
        # Limpiar la tabla
        self.tabla.delete('1.0', 'end')
        
        # Obtener todas las ventas
        ventas = VentaController.obtener_todas_ventas()
        
        # Mostrar encabezados
        self.tabla.insert('end', f"{'ID':<5} {'Fecha':<20} {'Cliente':<20} {'Producto':<20} {'Cant.':<8} {'Precio':<10} {'Total':<10}\n")
        self.tabla.insert('end', "-" * 100 + "\n")
        
        # Mostrar cada venta
        for venta in ventas:
            self.tabla.insert('end', (
                f"{venta['id']:<5} {venta['fecha']:<20} {venta['cliente_nombre'][:18]:<20} "
                f"{venta['producto_nombre'][:18]:<20} {venta['cantidad']:<8} "
                f"${venta['precio_unitario']:<9.2f} ${venta['total']:<9.2f}\n"
            ))