from gestorAplicacion.Personal.persona import Persona

from typing import List
import re

class Cliente(Persona):
    def __init__(self, cedula: int, nombre: str, rol: str, telefono: int, direccion: str, correo: str, compras_previas):
        super().__init__(cedula, nombre, rol="Cliente")
        self._telefono = telefono
        self._direccion = direccion
        self._correo = correo
        self._compras_previas = compras_previas

    
    @classmethod
    def validar_celular(cls, celular: str) -> bool:
        return celular.isdigit() and len(celular) == 10 and celular.startswith("3")
    
    @classmethod
    def validar_correo(cls, correo: str) -> bool:
        if correo.strip() == "":
            return True  # campo opcional

        patron = r'^[\w\.-]+@([\w\.-]+\.\w+)$'
        match = re.fullmatch(patron, correo.strip())

        if not match:
            return False

        dominio = match.group(1).lower()

        dominios_permitidos = {
            'gmail.com',
            'hotmail.com',
            'outlook.com',
            'yahoo.es'
        }

        # Acepta dominios universitarios que terminan en .edu.co
        if dominio in dominios_permitidos or dominio.endswith('.edu.co'):
            return True

        return False
    
    @classmethod
    def validar_direccion(cls, direccion: str) -> bool:
        if direccion.strip() == "":
            return True  # Campo opcional

        # Letras, números, espacios, puntos, comas, guiones y numeral
        patron = r'^[a-zA-Z0-9\s\.,\-#]+$'
        return bool(re.fullmatch(patron, direccion.strip()))
    
        
    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono: str):
        self._telefono = telefono

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion: str):
        self._direccion = direccion

    def get_correo(self):
        return self._correo

    def set_correo(self, correo: str):
        self._correo = correo

    def get_compras_previas(self):
        return self._compras_previas
    
    def set_compras_previas(self, compras_previas):
        self._compras_previas = compras_previas
    