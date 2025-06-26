from gestorAplicacion.Personal.cliente import Cliente
from gestorAplicacion.Personal.cajero import Cajero
from gestorAplicacion.Personal.asesor import Asesor
from gestorAplicacion.Administracion.compra import Compra
from gestorAplicacion.Administracion.calificacionProducto import Calificacion
from gestorAplicacion.Administracion.Devolucion import Devolucion
from typing import List

class Sede:
    def __init__(self):
        self._clientes: List[Cliente] = []
        self._asesores: List[Asesor] = []
        self._cajeros: List[Cajero] = []
        self._compras: List[Compra] = []
        self._devoluciones: List[Devolucion] = []
        self._cedulasClientes = set() #PARA HACER LAS BÚSQUEDAS EN O(1)
        self.calificaciones: List[Calificacion] = []

    def setCedulas(self):
        return self._cedulasClientes

    def registrarCliente(self, cliente: Cliente):
        self._clientes.append(cliente)
        self._cedulasClientes.add(cliente.get_cedula())

    def verificar_cedula_existente(self, cedula: int):
        return cedula in self.setCedulas()
    
    def registrar_compra(self, compra: Compra):
        self._compras.append(compra)

    def registrar_devolucion(self, devolucion: Devolucion):
        self._devoluciones.append(devolucion)

    def obtener_compras_cliente(self, cedula_cliente: int) -> List[Compra]:
        return [c for c in self._compras if c.get_cliente().get_cedula() == cedula_cliente]

    def get_compras(self) -> List[Compra]:
            return self._compras   
    
    def registrar_calificacion(self, calificacion: Calificacion):
    # Buscar si ya existe una calificación para el mismo cliente y producto
        for c in self.calificaciones:
            if (c.get_cliente() == calificacion.get_cliente() and
                c.get_producto() == calificacion.get_producto()):
                # Si existe, actualizar los valores
                c.set_valor(calificacion.get_valor())
                c.set_comentario(calificacion.get_comentario())
                c.set_fecha(calificacion.get_fecha())
                return
        # Si no existe, agregar la nueva calificación
        self.calificaciones.append(calificacion)

    def buscar_cliente_por_cedula(self, cedula: int):
        for cliente in self._clientes:
            if cliente.get_cedula() == cedula:
                return cliente
        return None