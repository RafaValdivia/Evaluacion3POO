from datetime import datetime, timedelta
from abc import ABC, abstractmethod

# ---- Servicio ----
class Servicio(ABC):
    @abstractmethod
    def duracion_min(self):
        pass

class CorteCabello(Servicio):
    def duracion_min(self):
        return 30

class Coloracion(Servicio):
    def duracion_min(self):
        return 90
a
