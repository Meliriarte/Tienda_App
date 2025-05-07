import customtkinter as ctk
from views.producto_view import ProductoView
from views.cliente_view import ClienteView
from views.venta_view import VentaView

class MainView(ctk.CTk):
    """Vista principal de la aplicación"""
    
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana principal
        self.title("Sistema de Ventas - Tienda")
        self.geometry("1000x700")
        self.minsize(900, 600)
        
        # Configuración del tema
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        
        # Crear el contenedor principal
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Crear el título
        self.title_label = ctk.CTkLabel(
            self.container, 
            text="Sistema de Ventas para Tienda", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(pady=20)
        
        # Crear el frame para la navegación
        self.nav_frame = ctk.CTkFrame(self.container)
        self.nav_frame.pack(fill="x", padx=20, pady=10)
        
        # Configurar columnas para centrar los botones
        self.nav_frame.columnconfigure(0, weight=1)
        self.nav_frame.columnconfigure(1, weight=1)
        self.nav_frame.columnconfigure(2, weight=1)
        self.nav_frame.columnconfigure(3, weight=1)
        self.nav_frame.columnconfigure(4, weight=1)
        
        # Botones para las diferentes funcionalidades
        self.btn_inicio = ctk.CTkButton(
            self.nav_frame, 
            text="Inicio", 
            command=self.mostrar_inicio,
            width=150,
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.btn_inicio.grid(row=0, column=0, padx=10, pady=10)
        
        self.btn_productos = ctk.CTkButton(
            self.nav_frame, 
            text="Productos", 
            command=self.mostrar_productos,
            width=150,
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.btn_productos.grid(row=0, column=1, padx=10, pady=10)
        
        self.btn_clientes = ctk.CTkButton(
            self.nav_frame, 
            text="Clientes", 
            command=self.mostrar_clientes,
            width=150,
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.btn_clientes.grid(row=0, column=2, padx=10, pady=10)
        
        self.btn_ventas = ctk.CTkButton(
            self.nav_frame, 
            text="Registrar Venta", 
            command=self.mostrar_ventas,
            width=150,
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.btn_ventas.grid(row=0, column=3, padx=10, pady=10)
        
        self.btn_listar_ventas = ctk.CTkButton(
            self.nav_frame, 
            text="Listar Ventas", 
            command=self.mostrar_listado_ventas,
            width=150,
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.btn_listar_ventas.grid(row=0, column=4, padx=10, pady=10)
        
        # Frame para el contenido
        self.content_frame = ctk.CTkFrame(self.container)
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Centrar el contenido en la ventana
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # Inicializar las vistas
        self.vista_inicio = None
        self.vista_productos = None
        self.vista_clientes = None
        self.vista_ventas = None
        self.vista_listado_ventas = None
        
        # Vista actual
        self.vista_actual = None
        
        # Mostrar la vista de inicio por defecto
        self.mostrar_inicio()
        
        # Etiqueta de pie de página
        self.footer_label = ctk.CTkLabel(
            self.container,
            text="Sistema desarrollado con Python, CustomTkinter y Peewee",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        self.footer_label.pack(pady=10)
    
    def limpiar_contenido(self):
        """Limpia el frame de contenido"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def mostrar_inicio(self):
        """Muestra la vista de inicio"""
        self.limpiar_contenido()
        
        # Crear el frame de inicio
        self.vista_inicio = ctk.CTkFrame(self.content_frame)
        self.vista_inicio.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Contenido de la vista de inicio
        welcome_label = ctk.CTkLabel(
            self.vista_inicio,
            text="Bienvenido al Sistema de Ventas",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        welcome_label.pack(pady=30)
        
        info_text = (
            "Este sistema le permite gestionar productos, clientes y ventas de su tienda.\n\n"
            "Utilice los botones de navegación para acceder a las diferentes funcionalidades\n"
        )
        
        info_label = ctk.CTkLabel(
            self.vista_inicio,
            text=info_text,
            font=ctk.CTkFont(size=14),
            justify="left",
            wraplength=600
        )
        info_label.pack(pady=20)
    
    def mostrar_productos(self):
        """Muestra la vista de productos"""
        self.limpiar_contenido()
        
        # Crear la vista de productos si no existe
        self.vista_productos = ProductoView(self.content_frame)
        self.vista_productos.pack(fill="both", expand=True)
        
        self.vista_actual = "productos"
    
    def mostrar_clientes(self):
        """Muestra la vista de clientes"""
        self.limpiar_contenido()
        
        # Crear la vista de clientes si no existe
        self.vista_clientes = ClienteView(self.content_frame)
        self.vista_clientes.pack(fill="both", expand=True)
        
        self.vista_actual = "clientes"
    
    def mostrar_ventas(self):
        """Muestra la vista de registro de ventas"""
        self.limpiar_contenido()
        
        # Crear la vista de ventas si no existe
        self.vista_ventas = VentaView(self.content_frame, modo_listado=False)
        self.vista_ventas.pack(fill="both", expand=True)
        
        self.vista_actual = "ventas"
    
    def mostrar_listado_ventas(self):
        """Muestra la vista de listado de ventas"""
        self.limpiar_contenido()
        
        # Crear la vista de listado de ventas si no existe
        self.vista_listado_ventas = VentaView(self.content_frame, modo_listado=True)
        self.vista_listado_ventas.pack(fill="both", expand=True)
        
        self.vista_actual = "listado_ventas"