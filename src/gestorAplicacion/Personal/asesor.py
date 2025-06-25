from persona import Persona

class Asesor(Persona):
    def __init__(self, cedula: int, nombre: str, rol: str = "Asesor", id: int = 0, calificacion: float = 0.0):
        super().__init__(cedula, nombre, rol)
        self._id = id
        self._calificacion = calificacion


    #Getters y Setters

    def get_id(self) -> int:
        return self._id

    def set_id(self, nuevo_id: int):
        self._id = nuevo_id

    def get_calificacion(self) -> float:
        return self._calificacion

    def set_calificacion(self, nueva_calificacion: float):
        self._calificacion = nueva_calificacion
