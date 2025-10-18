from abc import ABC, abstractmethod
from datetime import datetime, time

class Tarifa(ABC):
    
    @abstractmethod
    def calcular_importe(self, inicio: datetime, fin: datetime) -> dict:
        pass

class TarifaFinDeSemana(Tarifa):
    VALOR_HORA = 35.0

    def calcular_importe(self, inicio: datetime, fin: datetime) -> dict:
        if inicio >= fin:
             raise ValueError("Intervalo inválido.")
             
        duracion_horas = (fin - inicio).total_seconds() / 3600
        total = duracion_horas * self.VALOR_HORA
        return {
            "total": round(total, 2), 
            "desglose": [{"tipo": "FinDeSemana", "subtotal": round(total, 2)}] 
        }

class TarifaDiurna(Tarifa):
    VALOR_HORA = 20.0
    HORA_INICIO = time(8, 0)
    HORA_FIN = time(19, 59)

    def calcular_importe(self, inicio: datetime, fin: datetime) -> dict:
        if inicio >= fin:
             raise ValueError("Intervalo inválido.")
             
        duracion_horas = (fin - inicio).total_seconds() / 3600
        total = duracion_horas * self.VALOR_HORA
        return {
            "total": round(total, 2), 
            "desglose": [{"tipo": "Diurna", "subtotal": round(total, 2)}]
        }

class TarifaNocturna(Tarifa):
    VALOR_HORA = 15.0 
    
    def calcular_importe(self, inicio: datetime, fin: datetime) -> dict:
        if inicio >= fin:
             raise ValueError("Intervalo inválido.")
             
        duracion_horas = (fin - inicio).total_seconds() / 3600
        total = duracion_horas * self.VALOR_HORA
        return {
            "total": round(total, 2), 
            "desglose": [{"tipo": "Nocturna", "subtotal": round(total, 2)}]
        }
