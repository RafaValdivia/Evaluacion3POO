from abc import ABC, abstractmethod

class PoliticaCancelacion(ABC):
    @abstractmethod
    def penalizacion(self, horas_previas: float, importe: float) -> dict:
        pass
        
class CancelacionFlexible(PoliticaCancelacion):
    def penalizacion(self, horas_previas: float, importe: float) -> dict:
        monto = 0.0
        motivo = "Sin penalización por tiempo."
        if horas_previas < 24:
            monto = importe * 0.20
            motivo = "Penalidad 20% por cancelación tardía."
            
        return {"monto_penalizacion": round(monto, 2), "motivo": motivo}

class CancelacionEstricta(PoliticaCancelacion):
    def penalizacion(self, horas_previas: float, importe: float) -> dict:
        monto = importe * 0.50
        motivo = "Penalidad 50% por política Estricta."
        return {"monto_penalizacion": round(monto, 2), "motivo": motivo}
