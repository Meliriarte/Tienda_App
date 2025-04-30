from models.models import Cliente
import re

class ClienteController:
    """Controlador para la gestión de clientes"""
    
    @staticmethod
    def validar_email(email):
        """
        Valida que el email tenga un formato correcto
        
        Args:
            email (str): Email a validar
            
        Returns:
            bool: True si el email es válido, False en caso contrario
        """
        # Patrón básico para validar email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    @staticmethod
    def crear_cliente(nombre, email):
        """
        Crea un nuevo cliente en la base de datos
        
        Args:
            nombre (str): Nombre del cliente
            email (str): Email del cliente
            
        Returns:
            Cliente: El cliente creado o None si hay error
        """
        try:
            # Validación de datos
            if not nombre or not email:
                raise ValueError("El nombre y el email son obligatorios")
            
            if not ClienteController.validar_email(email):
                raise ValueError("El formato del email no es válido")
                
            # Crear el cliente
            cliente = Cliente.create(
                nombre=nombre,
                email=email
            )
            return cliente
        except ValueError as e:
            # Error de validación
            print(f"Error de validación: {e}")
            return None
        except Exception as e:
            # Error de base de datos u otro error
            print(f"Error al crear cliente: {e}")
            return None
    
    @staticmethod
    def obtener_todos_clientes():
        """
        Obtiene todos los clientes de la base de datos
        
        Returns:
            list: Lista de clientes
        """
        try:
            return list(Cliente.select())
        except Exception as e:
            print(f"Error al obtener clientes: {e}")
            return []
    
    @staticmethod
    def obtener_cliente_por_id(cliente_id):
        """
        Obtiene un cliente por su ID
        
        Args:
            cliente_id (int): ID del cliente
            
        Returns:
            Cliente: El cliente encontrado o None
        """
        try:
            return Cliente.get_by_id(cliente_id)
        except Cliente.DoesNotExist:
            return None
        except Exception as e:
            print(f"Error al obtener cliente: {e}")
            return None