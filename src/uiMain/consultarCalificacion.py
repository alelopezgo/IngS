import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gestorAplicacion.Administracion.calificacionProducto import Calificacion
from gestorAplicacion.Administracion.sede import Sede
from gestorAplicacion.Personal.cajero import Cajero
from gestorAplicacion.Personal.cliente import Cliente
from gestorAplicacion.Administracion.compra import Compra
from gestorAplicacion.Administracion.calzado import Calzado
from gestorAplicacion.Administracion.modeloCalzado import ModeloCalzado
from datetime import datetime

def consultarCalificacion(sede: Sede ):
    print("\n=====  CONSULTA CALIFICACIÓN ====\n")

    # Validar cédula
    while True:
        cedula = input("Ingrese el número de cédula del cliente (opcional): ")
        if not cedula or cedula.isdigit():
            break
        print("La cédula debe ser numérica o dejarse vacía.")

    nombreProducto = input("Ingrese el nombre del producto (opcional): ")

    # Validar código
    while True:
        codigo = input("Ingrese el código del producto (opcional): ")
        if not codigo or codigo.isdigit():
            break
        print("El código debe ser numérico o dejarse vacío.")

    # Validar fecha inicial
    while True:
        fechaInicial = input("Ingrese la fecha inicial (YYYY-MM-DD) (opcional): ")
        if not fechaInicial:
            break
        try:
            datetime.strptime(fechaInicial, "%Y-%m-%d")
            break
        except ValueError:
            print("La fecha inicial no tiene el formato correcto (YYYY-MM-DD).")

    # Validar fecha final
    while True:
        fechaFinal = input("Ingrese la fecha final (YYYY-MM-DD) (opcional): ")
        if not fechaFinal:
            break
        try:
            datetime.strptime(fechaFinal, "%Y-%m-%d")
            break
        except ValueError:
            print("La fecha final no tiene el formato correcto (YYYY-MM-DD).")

    calificaciones = sede.consultar_calificacion(
        int(cedula) if cedula else None,
        nombreProducto if nombreProducto else None,
        codigo if codigo else None,
        fechaInicial if fechaInicial else None,
        fechaFinal if fechaFinal else None
    )
    prom = 0
    if not calificaciones or len(calificaciones) == 0:
        print("No se encontraron calificaciones con los criterios especificados.")
        return
    for calificacion in calificaciones:
        prom = prom + calificacion.get_valor()
        print(f"Cliente: {calificacion.get_cliente().get_nombre()}, Producto: {calificacion.get_producto().get_modelo().get_nombre()}, Valor: {calificacion.get_valor()}, Comentario: {calificacion.get_comentario()}")
        print(f"Fecha: {calificacion.get_fecha()}")
    if len(calificaciones) > 0:
        prom = prom / len(calificaciones)
    print(f"Promedio de calificaciones: {prom:.2f}")