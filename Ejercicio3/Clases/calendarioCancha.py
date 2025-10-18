class CalendarioCancha:
    def __init__(self):
        self._mantencion = []

    def agregar(self, inicio, fin):
        if inicio < fin and not any(inicio < m["fin"] and fin > m["inicio"] for m in self._mantencion):
            self._mantencion.append({"inicio": inicio, "fin": fin})
            return True
        return False

    def intersecta(self, inicio, fin):
        return any(inicio < m["fin"] and fin > m["inicio"] for m in self._mantencion)