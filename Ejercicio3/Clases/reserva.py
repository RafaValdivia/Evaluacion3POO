from datetime import datetime
from cancha import Cancha
from tarifa import Tarifa
from politicacancelacion import PoliticaCancelacion
from datos import RESERVAS_ACTIVAS, existe_interseccion

class Reserva:
    def __init__(self, id_reserva, cancha: Cancha, cliente, inicio, fin):
        if inicio >= fin: raise ValueError("Intervalo inválido.") 
        
        self.id_reserva = id_reserva
        self.cancha = cancha
        self.cliente = cliente
        self.inicio = inicio
        self.fin = fin
        
        self.estado = "creada"
        self.importe = 0.0
        self.desglose_tarifa = []
        self.historial_eventos = []

    def registrar_evento(self, tipo, detalle, monto=None):
        self.historial_eventos.append({
            "ts": datetime.now(), 
            "tipo": tipo, 
            "detalle": detalle, 
            "monto": monto
        })

    def cotizar(self, tarifa: Tarifa):
        if self.estado != "creada": return
            
        resultado = tarifa.calcular_importe(self.inicio, self.fin)
        
        self.importe = resultado["total"]
        self.desglose_tarifa = resultado["desglose"]
        self.estado = "cotizada" 
        self.registrar_evento("COTIZADA", f"Importe: {self.importe}", self.importe)

    def confirmar(self, motivo):
        if self.estado not in ["creada", "cotizada"]: return
            
        if self.cancha.intersecta_mantencion(self.inicio, self.fin):
            raise ValueError("Rechazo: Mantención en la cancha.")

        if self._hay_solape_con_otra_reserva():
            raise ValueError("Rechazo: Solape con otra reserva activa.")

        self.estado = "confirmada"
        RESERVAS_ACTIVAS.append(self) 
        self.registrar_evento("CONFIRMADA", f"Confirmación: {motivo}")

    def cancelar(self, motivo, politica: PoliticaCancelacion):
        if self.estado not in ["creada", "confirmada"]: return
            
        horas_previas = (self.inicio - datetime.now()).total_seconds() / 3600
        penalizacion_info = politica.penalizacion(horas_previas, self.importe)
        monto = penalizacion_info["monto_penalizacion"]
        
        self.estado = "cancelada"
        if self in RESERVAS_ACTIVAS:
            RESERVAS_ACTIVAS.remove(self)
            
        self.registrar_evento("CANCELADA", f"Penalidad: {monto}", monto)

    def _hay_solape_con_otra_reserva(self):
        for otra_reserva in RESERVAS_ACTIVAS:
            if otra_reserva.cancha.id_cancha == self.cancha.id_cancha and otra_reserva.id_reserva != self.id_reserva:
                
                A_inicio, A_fin = otra_reserva.inicio, otra_reserva.fin
                B_inicio, B_fin = self.inicio, self.fin
                
                if existe_interseccion(A_inicio, A_fin, B_inicio, B_fin):
                    return True
        return False
        
    def marcar_no_show(self, motivo):
        if self.estado == "confirmada":
            self.estado = "no_show"
            self.registrar_evento("NO_SHOW", f"Cliente no asistió. Motivo: {motivo}")
            if self in RESERVAS_ACTIVAS:
                RESERVAS_ACTIVAS.remove(self)
        else:
            return
