from datetime import datetime

class PlanSemanal:
    def __init__(self, semana):
        self._semana = semana
        self._franjas = []
        self._turnos_asignados = []
        self._historial_eventos = []

    def cobertura_pct(self):
        return (len(self._turnos_asignados) / len(self._franjas) * 100) if self._franjas else 0

    def valido(self):
        return len(self._turnos_asignados) == len(self._franjas)