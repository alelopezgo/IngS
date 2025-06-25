class Calzado:
    def __init__(self, tipo: str, talla: int, color: str, codigo: int, precio: int):
        self._tipo = tipo
        self._talla = talla
        self._color = color
        self._codigo = codigo
        self._precio = precio

  
    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo: str):
        self._tipo = tipo

    def get_talla(self):
        return self._talla

    def set_talla(self, talla: int):
        self._talla = talla

    def get_color(self):
        return self._color

    def set_color(self, color: str):
        self._color = color

    def get_codigo(self):
        return self._codigo

    def set_codigo(self, codigo: int):
        self._codigo = codigo

    def get_precio(self):
        return self._precio

    def set_precio(self, precio: int):
        self._precio = precio


 
