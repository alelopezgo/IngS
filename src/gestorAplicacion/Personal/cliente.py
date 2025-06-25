from Personal.persona import Persona


class Cliente(Persona):
    def __init__(self, cedula: int, nombre: str, rol: str, telefono: int, direccion: str, correo: str):
        super().__init__(cedula, nombre, rol="Cliente")
        self._telefono = telefono
        self._direccion = direccion
        self._correo = correo

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
