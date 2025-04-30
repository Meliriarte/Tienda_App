import customtkinter as ctk
from controllers.cliente_controller import ClienteController
from CTkMessagebox import CTkMessagebox

class ClienteView(ctk.CTkFrame):
    """Vista para la gestión de clientes"""
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # Crear el contenedor principal
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título
        self.title_label = ctk.CTkLabel(
            self.container, 
            text="Gestión de Clientes", 
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
        
        self.lbl_email = ctk.CTkLabel(form_container, text="Email:")
        self.lbl_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        self.entry_email = ctk.CTkEntry(form_container, width=300)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)
        
        # Botón para guardar
        self.btn_guardar = ctk.CTkButton(
            form_container, 
            text="Guardar Cliente", 
            command=self.guardar_cliente
        )
        self.btn_guardar.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
        
        # Frame para la lista de clientes
        self.list_frame = ctk.CTkFrame(self.container)
        self.list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Título de la lista
        self.list_title = ctk.CTkLabel(
            self.list_frame, 
            text="Clientes Registrados", 
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.list_title.pack(pady=10)
        
        # Crear la tabla (usando un widget Text para simular una tabla)
        self.tabla = ctk.CTkTextbox(self.list_frame, height=200)
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Cargar los clientes existentes
        self.cargar_clientes()
    
    def guardar_cliente(self):
        """Guarda un nuevo cliente en la base de datos"""
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()
        
        # Validar que los campos no estén vacíos
        if not nombre or not email:
            CTkMessagebox(
                title="Error", 
                message="Todos los campos son obligatorios", 
                icon="cancel"
            )
            return
        
        # Intentar guardar el cliente
        cliente = ClienteController.crear_cliente(nombre, email)
        
        if cliente:
            CTkMessagebox(
                title="Éxito", 
                message=f"Cliente '{nombre}' guardado correctamente", 
                icon="check"
            )
            # Limpiar los campos
            self.entry_nombre.delete(0, 'end')
            self.entry_email.delete(0, 'end')
            # Recargar la lista de clientes
            self.cargar_clientes()
        else:
            CTkMessagebox(
                title="Error", 
                message="No se pudo guardar el cliente. Verifique que el email sea válido y no exista otro cliente con el mismo email.", 
                icon="cancel"
            )
    
    def cargar_clientes(self):
        """Carga y muestra los clientes existentes"""
        # Limpiar la tabla
        self.tabla.delete('1.0', 'end')
        
        # Obtener todos los clientes
        clientes = ClienteController.obtener_todos_clientes()
        
        # Mostrar encabezados
        self.tabla.insert('end', f"{'ID':<5} {'Nombre':<25} {'Email':<30}\n")
        self.tabla.insert('end', "-" * 60 + "\n")
        
        # Mostrar cada cliente
        for cliente in clientes:
            self.tabla.insert('end', f"{cliente.id:<5} {cliente.nombre:<25} {cliente.email:<30}\n")