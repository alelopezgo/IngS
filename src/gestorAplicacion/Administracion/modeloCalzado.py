
class ModeloCalzado:
    def __init__(self, codigo: int, nombre: str, marca: str = ""):
        self._codigo = codigo          # Código del modelo
        self._nombre = nombre          
        self._marca = marca           

    def get_codigo(self):
        return self._codigo

    def set_codigo(self, codigo: int):
        self._codigo = codigo

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_marca(self):
        return self._marca

    def set_marca(self, marca: str):
        self._marca = marca
