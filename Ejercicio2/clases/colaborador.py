from datetime import datetime

class Colaborador:
    def __init__(self, id_colaborador, nombre, horas_semana_max, preferencia, no_disponible):
        self._id_colaborador = id_colaborador
        self._nombre = nombre
        self._horas_semana_max = horas_semana_max
        self._preferencia = preferencia
        self._no_disponible = no_disponible
        self._historial_eventos = []
        self._horas_asignadas_semana = 0

    def horas_asignadas_semana(self):
        return self._horas_asignadas_semana