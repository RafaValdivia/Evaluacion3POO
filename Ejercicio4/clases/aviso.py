from datetime import datetime

class Aviso:
    def __init__(self, retiro, mensaje):
        self._retiro = retiro
        self._mensaje = mensaje
        self._fecha_emision = datetime.now()
        self._leido = False

    def marcar_leido(self):
        self._leido = True
        return f"Aviso leido: {self._mensaje}"

    def get_mensaje(self):
        return self._mensaje