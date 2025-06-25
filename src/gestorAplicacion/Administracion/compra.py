from gestorAplicacion.Personal.cliente import Cliente
from gestorAplicacion.Personal.cajero import Cajero
from gestorAplicacion.Administracion.calzado import Calzado
import datetime
from typing import List
class Compra:
    def __init__(self,codigo: int,cliente: Cliente,cajero: Cajero,productos: list,medio_pago: str,fecha: datetime):  
        self._codigo = codigo
        self._cliente = cliente
        self._cajero = cajero
        self._productos: List[Calzado]
        self._medio_pago = medio_pago
        self._fecha = fecha

        self._subtotal = self.calcular_subtotal()
        self._descuento = cliente.get_beneficios()
        self._total = self._subtotal - self._descuento

    #Método para subtotal:

    def calcular_subtotal(self):
        return sum(p.get_precio() for p in self._productos)

    #Getters y setters:

    def get_codigo(self):
        return self._codigo

    def set_codigo(self, codigo: int):
        self._codigo = codigo

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente):
        self._cliente = cliente

    def get_cajero(self):
        return self._cajero

    def set_cajero(self, cajero):
        self._cajero = cajero

    def get_productos(self):
        return self._productos

    def set_productos(self, productos: list):
        self._productos = productos
        # Cambiar los totales si se añade un producto
        self._subtotal = self.calcular_subtotal()
        self._total = self._subtotal - self._descuento

    def get_medio_pago(self):
        return self._medio_pago

    def set_medio_pago(self, medio_pago: str):
        self._medio_pago = medio_pago

    def get_fecha(self):
        return self._fecha

    def set_fecha(self, fecha: str):
        self._fecha = fecha

    def get_subtotal(self):
        return self._subtotal

    def set_subtotal(self, subtotal: int):
        self._subtotal = subtotal

    def get_descuento(self):
        return self._descuento

    def set_descuento(self, descuento: int):
        self._descuento = descuento
        self._total = self._subtotal - self._descuento

    def get_total(self):
        return self._total

    def set_total(self, total: int):
        self._total = total
