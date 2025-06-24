from abc import ABC


class persona(ABC):
    def __init__(self, Cedula: int, Nombre: str, Rol: str):
        self.Cedula = Cedula
        self.Nombre = Nombre
        self.Rol = Rol
