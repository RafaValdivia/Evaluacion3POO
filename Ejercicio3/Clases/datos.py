from datetime import datetime

RESERVAS_ACTIVAS = [] 
CANCHAS_REGISTRADAS = []

def existe_interseccion(A_inicio: datetime, A_fin: datetime, B_inicio: datetime, B_fin: datetime) -> bool:
    return A_inicio < B_fin and B_inicio < A_fin
