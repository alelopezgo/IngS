import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gestorAplicacion.Personal.persona import Persona
from gestorAplicacion.Personal.cliente import Cliente
from gestorAplicacion.Administracion.sede import Sede

# FUNCIONES REUTILIZABLES

def pedir_cedula():
    while True:
        cedula = input("Cédula: ").strip()
        if not Persona.validar_cedula(cedula):
            print("Cédula inválida: debe contener solo dígitos y tener entre 6 y 10 caracteres.\n")
        else:
            return int(cedula)

def pedir_nombre():
    while True:
        nombre = input("Nombre: ").strip()
        if not Persona.validar_nombre(nombre):
            print("nombre inválido: no se permiten números ni caracteres especiales.\n")
        else:
            return nombre

def pedir_celular():
    while True:
        celular = input("Celular: ").strip()
        if not Cliente.validar_celular(celular):
            print("número celular inválido. Debe tener 10 dígitos y comenzar con 3.\n")
        else:
            return int(celular)

def pedir_correo():
    while True:
        correo = input("Correo (opcional): ").strip()
        if not Cliente.validar_correo(correo):
            print("Correo inválido: solo se aceptan direcciones Gmail, Hotmail, Outlook, Yahoo.es o .edu.co\n")
        else:
            return correo

def pedir_direccion():
    while True:
        direccion = input("Dirección (opcional): ").strip()
        if not Cliente.validar_direccion(direccion):
            print("Dirección inválida: solo se permiten letras, números, espacios, puntos (.), comas (,), guiones (-) y numeral (#).\n")
        else:
            return direccion



def registrarCliente(sede: Sede):
    print("\n=====  REGISTRO CLIENTE ====\n")

    datos = {
        "cedula": pedir_cedula()
    }

    if sede.verificar_cedula_existente(datos["cedula"]):
        print("No se puede continuar: el cliente ya se encuentra registrado.\n")
        return

    # Resto de datos
    datos["nombre"] = pedir_nombre()
    datos["celular"] = pedir_celular()
    datos["correo"] = pedir_correo()
    datos["direccion"] = pedir_direccion()

    # Mostrar resumen
    print("\nResumen de datos ingresados:")
    for campo, valor in datos.items():
        print(f" - {campo.capitalize()}: {valor if valor else '(vacío)'}")

    # Opción de edición
    while True:
        opcion = input("\n¿Desea editar algún dato? Ingrese:\n1 - Cédula\n2 - Nombre\n3 - Celular\n4 - Correo\n5 - Dirección\n0 - Continuar\nOpción: ").strip()
        if opcion == "1":
            datos["cedula"] = pedir_cedula()
        elif opcion == "2":
            datos["nombre"] = pedir_nombre()
        elif opcion == "3":
            datos["celular"] = pedir_celular()
        elif opcion == "4":
            datos["correo"] = pedir_correo()
        elif opcion == "5":
            datos["direccion"] = pedir_direccion()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

    # Crear cliente
    nuevo_cliente = Cliente(
        datos["cedula"], datos["nombre"],
        datos["celular"], datos["direccion"], datos["correo"]
    )

    # Mostrar datos ingresados
    print("\nResumen de datos ingresados:")
    for campo, valor in datos.items():
        print(f" - {campo.capitalize()}: {valor if valor else '(vacío)'}")

    sede.registrarCliente(nuevo_cliente)
    print("\nCliente registrado exitosamente.\n")


# =========== PRUEBAS ===============

SpringStep = Sede()

#while True:
#    registrarCliente(SpringStep)
