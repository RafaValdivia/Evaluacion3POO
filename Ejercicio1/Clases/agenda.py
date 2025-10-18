from datetime import datetime, timedelta

class Agenda:
    def __init__(self):
        self._citas = []

    def agregar(self, cita):
        if not any(c._id_cita == cita._id_cita for c in self._citas) and not self.existe_solape(cita._profesional, cita._inicio, cita.fin()):
            self._citas.append(cita)
            return True
        return False

    def existe_solape(self, profesional, inicio, fin):
        for cita in self._citas:
            if cita._profesional == profesional and cita._estado != "cancelada" and cita._inicio < fin and inicio < cita.fin():
                return True
        return False