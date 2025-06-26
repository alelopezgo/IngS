from datetime import datetime

class CalificacionServicio:
    registros = []

    def __init__(self, cliente, valor: int, comentario: str = ""):
        if not 1 <= valor <= 5:
            raise ValueError("El puntaje debe estar entre 1 y 5")
        self._cliente = cliente
        self._valor = valor
        self._comentario = comentario
        self._fecha = datetime.now()
        CalificacionServicio.registros.append(self)

    def __str__(self):
        nom = self._cliente.get_nombre()
        return f"[{self._fecha:%d-%m-%Y}] {nom}: {self._valor}/5 «{self._comentario}»"
