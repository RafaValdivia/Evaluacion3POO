class Franja:
    def __init__(self, dia, hora_inicio, hora_fin):
        self._dia = dia
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin

    def duracion_horas(self):
        return (self._hora_fin - self._hora_inicio).total_seconds() / 3600