from gestorAplicacion.Personal.cliente import Cliente
from gestorAplicacion.Personal.cajero import Cajero
from gestorAplicacion.Personal.asesor import Asesor
from Administracion.compra import Compra
from typing import List

class Sede:
    def __init__(self):
        self._clientes: List[Cliente] = []
        self._asesores: List[Asesor] = []
        self._cajeros: List[Cajero] = []
        self._compras: List[Compra] = []
        self._cedulasClientes = set() #PARA HACER LAS BÚSQUEDAS EN O(1)


    def setCedulas(self):
        return self._cedulasClientes

    def registrarCliente(self, cliente: Cliente):
        self._clientes.append(cliente)
        self._cedulasClientes.add(cliente.getcedula())

    def verificar_cedula_existente(self, cedula: int):
        return cedula in self.setCedulas()
    
    def registrar_compra(self, compra: Compra):
        self._compras.append(compra)
    
    def obtener_compras_cliente(self, cedula_cliente: int) -> List[Compra]:
        return [c for c in self._compras if c.get_cliente().get_cedula() == cedula_cliente]

    


