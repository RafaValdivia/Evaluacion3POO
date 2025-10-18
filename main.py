"""Ejercicio 1"""

from datetime import datetime, timedelta
from Ejercicio1.Clases.agenda import Agenda
from Ejercicio1.Clases.cita import Cita
from Ejercicio1.Clases.servicio import Coloracion, CorteCabello


agenda = Agenda()
cita1 = Cita(1, "Ana", "Carlos", datetime.now() + timedelta(hours=1))
cita1.asignar_servicio(CorteCabello())
agenda.agregar(cita1)
cita1.confirmar("Cliente confirmó", agenda)

cita2 = Cita(2, "Luis", "Carlos", datetime.now() + timedelta(hours=1, minutes=15))
cita2.asignar_servicio(Coloracion())

try:
    agenda.agregar(cita2)
    cita2.confirmar("Intento de confirmar", agenda)
except Exception as e:
    print("Error:", e)


"""Ejercicio 2"""
from datetime import datetime, timedelta
# Importamos todas las clases de los archivos separados
from cancha import Cancha
from reserva import Reserva
from tarifa import TarifaFinDeSemana, TarifaDiurna, TarifaNocturna
from politica_cancelacion import CancelacionFlexible, CancelacionEstricta
from reglas_y_datos import RESERVAS_ACTIVAS

# --- 1. CONFIGURACIÓN DE TIEMPOS DE PRUEBA ---
AHORA = datetime.now()
FIN_DE_SEMANA_FUTURO = AHORA + timedelta(days=5, hours=10) # Para reservas validas
HOY_MAS_1_HORA = AHORA + timedelta(hours=1) # Para cancelación tardía
DURACION = timedelta(hours=2)

# --- 2. INSTANCIACIÓN DE MODELOS BASE Y POLIMÓRFICOS ---
print("--- 1. INSTANCIACIÓN DE MODELOS ---")

# Instanciación de Cancha
cancha_principal = Cancha(id_cancha=1, nombre="Sintética Principal")
cancha_principal.bloquear_mantencion(AHORA + timedelta(days=2, hours=10), AHORA + timedelta(days=2, hours=12))
print(f"✔️ Cancha: {cancha_principal.nombre} instanciada y con bloqueo de Mantención.")

# Instanciación de Tarifa (Polimórfica)
tarifa_fds = TarifaFinDeSemana()
tarifa_diurna = TarifaDiurna()
print(f"✔️ Tarifa Fin de Semana instanciada (Valor Hora: {tarifa_fds.VALOR_HORA}).")

# Instanciación de Política de Cancelación (Polimórfica)
politica_flexible = CancelacionFlexible()
politica_estricta = CancelacionEstricta()
print(f"✔️ Políticas de Cancelación (Flexible/Estricta) instanciadas.")


# --- 3. ESCENARIO 1: COTIZAR Y CONFIRMAR RESERVA VÁLIDA ---
print("\n--- 2. ESCENARIO 1: RESERVA VÁLIDA (COTIZAR -> CONFIRMAR) ---")
reserva_a = Reserva(
    id_reserva=100, 
    cancha=cancha_principal, 
    cliente="Juan Pérez", 
    inicio=FIN_DE_SEMANA_FUTURO, 
    fin=FIN_DE_SEMANA_FUTURO + DURACION
)
print(f"   Reserva A creada ({reserva_a.estado}).")
reserva_a.cotizar(tarifa_fds)
print(f"   Reserva A cotizada ({reserva_a.estado}). Importe: {reserva_a.importe}")
reserva_a.confirmar("Pago electrónico exitoso.")
print(f"   Reserva A CONFIRMADA ({reserva_a.estado}). Activas: {len(RESERVAS_ACTIVAS)}")


# --- 4. ESCENARIO 2: INTENTO DE SOLAPE (DEBE FALLAR) ---
print("\n--- 3. ESCENARIO 2: INTENTO DE SOLAPE (REGLA SIN SOLAPES) ---")
reserva_b_solape = Reserva(
    id_reserva=101, 
    cancha=cancha_principal, 
    cliente="María López", 
    inicio=FIN_DE_SEMANA_FUTURO + timedelta(hours=1), # Se solapa con Reserva A
    fin=FIN_DE_SEMANA_FUTURO + timedelta(hours=3)
)
reserva_b_solape.cotizar(tarifa_fds)
try:
    reserva_b_solape.confirmar("Intento de confirmación con solape")
except ValueError as e:
    print(f"   ❌ ÉXITO: Solape rechazado. Mensaje: {e}")
finally:
    # Como falló, quitamos la reserva del historial de activos si se agregó por error.
    if reserva_b_solape in RESERVAS_ACTIVAS:
        RESERVAS_ACTIVAS.remove(reserva_b_solape)


# --- 5. ESCENARIO 3: CANCELACIÓN CON PENALIZACIÓN (Trazabilidad) ---
print("\n--- 4. ESCENARIO 3: CANCELACIÓN TARDÍA (POLÍTICA FLEXIBLE) ---")
reserva_c_tardia = Reserva(
    id_reserva=102, 
    cancha=cancha_principal, 
    cliente="Carlos Ruiz", 
    inicio=HOY_MAS_1_HORA, # La hora de inicio es pronto (tardía)
    fin=HOY_MAS_1_HORA + DURACION
)
reserva_c_tardia.cotizar(tarifa_diurna)
reserva_c_tardia.confirmar("Confirmada para hoy.")

# Cancelamos con pocas horas de anticipación (< 24h)
reserva_c_tardia.cancelar("Motivo personal urgente", politica_flexible)

penalidad = reserva_c_tardia.historial_eventos[-1]['monto']
print(f"   Reserva C CANCELADA. Penalización aplicada (20%): {penalidad}")
print(f"   Trazabilidad: {reserva_c_tardia.historial_eventos[-1]['detalle']}")


# --- 6. ESCENARIO 4: INTENTO DE RESERVA EN MANTENCIÓN (DEBE FALLAR) ---
print("\n--- 5. ESCENARIO 4: RESERVA EN MANTENCIÓN (DEBE FALLAR) ---")
reserva_d_mantencion = Reserva(
    id_reserva=103, 
    cancha=cancha_principal, 
    cliente="Andrea Soto", 
    inicio=AHORA + timedelta(days=2, hours=11), # Intervalo de 11:00 a 13:00
    fin=AHORA + timedelta(days=2, hours=13)
)
reserva_d_mantencion.cotizar(tarifa_diurna)
try:
    reserva_d_mantencion.confirmar("Intento en horario de mantención")
except ValueError as e:
    print(f"   ❌ ÉXITO: Mantención rechazada. Mensaje: {e}")
