import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gestorAplicacion.Administracion.calificacionServicio import CalificacionServicio
from gestorAplicacion.Administracion.sede import Sede

def registrarCalificacionServicio(sede: Sede) -> None:
    print("\n===== CALIFICAR SERVICIO =====")
    cedula = input("Cédula del cliente: ").strip()
    if not cedula.isdigit():
        print("Cédula no válida.")
        return
    cliente = sede.buscar_cliente_por_cedula(int(cedula))
    if not cliente or cliente.get_rol() != "Cliente":
        print("Cliente no encontrado o rol incorrecto.")
        return
    while True:
        valor_str = input("Puntaje (1-5): ").strip()
        if valor_str.isdigit():
            valor = int(valor_str)
            if 1 <= valor <= 5:
                break
        print("Debe ser un número entre 1 y 5.")
    comentario = input("Comentario (opcional): ").strip()
    calificacion = CalificacionServicio(cliente, valor, comentario)
    sede.registrar_calificacion_servicio(calificacion)
    print("\n¡Gracias por calificar nuestro servicio!")
    print(calificacion)
