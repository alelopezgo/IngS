from datetime import datetime
from typing import List

class CalificacionServicio:
    registros: List["CalificacionServicio"] = []

    def __init__(self, cliente, valor: int, comentario: str = "") -> None:
        if not 1 <= valor <= 5:
            raise ValueError("El puntaje debe estar entre 1 y 5")
        self._cliente = cliente
        self._valor = valor
        self._comentario = comentario
        self._fecha = datetime.now()
        CalificacionServicio.registros.append(self)

    @classmethod
    def promedio(cls) -> float:
        if not cls.registros:
            return 0.0
        return sum(c._valor for c in cls.registros) / len(cls.registros)

    @classmethod
    def listar_todas(cls) -> List["CalificacionServicio"]:
        return cls.registros

    def __str__(self) -> str:
        return f"[{self._fecha:%d-%m-%Y}] {self._cliente.get_nombre()}: {self._valor}/5 «{self._comentario}»"
