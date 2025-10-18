class Servicios:
    def __init__(self):
        self._services = {
            "CorteCabello": 30,
            "Coloracion": 90
        }

    def get_services(self):
        return list(self._services.keys())

    def get_duracion(self, servicio_type):
        return self._services.get(servicio_type, 0)