import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gestorAplicacion.Personal.persona import Persona
from gestorAplicacion.Personal.cliente import Cliente
from gestorAplicacion.Administracion.sede import Sede

SpringStep = Sede()

def registrarCliente(sede: Sede ):
    SringStep = sede

    print("\n=====  REGISTRO CLIENTE ====\n")
    nombre = None
    cedula = None
    celular = None
    correo = None
    direccion = None

    while True:
         cedula = input("Cedula: ")

        # VALIDAR FORMATO CÉDULA      
         if  not Persona.validar_cedula(cedula):
            print("CC inválida: debe contener solo dígitos y tener entre 6 y 10 caracteres.\n")
            continue
         
         else: break
         
    cedula = int(cedula)

    # VALIDAR SI EL CLIENTE SE ENCUENTRA REGISTRADO
    if SpringStep.verificar_cedula_existente(cedula):
        print("No se puede continuar con el registro, debido a que el cliente ya se encuentra en el sistema.\n")

    else:
        while True:
            nombre = input("Nombre: ")

            # VALIDAR FORMATO NOMBRE
            if not Persona.validar_nombre(nombre):
                print("nombre inválido: no se permiten números ni caracteres especiales, intente de nuevo.\n")
                continue

            else: break

        while True:
            celular = input("Celular: ")

            # VALIDAR FORMATO DE CELULAR
            if not Cliente.validar_celular(celular):
                print("Numero celular inválido, intente de nuevo.\n")

            else: break

        while True:
            correo = input("Correo (opcional): ")

            #VALIDAR FORMATO DE CORREO
            if not Cliente.validar_correo(correo):
                print("Correo inválido: solo se aceptan direcciones de Gmail, Hotmail, Outlook, Yahoo.es o universidades .edu.co\n")

            else: break

        while True:
            direccion = input("Dirección (opcional): " \
            "): ")

            #VALIDAR FORMATO
            if not Cliente.validar_direccion(direccion):
                print("Dirección inválida: contiene caracteres no permitidos, intente de nuevo.")

            else:
                break

# PRUEBAS
registrarCliente(SpringStep)