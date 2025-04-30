from peewee import *
import datetime

# Configuración de la base de datos
db = SqliteDatabase('tienda.db')

class BaseModel(Model):
    """Modelo base para heredar la configuración de la base de datos"""
    class Meta:
        database = db

class Producto(BaseModel):
    """Modelo para representar productos en la tienda"""
    nombre = CharField(max_length=100, unique=True)
    precio = FloatField()
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"

class Cliente(BaseModel):
    """Modelo para representar clientes de la tienda"""
    nombre = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.email})"

class Venta(BaseModel):
    """Modelo para representar ventas realizadas"""
    cliente = ForeignKeyField(Cliente, backref='ventas')
    producto = ForeignKeyField(Producto, backref='ventas')
    cantidad = IntegerField()
    fecha = DateTimeField(default=datetime.datetime.now)
    
    @property
    def total(self):
        """Calcula el total de la venta (precio * cantidad)"""
        return self.producto.precio * self.cantidad
    
    def __str__(self):
        return f"Venta a {self.cliente.nombre} - {self.producto.nombre} x{self.cantidad}"

def inicializar_bd():
    """Inicializa la base de datos creando las tablas si no existen"""
    db.connect()
    db.create_tables([Producto, Cliente, Venta])
    print("Base de datos inicializada correctamente.")