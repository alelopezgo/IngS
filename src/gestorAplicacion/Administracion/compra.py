from datetime import datetime
from gestorAplicacion.Personal.cliente import Cliente
from gestorAplicacion.Personal.cajero import Cajero
from gestorAplicacion.Administracion.calzado import Calzado
from typing import List


class Compra:
    _contador_codigos = 1  # Atributo de clase para generar códigos únicos

    def __init__(self, cliente: Cliente, cajero: Cajero, medio_pago: str):
        self._codigo = Compra._contador_codigos
        Compra._contador_codigos += 1

        self._cliente = cliente
        self._cajero = cajero
        self._medio_pago = medio_pago.lower()
        self._fecha = datetime.now()

        self._productos: List[Calzado] = []
        self._subtotal: float = 0.0
        self._descuento: float = 0.0
        self._total: float = 0.0

    # ==== Getters y Setters ====

    def get_codigo(self):
        return self._codigo

    def get_cliente(self):
        return self._cliente

    def get_cajero(self):
        return self._cajero

    def get_medio_pago(self):
        return self._medio_pago

    def set_medio_pago(self, medio: str):
        self._medio_pago = medio.lower()

    def get_fecha(self):
        return self._fecha

    def get_productos(self):
        return self._productos

    def get_subtotal(self):
        return self._subtotal

    def get_descuento(self):
        return self._descuento

    def get_total(self):
        return self._total

    # ==== Métodos funcionales ====

    def agregar_producto(self, producto: Calzado):
        if producto not in self._productos:
            self._productos.append(producto)
            self.calcular_subtotal()
            self.calcular_total()

    def eliminar_producto(self, producto: Calzado):
        if producto in self._productos:
            self._productos.remove(producto)
            self.calcular_subtotal()
            self.calcular_total()

    def calcular_subtotal(self):
        self._subtotal = sum([p.get_precio() for p in self._productos])

    def aplicar_descuento_por_historial(self, compras_previas: List['Compra']):
        if compras_previas:
            ultima_compra = compras_previas[-1]
            self._descuento = ultima_compra.get_total() * 0.08
        else:
            self._descuento = 0.0

    def calcular_total(self):
        self._total = self._subtotal - self._descuento

    def validar_medio_pago(self) -> bool:
        return self._medio_pago in ["efectivo", "tarjeta"]

    def validar_campos_requeridos(self) -> bool:
        return bool(self._productos) and self._medio_pago in ["efectivo", "tarjeta"]

    def generar_factura(self) -> str:
        factura = f"----- FACTURA #{self._codigo} -----\n"
        factura += f"Fecha: {self._fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
        factura += f"Cliente: {self._cliente.get_nombre()} - CC: {self._cliente.get_cedula()}\n"
        factura += f"Cajero: {self._cajero.get_nombre()} (ID: {self._cajero.get_id()})\n"
        factura += f"Medio de pago: {self._medio_pago.capitalize()}\n"
        factura += f"\nProductos:\n"
        for p in self._productos:
            factura += f" - {p.get_tipo()} | Talla: {p.get_talla()} | Color: {p.get_color()} | Precio: ${p.get_precio()}\n"
        factura += f"\nSubtotal: ${self._subtotal:.2f}\n"
        factura += f"Descuento aplicado: ${self._descuento:.2f}\n"
        factura += f"Total a pagar: ${self._total:.2f}\n"
        factura += "-----------------------------"
        return factura
