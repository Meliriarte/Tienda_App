from models.models import Venta, Cliente, Producto
from peewee import JOIN

class VentaController:
    """Controlador para la gestión de ventas"""
    
    @staticmethod
    def crear_venta(cliente_id, producto_id, cantidad):
        """
        Crea una nueva venta en la base de datos
        
        Args:
            cliente_id (int): ID del cliente
            producto_id (int): ID del producto
            cantidad (int): Cantidad de productos vendidos
            
        Returns:
            Venta: La venta creada o None si hay error
        """
        try:
            # Validación de datos
            if not cliente_id or not producto_id or not cantidad:
                raise ValueError("El cliente, producto y cantidad son obligatorios")
            
            cantidad = int(cantidad)
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que cero")
            
            # Verificar que existan el cliente y el producto
            cliente = Cliente.get_by_id(cliente_id)
            producto = Producto.get_by_id(producto_id)
                
            # Crear la venta
            venta = Venta.create(
                cliente=cliente,
                producto=producto,
                cantidad=cantidad
            )
            return venta
        except ValueError as e:
            # Error de validación
            print(f"Error de validación: {e}")
            return None
        except Cliente.DoesNotExist:
            print("El cliente no existe")
            return None
        except Producto.DoesNotExist:
            print("El producto no existe")
            return None
        except Exception as e:
            # Error de base de datos u otro error
            print(f"Error al crear venta: {e}")
            return None
    
    @staticmethod
    def obtener_todas_ventas():
        """
        Obtiene todas las ventas de la base de datos con información detallada
        
        Returns:
            list: Lista de ventas con información detallada
        """
        try:
            # Consulta con join para obtener datos relacionados
            ventas = (Venta
                     .select(Venta, Cliente, Producto)
                     .join(Cliente)
                     .switch(Venta)
                     .join(Producto)
                     .order_by(Venta.fecha.desc()))
            
            # Convertir a lista de diccionarios para facilitar su uso en la vista
            resultado = []
            for venta in ventas:
                resultado.append({
                    'id': venta.id,
                    'fecha': venta.fecha.strftime('%Y-%m-%d %H:%M'),
                    'cliente_nombre': venta.cliente.nombre,
                    'producto_nombre': venta.producto.nombre,
                    'cantidad': venta.cantidad,
                    'precio_unitario': venta.producto.precio,
                    'total': venta.total
                })
            
            return resultado
        except Exception as e:
            print(f"Error al obtener ventas: {e}")
            return []