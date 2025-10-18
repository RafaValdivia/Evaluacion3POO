"""ejercicio 1"""
from Ejercicio1.Clases.cita import Cita
from Ejercicio1.Clases.agenda import Agenda
from Ejercicio1.Clases.servicios import Servicios
from datetime import datetime, timedelta

def get_datetime_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            return datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Formato incorrecto. Use YYYY-MM-DD HH:MM (ejemplo: 2025-10-18 10:00). Intente de nuevo.")

def main():
    agenda = Agenda()
    servicios = Servicios()

    while True:
        print("\nOpciones:")
        print("1. Agregar cita")
        print("2. Salir")
        choice = input("Seleccione una opción (1-2): ")

        if choice == "2":
            break

        if choice == "1":
            id_cita = input("Ingrese ID de la cita: ")
            cliente = input("Ingrese nombre del cliente: ")
            profesional = input("Ingrese nombre del profesional: ")
            inicio = get_datetime_input("Ingrese fecha y hora de inicio (YYYY-MM-DD HH:MM) a partir del 2025-10-18 para adelante: ")

            cita = Cita(id_cita, cliente, profesional, inicio)
            servicio_type = input(f"Seleccione servicio ({', '.join(servicios.get_services())}): ")
            if cita.asignar_servicio(servicios, servicio_type):
                motivo = input("Ingrese motivo de confirmación: ")
                if agenda.agregar(cita) and cita.confirmar(motivo, agenda):
                    print(f"Cita {id_cita} agregada y confirmada. Fin: {cita.fin()}, Servicio: {cita.get_servicio_type()}")
                else:
                    print("No se pudo agregar la cita (posible solape).")
            else:
                print("No se pudo asignar el servicio.")

if __name__ == "__main__":
    main()
    
"""ejercicio 2"""
from Ejercicio2.clases.colaborador import Colaborador
from Ejercicio2.clases.franja import Franja
from Ejercicio2.clases.turno_asignado import TurnoAsignado
from Ejercicio2.clases.plan_semanal import PlanSemanal
from Ejercicio2.clases.politica_turno import TurnoFijo
from datetime import datetime, timedelta

def main():
    id_colaborador = input("Ingrese el ID del colaborador: ")
    nombre = input("Ingrese el nombre del colaborador: ")
    horas_max = int(input("Ingrese las horas máximas por semana: "))
    preferencia = input("Ingrese la preferencia (manana/tarde): ")
    no_disponible = []  # Simplified for input, can be expanded
    colaborador = Colaborador(id_colaborador, nombre, horas_max, preferencia, no_disponible)

    dia = input("Ingrese el día (ej. lunes): ")
    hora_inicio = input("Ingrese la hora de inicio (formato HH:MM, ej. 09:00): ")
    hora_fin = input("Ingrese la hora de fin (formato HH:MM, ej. 10:00): ")
    inicio = datetime.strptime(f"{datetime.now().strftime('%Y-%m-%d')} {hora_inicio}", "%Y-%m-%d %H:%M")
    fin = datetime.strptime(f"{datetime.now().strftime('%Y-%m-%d')} {hora_fin}", "%Y-%m-%d %H:%M")
    franja = Franja(dia, inicio, fin)

    turno = TurnoAsignado(franja, colaborador)
    plan = PlanSemanal(f"{datetime.now().strftime('%Y-%m-%d')} to {datetime.now().strftime('%Y-%m-%d')}")
    plan._franjas.append(franja)
    plan._turnos_asignados.append(turno)
    politica = TurnoFijo()
    print(f"Cobertura: {plan.cobertura_pct()}%")

if __name__ == "__main__":
    main()
    
"""Ejercicio 3"""
from Ejercicio3.Clases.cancha import Cancha
from Ejercicio3.Clases.calendarioCancha import CalendarioCancha
from Ejercicio3.Clases.reserva import Reserva
from Ejercicio3.Clases.tarifa import TarifaDiurna, TarifaNocturna, TarifaFinDeSemana
from Ejercicio3.Clases.politicacancelacion import CancelacionFlexible, CancelacionEstricta
from datetime import datetime, timedelta

def main():
    id_cancha = input("Ingrese el ID de la cancha: ")
    nombre = input("Ingrese el nombre de la cancha: ")
    cancha = Cancha(id_cancha, nombre)
    calendario = CalendarioCancha()

    id_reserva = input("Ingrese el ID de la reserva: ")
    cliente = input("Ingrese el nombre del cliente: ")
    hora_inicio = input("Ingrese la hora de inicio (formato HH:MM, ej. 14:00): ")
    hora_fin = input("Ingrese la hora de fin (formato HH:MM, ej. 15:00): ")
    inicio = datetime.strptime(f"{datetime.now().strftime('%Y-%m-%d')} {hora_inicio}", "%Y-%m-%d %H:%M")
    fin = datetime.strptime(f"{datetime.now().strftime('%Y-%m-%d')} {hora_fin}", "%Y-%m-%d %H:%M")
    reserva = Reserva(id_reserva, cancha, cliente, inicio, fin)

    tarifa_type = input("Ingrese el tipo de tarifa (diurna/nocturna/finde): ").lower()
    tarifa = TarifaDiurna() if tarifa_type == "diurna" else TarifaNocturna() if tarifa_type == "nocturna" else TarifaFinDeSemana()
    if reserva.cotizar(tarifa):
        print(f"Importe cotizado: {reserva._importe}")
    else:
        print("No se pudo cotizar la reserva.")

if __name__ == "__main__":
    main()

"""Ejercicio 4"""
from Ejercicio4.clases.suscriptor import Suscriptor
from Ejercicio4.clases.retiro import Retiro
from Ejercicio4.clases.material import Plastico, Vidrio, PapelCarton
from Ejercicio4.clases.bonussemanal import BonusSemanal
from Ejercicio4.clases.aviso import Aviso
from datetime import datetime

def main():
    id_suscriptor = input("Ingrese el ID del suscriptor: ")
    direccion = input("Ingrese la dirección del suscriptor: ")
    suscriptor = Suscriptor(id_suscriptor, direccion)

    id_retiro = input("Ingrese el ID del retiro: ")
    material_type = input("Ingrese el tipo de material (plastico/vidrio/papel): ").lower()
    material = Plastico() if material_type == "plastico" else Vidrio() if material_type == "vidrio" else PapelCarton()
    kg = float(input("Ingrese los kilogramos: "))
    fecha = datetime.now()
    retiro = Retiro(id_retiro, suscriptor, fecha, material, kg)
    
    retiro.validar()  # Simular validación del retiro
    print(f"Puntos calculados: {retiro.puntos_calculados()}")

    bonus = BonusSemanal(suscriptor)
    puntos_bonus = bonus.calcular_bonus()
    if puntos_bonus > 0:
        print(f"Bonus semanal aplicado: {puntos_bonus} puntos")

    aviso = Aviso(retiro, f"Retiro {id_retiro} validado con {kg} kg de {material_type}")
    print(f"Aviso emitido: {aviso.get_mensaje()}")
    print(f"Estado después de leer: {aviso.marcar_leido()}")

if __name__ == "__main__":
    main()