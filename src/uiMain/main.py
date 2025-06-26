from registrarcliente import registrarCliente
from gestorAplicacion.Administracion.sede import Sede
from registrarcompra import registrarCompra
from registrardevolucion import registrar_devolucion
from gestorAplicacion.Personal.cajero import Cajero
from gestorAplicacion.Personal.cliente import Cliente
from gestorAplicacion.Administracion.calzado import Calzado
from gestorAplicacion.Administracion.modeloCalzado import ModeloCalzado
from gestorAplicacion.Administracion.compra import Compra
from gestorAplicacion.Administracion.Devolucion import Devolucion

SpringStep = Sede()

# Crear cliente y cajero
cliente = Cliente(nombre="Alejandro Lopez",cedula=1001506186, rol="Cliente", telefono=3207078279, direccion="", correo="", compras_previas=[])
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

# Mostrar factura (opcional)
#print(compra1.generar_factura())

# Llamar al flujo de devolución
#registrar_devolucion(SpringStep)


#registrarCompra(SpringStep, cajero)