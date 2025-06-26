
from datetime import datetime

class Calificacion:
    def __init__(self, cliente, producto, valor, comentario):
        self.cliente   = cliente
        self.producto  = producto
        self.valor     = valor
        self.comentario= comentario
        self.fecha     = datetime.now()

    # Getters
    def get_cliente(self):
        return self.cliente

    def get_producto(self):
        return self.producto

    def get_valor(self):
        return self.valor

    def get_comentario(self):
        return self.comentario

    def get_fecha(self):
        return self.fecha

    # Setters
    def set_cliente(self, cliente):
        self.cliente = cliente

    def set_producto(self, producto):
        self.producto = producto

    def set_valor(self, valor):
        self.valor = valor

    def set_comentario(self, comentario):
        self.comentario = comentario

    def set_fecha(self, fecha):
        self.fecha = fecha