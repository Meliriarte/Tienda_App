from models.models import Producto

class ProductoController:
    """Controlador para la gestión de productos"""
    
    @staticmethod
    def crear_producto(nombre, precio):
        """
        Crea un nuevo producto en la base de datos
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio del producto
            
        Returns:
            Producto: El producto creado o None si hay error
        """
        try:
            # Validación de datos
            if not nombre or not precio:
                raise ValueError("El nombre y el precio son obligatorios")
            
            if float(precio) <= 0:
                raise ValueError("El precio debe ser mayor que cero")
                
            # Crear el producto
            producto = Producto.create(
                nombre=nombre,
                precio=float(precio)
            )
            return producto
        except ValueError as e:
            # Error de validación
            print(f"Error de validación: {e}")
            return None
        except Exception as e:
            # Error de base de datos u otro error
            print(f"Error al crear producto: {e}")
            return None
    
    @staticmethod
    def obtener_todos_productos():
        """
        Obtiene todos los productos de la base de datos
        
        Returns:
            list: Lista de productos
        """
        try:
            return list(Producto.select())
        except Exception as e:
            print(f"Error al obtener productos: {e}")
            return []
    
    @staticmethod
    def obtener_producto_por_id(producto_id):
        """
        Obtiene un producto por su ID
        
        Args:
            producto_id (int): ID del producto
            
        Returns:
            Producto: El producto encontrado o None
        """
        try:
            return Producto.get_by_id(producto_id)
        except Producto.DoesNotExist:
            return None
        except Exception as e:
            print(f"Error al obtener producto: {e}")
            return None