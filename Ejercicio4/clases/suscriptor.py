from datetime import datetime

class Suscriptor:
    def __init__(self, id_suscriptor, direccion):
        self._id_suscriptor = id_suscriptor
        self._direccion = direccion
        self._saldo_puntos = 0
        self._estado = "habilitado"
        self._historial_eventos = []

    def retiros_validados_semana(self):
        return sum(1 for e in self._historial_eventos if e["tipo"] == "validado" and e["timestamp"].isocalendar()[1] == datetime.now().isocalendar()[1])