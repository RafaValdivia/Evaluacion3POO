from datetime import datetime
from datos import CANCHAS_REGISTRADAS, existe_interseccion

class Cancha:
    def __init__(self, id_cancha, nombre):
        self.id_cancha = id_cancha
        self.nombre = nombre
        self.mantencion_bloques = []
        self.historial = [] 

        if id_cancha in [c.id_cancha for c in CANCHAS_REGISTRADAS]:
             raise ValueError("Cancha ID ya existe.")
        CANCHAS_REGISTRADAS.append(self)

    def registrar_evento(self, tipo, detalle, monto=None):
        self.historial.append({
            "ts": datetime.now(), 
            "tipo": tipo, 
            "detalle": detalle, 
            "monto": monto
        })
    
    def bloquear_mantencion(self, inicio, fin):
        if inicio >= fin: raise ValueError("Inicio no puede ser despues del fin.")
        self.mantencion_bloques.append({"inicio": inicio, "fin": fin})
        self.registrar_evento("MANTENCION", f"Bloqueada de {inicio} a {fin}")

    def intersecta_mantencion(self, inicio, fin):
        for bloque in self.mantencion_bloques:
            if existe_interseccion(bloque['inicio'], bloque['fin'], inicio, fin):
                return True
        return False
