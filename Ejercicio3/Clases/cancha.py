from datetime import datetime

class Cancha:
    def __init__(self, id_cancha, nombre):
        self._id_cancha = id_cancha
        self._nombre = nombre
        self._calendario_mantencion = []
        self._historial_eventos = []

    def bloquear_mantencion(self, inicio, fin):
        self._calendario_mantencion.append({"inicio": inicio, "fin": fin})
        self._historial_eventos.append({"timestamp": datetime.now(), "tipo": "bloqueo_mantencion", "detalle": f"Bloqueo de {inicio} a {fin}"})