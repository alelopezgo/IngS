from gestorAplicacion.Personal.persona import Persona

class Cajero(Persona):
    def __init__(self, cedula: int, nombre: str, rol: str, id: int):
        super().__init__(cedula, nombre, rol="Cajero")
        self._id = id
        self._compras_registradas = []  # Lista de compras que ha registrado
        self._cantidad_ventas = 0      

    #Getters y setters

    def get_id(self):
        return self._id

    def set_id(self, id: int):
        self._id = id

    def get_compras_registradas(self):
        return self._compras_registradas

    def get_cantidad_ventas(self):
        return len(self._compras_registradas)


    #Funcion para registrar compras

    def registrar_compra(self, compra):
        self._compras_registradas.append(compra)
        




    
        

        
