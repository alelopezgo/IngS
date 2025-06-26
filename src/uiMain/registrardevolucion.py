from gestorAplicacion.Administracion.Devolucion import Devolucion
from gestorAplicacion.Administracion.compra import Compra
from gestorAplicacion.Administracion.calzado import Calzado
from gestorAplicacion.Administracion.sede import Sede

SpringStep = Sede()

def registrar_devolucion(sede: Sede):
    try:
        codigo = int(input("Ingrese el número de factura de su compra: "))
        compra = next((c for c in sede.get_compras() if c.get_codigo() == codigo), None)

        if not compra:
            print("Compra no encontrada.")
            return

        productos = compra.get_productos()
        if not productos:
            print("La compra no contiene productos.")
            return

        print("\nProductos comprados:")
        for idx, prod in enumerate(productos, 1):
            modelo = prod.get_modelo()
            print(f"{idx}. {modelo.get_nombre()} ({modelo.get_marca()}) - Talla {prod.get_talla()} - Color {prod.get_color()}")

        idx = int(input("\nSeleccione el número del producto a devolver: ")) - 1
        if idx < 0 or idx >= len(productos):
            print("Selección inválida.")
            return

        producto = productos[idx]
        motivo = input("Ingrese el motivo de devolución: ").strip()
        if not motivo:
            print("Motivo no puede estar vacío.")
            return

        estado_producto = input("Ingrese el estado del producto (nuevo, usado, defectuoso, dañado, deteriorado.): ").strip()

        devolucion = Devolucion(producto, motivo, compra, estado_producto)
        print(devolucion.resumen())

        if devolucion.es_valida():
            sede.registrar_devolucion(devolucion)
            print("Devolución registrada exitosamente.")
        else:
            print("La devolución es inválida.")

    except ValueError:
        print("Entrada inválida. Intente de nuevo.")
