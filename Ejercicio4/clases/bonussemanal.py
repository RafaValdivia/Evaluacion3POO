from datetime import datetime

class BonusSemanal:
    def __init__(self, suscriptor):
        self._suscriptor = suscriptor
        self._bonus_aplicado = False
        self._puntos_bonus = 0

    def calcular_bonus(self):
        retiros = self._suscriptor.retiros_validados_semana()
        if not self._bonus_aplicado and retiros >= 3:
            self._puntos_bonus = retiros * 10  # 10 puntos extra por cada retiro validado más allá de 2
            self._bonus_aplicado = True
            self._suscriptor._historial_eventos.append({"timestamp": datetime.now(), "tipo": "bonus_aplicado", "detalle": f"Bonus de {self._puntos_bonus} puntos"})
            return self._puntos_bonus
        return 0

    def get_puntos_bonus(self):
        return self._puntos_bonus