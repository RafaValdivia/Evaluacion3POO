from datetime import datetime

class Retiro:
    def __init__(self, id_retiro, suscriptor, fecha, material, kg):
        self._id_retiro = id_retiro
        self._suscriptor = suscriptor
        self._fecha = fecha
        self._material = material
        self._kg = kg
        self._estado = "registrado"
        self._historial_eventos = []

    def puntos_calculados(self):
        return self._material.puntos(self._kg) if self._estado == "validado" else 0

    def validar(self):
        if self._estado == "registrado":
            self._estado = "validado"
            self._historial_eventos.append({"timestamp": datetime.now(), "tipo": "validado", "detalle": f"Validado {self._kg} kg de {self._material.__class__.__name__}"})
            return True
        return False