from abc import ABC, abstractmethod

class PoliticaCancelacion(ABC):
    @abstractmethod
    def penalizacion(self, horas_previas, importe):
        pass

class CancelacionFlexible(PoliticaCancelacion):
    def penalizacion(self, horas_previas, importe):
        return 0 if horas_previas >= 24 else 0.20 * importe, "Penalización Flexible"

class CancelacionEstricta(PoliticaCancelacion):
    def penalizacion(self, horas_previas, importe):
        return 0.50 * importe, "Penalización Estricta"