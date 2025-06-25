from abc import ABC
import re

class Persona(ABC):
    def __init__(self, cedula: int, nombre: str, rol: str):
        self._nombre = nombre
        self._cedula = cedula
        self._rol = rol

    def get_cedula(self):
        return self._cedula

    def set_cedula(self, cedula: int):
        self._cedula = cedula

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_rol(self):
        return self._rol

    def set_rol(self, rol: str):
        self._rol = rol


    @classmethod
    def validar_nombre(cls, nombre: str) -> bool:
        patron = r'^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$'
        return bool(re.fullmatch(patron, nombre.strip())) and nombre.strip() != ""
    
    @classmethod
    def validar_cedula(cls, cedula: str) -> bool:
        return cedula.isdigit() and 6 <=len(cedula) <=10
    