from gestorAplicacion.Administracion.calzado import Calzado
from gestorAplicacion.Personal.cajero import Cajero
from gestorAplicacion.Personal.cliente import Cliente
from gestorAplicacion.Administracion.compra import Compra
from gestorAplicacion.Administracion.sede import Sede
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


SpringStep = Sede()  # Simulación de instancia de sede


def registrarCompra(sede: Sede, cajero: Cajero):
    print("\n===== REGISTRAR COMPRA =====\n")

    # 1. INGRESAR CÉDULA DEL CLIENTE
    while True:
        cedula = input("Ingrese la cédula del cliente: ")
        if not cedula.isdigit():
            print("La cédula debe contener solo números.")
            continue
        cedula = int(cedula)
        break

    # Verificar si el cliente existe
    if not sede.verificar_cedula_existente(cedula):
        print("El cliente no está registrado en la sede.")
        return

    cliente = next(c for c in sede._clientes if c.get_cedula() == cedula)

    # 2. CREAR OBJETO COMPRA (vacío aún)
    # Medio de pago se añade después
    compra = Compra(cliente=cliente, cajero=cajero, medio_pago="")

    # 3. SELECCIÓN DE PRODUCTOS
    while True:
        print("\n--- Inventario disponible ---")
        productos = sede.get_productos()

        if not productos:
            print("No hay productos disponibles en el inventario.")
            return

        for i, p in enumerate(productos, start=1):
            modelo = p.get_modelo()
            print(f"{i}. Modelo: {modelo.get_nombre()} | Marca: {modelo.get_marca()} | "
                  f"Talla: {p.get_talla()} | Color: {p.get_color()} | Precio: ${p.get_precio()}")

        seleccion = input(
            "\nSeleccione el número del producto a agregar (o escriba 'fin' para terminar): ").strip()

        if seleccion.lower() == "fin":
            break

        if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(productos)):
            print("Selección inválida.")
            continue

        idx = int(seleccion) - 1
        producto = productos[idx]

        # Agregar producto a la compra
        compra.agregar_producto(producto)
        print("Producto agregado con éxito.")

    # Validación de que haya al menos un producto
    if not compra.get_productos():
        print("No se registró ningún producto. Compra cancelada.")
        return

    # 4. INGRESAR MEDIO DE PAGO
    while True:
        medio = input("Medio de pago (efectivo/tarjeta): ").strip().lower()
        compra.set_medio_pago(medio)

        if not compra.validar_medio_pago():
            print("Medio de pago inválido. Solo se permite 'efectivo' o 'tarjeta'.")
        else:
            break

    # 5. VALIDACIÓN FINAL DE CAMPOS
    if not compra.validar_campos_requeridos():
        print("Faltan campos requeridos. No se puede continuar.")
        return

    # 6. DESCUENTO AUTOMÁTICO
    compra.aplicar_descuento_por_historial(sede)

    # 7. CALCULAR TOTALES
    compra.calcular_total()

    # 8. MODIFICACIONES ANTES DE FINALIZAR
    while True:
        modificar = input(
            "\n¿Desea modificar la compra antes de finalizar? (s/n): ").lower()
        if modificar == 's':
            print("Productos actuales:")
            for i, p in enumerate(compra.get_productos(), 1):
                print(
                    f"{i}. {p.get_modelo().get_nombre()} - Talla {p.get_talla()} - ${p.get_precio()}")

            opcion = input(
                "Ingrese el número del producto a eliminar o 'cancelar' para salir: ").strip()
            if opcion.lower() == 'cancelar':
                break

            if opcion.isdigit() and 1 <= int(opcion) <= len(compra.get_productos()):
                producto = compra.get_productos()[int(opcion)-1]
                compra.eliminar_producto(producto)
                print("Producto eliminado.")
            else:
                print("Opción inválida.")
        else:
            break

    # Verificación final
    if not compra.validar_campos_requeridos():
        print("Compra incompleta después de modificaciones. Proceso cancelado.")
        return

    # 9. REGISTRAR COMPRA EN LA SEDE
    sede.registrar_compra(compra)

    # 10. MOSTRAR FACTURA
    print("\n===== FACTURA FINAL =====")
    print(compra.generar_factura())
