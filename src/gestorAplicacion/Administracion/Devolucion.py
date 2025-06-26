from datetime import datetime
from gestorAplicacion.Administracion.compra import Compra
from gestorAplicacion.Administracion.calzado import Calzado
from gestorAplicacion.Administracion.sede import Sede

class Devolucion:
    ESTADOS_NO_ADMITIDOS = ["usado", "dañado", "defectuoso", "deteriorado"]

    def __init__(self, producto: Calzado, motivo: str, compra: Compra, estado_producto: str):
        self._producto = producto
        self._motivo = motivo
        self._compra = compra
        self._estado_producto = estado_producto.strip().lower()
        self._fecha_compra = compra.get_fecha()
        self._dias = (datetime.now() - self._fecha_compra).days
        self._valida = (self._dias <= 30 and self._estado_producto not in Devolucion.ESTADOS_NO_ADMITIDOS)

    def es_valida(self):
        return self._valida
    
    def get_producto(self):
        return self._producto

    def get_motivo(self):
        return self._motivo

    def get_compra(self):
        return self._compra

    def get_estado_producto(self):
        return self._estado_producto
    
    def get_dias(self):
        return self._dias
    
    def resumen(self):
        resultado = "Devolución válida" if self._valida else "Devolución inválida"
        if self._dias > 30:
            resultado += " (más de 30 días)"
        elif self._estado_producto in Devolucion.ESTADOS_NO_ADMITIDOS:
            resultado += f" (producto en estado no admitido: {self._estado_producto})"

        modelo = self._producto.get_modelo()

        return (
            f"----- DEVOLUCIÓN -----\n"
            f"Código de compra: {self._compra.get_codigo()}\n"
            f"Producto: {modelo.get_nombre()} ({modelo.get_marca()}) - "
            f"Talla {self._producto.get_talla()} - Color {self._producto.get_color()}\n"
            f"Motivo: {self._motivo}\n"
            f"Fecha de compra: {self._fecha_compra.strftime('%Y-%m-%d')}\n"
            f"Días transcurridos: {self._dias} días\n"
            f"Estado del producto: {self._estado_producto}\n"
            f"Resultado: {resultado}"
        )
    