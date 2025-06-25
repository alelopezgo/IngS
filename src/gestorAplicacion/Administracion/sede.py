from gestorAplicacion.Personal.cliente import Cliente
from gestorAplicacion.Personal.cajero import Cajero
from gestorAplicacion.Personal.asesor import Asesor
from typing import List

class Sede:
    def __init__(self):
        self._clientes: List[Cliente] = []
        self._asesores: List[Asesor] = []
        self._cajeros: List[Cajero] = []
        self._cedulasClientes = set() #PARA HACER LAS BÚSQUEDAS EN O(1)


    def setCedulas(self):
        return self._cedulasClientes

    def registrarCliente(self, cliente: Cliente):
        self._clientes.append(cliente)
        self._cedulasClientes.add(cliente.getcedula())

    def verificar_cedula_existente(self, cedula: int):
        return cedula in self.setCedulas()

