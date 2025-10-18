from datetime import datetime

class Reserva:
    def __init__(self, id_reserva, cancha, cliente, inicio, fin):
        self._id_reserva = id_reserva
        self._cancha = cancha
        self._cliente = cliente
        self._inicio = inicio
        self._fin = fin
        self._estado = "creada"
        self._importe = 0
        self._desglose_tarifa = []
        self._historial_eventos = []

    def cotizar(self, tarifa):
        if self._estado == "creada":
            self._importe, self._desglose_tarifa = tarifa.calcular_importe(self._inicio, self._fin)
            self._historial_eventos.append({"timestamp": datetime.now(), "tipo": "cotizada", "detalle": f"Importe: {self._importe}"})
            return True
        return False