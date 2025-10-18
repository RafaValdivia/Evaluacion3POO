from datetime import datetime

class TurnoAsignado:
    def __init__(self, franja, responsable):
        self._franja = franja
        self._responsable = responsable
        self._marcado_forzado = False
        self._historial_eventos = []

    def duracion_horas(self):
        return self._franja.duracion_horas()