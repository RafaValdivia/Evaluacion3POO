from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Tarifa(ABC):
    @abstractmethod
    def calcular_importe(self, inicio, fin):
        pass

class TarifaDiurna(Tarifa):
    def calcular_importe(self, inicio, fin):
        return 10, [{"desde": inicio, "hasta": fin, "tipo_tarifa": "Diurna", "minutos": (fin - inicio).total_seconds() / 60, "valor_hora": 10, "subtotal": 10}]

class TarifaNocturna(Tarifa):
    def calcular_importe(self, inicio, fin):
        return 15, [{"desde": inicio, "hasta": fin, "tipo_tarifa": "Nocturna", "minutos": (fin - inicio).total_seconds() / 60, "valor_hora": 15, "subtotal": 15}]

class TarifaFinDeSemana(Tarifa):
    def calcular_importe(self, inicio, fin):
        return 20, [{"desde": inicio, "hasta": fin, "tipo_tarifa": "FinDeSemana", "minutos": (fin - inicio).total_seconds() / 60, "valor_hora": 20, "subtotal": 20}]