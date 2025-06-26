from registrarCliente import registrarCliente
from gestorAplicacion.Administracion.sede import Sede
from registrarcompra import registrarCompra
from registrardevolucion import registrar_devolucion
from registrarCalificacion import registrarCalificacion
from registrarCalificacionServicio import registrarCalificacionServicio
from gestorAplicacion.Personal.cajero import Cajero
from gestorAplicacion.Personal.cliente import Cliente
from gestorAplicacion.Administracion.calzado import Calzado
from gestorAplicacion.Administracion.modeloCalzado import ModeloCalzado
from gestorAplicacion.Administracion.compra import Compra
from gestorAplicacion.Administracion.Devolucion import Devolucion

SpringStep = Sede()

# Crear cliente y cajero
cliente = Cliente(nombre="Alejandro Lopez", cedula=1001506186, telefono=3207078279, direccion="", correo="", compras_previas=[])
cajero = Cajero(cedula=123456789, nombre="Alejandro Lopez", rol="Cajero", id=1)

# Registrar cliente en la sede
SpringStep.registrarCliente(cliente)

# Crear modelo y productos
modelo1 = ModeloCalzado(nombre="AirZoom", marca="Nike")
producto1 = Calzado(modelo=modelo1, talla=42, color="Negro", precio=250000)
producto2 = Calzado(modelo=modelo1, talla=41, color="Blanco", precio=230000)

SpringStep.registrar_producto(producto1)

# Crear compra y agregar productos
compra1 = Compra(cliente=cliente, cajero=cajero, medio_pago="efectivo")
compra1.agregar_producto(producto1)
compra1.agregar_producto(producto2)

# Registrar compra en la sede
SpringStep.registrar_compra(compra1)

#Mostrar factura (opcional)
#print(compra1.generar_factura())

# Llamar al flujo de devolución
#registrar_devolucion(SpringStep)

#registrarCompra(SpringStep, cajero)

#registrarCalificacion(SpringStep)"""

def menu_cliente():
    while True:
        print("\n--- Menú Cliente ---")
        print("1. Calificación Producto.")
        print("2. Calificación Servicio.")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrarCalificacion(SpringStep)
        elif opcion == "2":
            registrarCalificacionServicio(SpringStep)
        elif opcion == "0":
            print("Saliendo del menú cliente.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_cajero():
    while True:
        print("\n--- Menú Cajero ---")
        print("1. Registrar Cliente.")
        print("2. Registrar Compra.")
        print("3. Registrar Devolución")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Registrando Cliente...")
            registrarCliente(SpringStep)
        elif opcion == "2":
            print("Registrando Compra...")
            registrarCompra(SpringStep, cajero)
        elif opcion == "3":
            print("Registrando Devolución...")
            registrar_devolucion(SpringStep)
        elif opcion == "0":
            print("Saliendo del menú cajero.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_principal():
    while True:
        print("\n=== Bienvenido al sistema ===")
        print("¿Es usted cliente o cajero?")
        print("1. Cliente")
        print("2. Cajero")
        print("0. Salir del sistema")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_cliente()
        elif opcion == "2":
            menu_cajero()
        elif opcion == "0":
            print("Gracias por usar el sistema. Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar menú principal
menu_principal()
