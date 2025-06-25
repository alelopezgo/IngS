import persona

class Cajero(persona):
    def __init__(self, cedula: int, nombre: str, rol: str, id: int):
        super().__init__(cedula, nombre, rol = "Cajero")
        self._id = id

    def get_id(self):
        return self._id

    def set_id(self, id: int):
        self._id = id

    
        

        
