# Sistema de Ventas para Tienda

Este proyecto implementa un sistema de ventas para una tienda utilizando Python con CustomTkinter para la interfaz gráfica, Peewee como ORM para el manejo de base de datos y siguiendo el patrón de arquitectura MVC (Modelo-Vista-Controlador).

---

## Características

- Registro de productos con nombre y precio
- Registro de clientes con nombre y correo electrónico
- Registro de ventas, asociando un cliente con un producto y la cantidad comprada
- Visualización de un listado de ventas realizadas, con su fecha y total

---

## Estructura del Proyecto

El proyecto sigue el patrón MVC con la siguiente estructura:

\`\`\`
tienda_app/
│
├── models/
│   └── models.py           # Definición de la base de datos y modelos con Peewee
│
├── views/
│   ├── main_view.py        # Ventana principal (CustomTkinter)
│   ├── producto_view.py    # Formulario para agregar productos
│   ├── cliente_view.py     # Formulario para agregar clientes
│   └── venta_view.py       # Formulario para registrar ventas
│
├── controllers/
│   ├── producto_controller.py  # Lógica para productos
│   ├── cliente_controller.py   # Lógica para clientes
│   └── venta_controller.py     # Lógica para ventas
│
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del proyecto
└── tienda.db               # Archivo SQLite generado automáticamente
\`\`\`

---

## Uso

### Gestión de Productos

- Permite agregar nuevos productos con nombre y precio
- Muestra una lista de todos los productos registrados

### Gestión de Clientes

- Permite agregar nuevos clientes con nombre y correo electrónico
- Muestra una lista de todos los clientes registrados

### Registro de Ventas

- Permite seleccionar un cliente y un producto de los registrados
- Calcula automáticamente el total basado en el precio del producto y la cantidad
- Registra la venta con la fecha actual

### Listado de Ventas

- Muestra todas las ventas realizadas con detalles como:
  - Fecha y hora
  - Cliente
  - Producto
  - Cantidad
  - Precio unitario
  - Total

---

## Patrón MVC

### Modelo (Model)

- Define las tablas: Producto, Cliente, Venta
- Conecta a la base de datos SQLite
- Relaciona las tablas con claves foráneas

### Vista (View)

- Implementada con CustomTkinter
- Formularios para ingresar productos, clientes y ventas
- Pantallas para listar ventas y mostrar datos al usuario

### Controlador (Controller)

- Contiene la lógica de negocio
- Valida entradas
- Coordina la interacción entre vista y modelo
