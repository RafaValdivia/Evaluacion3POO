# ---- Cita ----
from datetime import datetime, timedelta


class Cita:
    def __init__(self, id_cita, cliente, profesional, inicio):
        self._id = id_cita
        self._cliente = cliente
        self._profesional = profesional
        self._inicio = inicio
        self._duracion_min = None
        self._estado = "creada"
        self._historial_eventos = []

    @property
    def fin(self):
        return self._inicio + timedelta(minutes=self._duracion_min) if self._duracion_min else None

    def _registrar_evento(self, tipo, detalle):
        self._historial_eventos.append({
            "timestamp": datetime.now(),
            "tipo": tipo,
            "detalle": detalle
        })

    def asignar_servicio(self, servicio):
        self._duracion_min = servicio.duracion_min()
        self._registrar_evento("servicio_asignado", f"Duración: {self._duracion_min} min")

    def confirmar(self, motivo, agenda):
        if self._estado != "creada" or self._duracion_min is None:
            raise Exception("No se puede confirmar esta cita.")
        if agenda.existe_solape(self._profesional, self._inicio, self.fin):
            raise Exception("Ya existe una cita en ese horario.")
        self._estado = "confirmada"
        self._registrar_evento("confirmada", motivo)

    def cancelar(self, motivo):
        if self._estado not in ["creada", "confirmada"]:
            raise Exception("No se puede cancelar esta cita.")
        self._estado = "cancelada"
        self._registrar_evento("cancelada", motivo)




