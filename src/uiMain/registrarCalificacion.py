import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gestorAplicacion.Administracion.calificacionProducto import Calificacion
from gestorAplicacion.Administracion.sede import Sede
from gestorAplicacion.Personal.cajero import Cajero
from gestorAplicacion.Personal.persona import Persona
from gestorAplicacion.Personal.cliente import Cliente
from gestorAplicacion.Administracion.compra import Compra
from gestorAplicacion.Administracion.calzado import Calzado
from gestorAplicacion.Administracion.modeloCalzado import ModeloCalzado

def registrarCalificacion(sede: Sede ):

    print("\n=====  REGISTRO CALIFICACIÓN ====\n")
    cliente = None
    producto = None
    valor = None
    comentario = None

    cedula = input("Ingrese el número de cédula del cliente: ")
    clienteExiste = sede.buscar_cliente_por_cedula(int(cedula))
    if not clienteExiste:
        print("El cliente no se encuentra registrado en el sistema. No se puede registrar calificación.")
        return
    
    if clienteExiste.get_rol() != "Cliente":
        print("El Rol no es de cliente. No puede registrar calificación.")
        return
    cliente = clienteExiste

    comprasCliente = sede.obtener_compras_cliente(int(cedula))
    if not comprasCliente or len(comprasCliente) == 0:
        print("El cliente no tiene compras registradas. No se puede registrar calificación.")
        return
    codigoProducto = input("Ingrese el código del producto: ")
    producto = None
    for compra in comprasCliente:
        for prod in compra.get_productos():
            if prod.get_modelo().get_codigo() == int(codigoProducto):
                producto = prod
                break
        if producto:
            break

    if not producto:
        print("El producto no fue encontrado en las compras del cliente.")
        return
    valor = input("Ingrese el valor de la calificación (1-5): ")
    while True:
        if valor.isdigit() and 1 <= int(valor) <= 5:
            break
        valor = input("Valor de calificación inválido. Debe ser un número entre 1 y 5. Intente nuevamente: ")
    
    comentario = input("Ingrese un comentario (opcional): ")
    calificacion = Calificacion(cliente, producto, int(valor), comentario)
    sede.registrar_calificacion(calificacion)
    print("Calificación registrada exitosamente.")
    print(f"Cliente: {cliente.get_nombre()}, Producto: {producto.get_modelo().get_nombre()}, Valor: {calificacion.get_valor()}, Comentario: {calificacion.get_comentario()}")
    print(f"Fecha: {calificacion.get_fecha()}")
    
# # Ejemplo de uso
# # Crear instancia de Sede
# sede = Sede()

# # Crear modelos y productos de ejemplo
# modelo1 = ModeloCalzado(1, "zapato X", "adidas")
# modelo2 = ModeloCalzado(2, "zapato Y", "nike")
# producto1 = Calzado(modelo1,9,"blanco",100000)
# producto2 = Calzado(modelo2,10,"negro",150000)

# # Crear clientes de ejemplo
#  # Crear un cliente
# cliente1 = Cliente(
#         cedula=123456789,
#         nombre="Juan Perez",
#         rol="Cliente",
#         telefono=3123456789,
#         direccion="Calle 123 #45-67",
#         correo="juan.perez@gmail.com"
#     )
# cliente2 = Cliente(
#         cedula=187654389,
#         nombre="Juana Perez",
#         rol="Cliente",
#         telefono=2123456789,
#         direccion="Calle 123 #45-67",
#         correo="juana.perez@gmail.com"
#     )

# # Registrar clientes en la sede
# sede.registrarCliente(cliente1)
# sede.registrarCliente(cliente2)

# # Crear compras de ejemplo y asociar productos
# cajero = Cajero(
#     cedula=987654321,
#     nombre="Laura Gómez",
#     rol="Cajero",
#     id=1
# )
# compra1 = Compra(cliente1,cajero, "efectivo")
# compra2 = Compra(cliente2,cajero, "tarjeta")

# compra1.agregar_producto(producto1)
# compra2.agregar_producto(producto2)
# # Registrar compras en la sede
# sede.registrar_compra(compra1)
# sede.registrar_compra(compra2)
# registrarCalificacion(sede)