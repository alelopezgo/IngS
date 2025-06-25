import modeloCalzado
class Calzado:
    def __init__(self, modelo: ModeloCalzado, talla: int, color: str, precio: int):
        self._modelo = modelo
        self._talla = talla
        self._color = color
        self._precio = precio

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo: ModeloCalzado):
        self._modelo = modelo

    def get_talla(self):
        return self._talla

    def set_talla(self, talla: int):
        self._talla = talla

    def get_color(self):
        return self._color

    def set_color(self, color: str):
        self._color = color

    def get_precio(self):
        return self._precio

    def set_precio(self, precio: int):
        self._precio = precio

 
