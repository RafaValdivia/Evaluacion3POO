from datetime import datetime, timedelta

class Cita:
    def __init__(self, id_cita, cliente, profesional, inicio):
        self._id_cita = id_cita
        self._cliente = cliente
        self._profesional = profesional
        self._inicio = inicio
        self._duracion_min = 0
        self._estado = "creada"
        self._historial_eventos = []
        self._servicio_type = None

    def fin(self):
        return self._inicio + timedelta(minutes=self._duracion_min)

    def asignar_servicio(self, servicios, servicio_type):
        if self._estado == "creada" and self._duracion_min == 0 and servicio_type in servicios.get_services():
            self._duracion_min = servicios.get_duracion(servicio_type)
            self._servicio_type = servicio_type
            self._historial_eventos.append({"timestamp": datetime.now(), "tipo": "servicio_asignado", "detalle": f"Servicio asignado: {self._duracion_min} minutos ({servicio_type})"})
            return True
        return False

    def confirmar(self, motivo, agenda):
        if self._estado == "creada" and self._duracion_min > 0 and not agenda.existe_solape(self._profesional, self._inicio, self.fin()):
            self._estado = "confirmada"
            self._historial_eventos.append({"timestamp": datetime.now(), "tipo": "confirmada", "detalle": motivo})
            return True
        return False

    def cancelar(self, motivo):
        if self._estado in ["creada", "confirmada"]:
            self._estado = "cancelada"
            self._historial_eventos.append({"timestamp": datetime.now(), "tipo": "cancelada", "detalle": motivo})
            return True
        return False

    def get_servicio_type(self):
        return self._servicio_type
