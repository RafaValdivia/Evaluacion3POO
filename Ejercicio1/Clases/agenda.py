# ---- Agenda ----
class Agenda:
    def __init__(self):
        self._citas = []

    def agregar(self, cita):
        if any(c._id == cita._id for c in self._citas):
            raise Exception("ID de cita duplicado.")
        if self.existe_solape(cita._profesional, cita._inicio, cita.fin):
            raise Exception("Cita solapada.")
        self._citas.append(cita)

    def existe_solape(self, profesional, inicio, fin):
        for c in self._citas:
            if c._profesional == profesional and c._estado != "cancelada":
                if inicio < c.fin and c._inicio < fin:
                    return True
        return False
