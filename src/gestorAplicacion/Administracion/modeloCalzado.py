class ModeloCalzado:
    _contador_modelos = 1  # contador para códigos automáticos

    def __init__(self, codigo: int = None, nombre: str = "", marca: str = ""):
        # Asignar código automáticamente si no se provee
        if codigo is None:
            self._codigo = ModeloCalzado._contador_modelos
            ModeloCalzado._contador_modelos += 1
        else:
            self._codigo = codigo
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
