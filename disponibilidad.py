from models import db, Turno, Negocio
from datetime import datetime, timedelta


def consultar_disponibilidad(negocio_id, fecha):
    negocio = Negocio.query.get(negocio_id)
    if not negocio:
        return {"error": "Negocio no encontrado"}

    # Convertimos la fecha a un objeto datetime para validar
    try:
        fecha_consulta = datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        return {"error": "Formato de fecha inválido. Use AAAA-MM-DD"}

    # Consultamos los turnos ya reservados para el negocio en esa fecha
    turnos_reservados = Turno.query.filter_by(negocio_id=negocio_id, fecha=fecha_consulta).all()
    
    # Obtenemos horarios de apertura y cierre
    hora_apertura = negocio.hora_apertura
    hora_cierre = negocio.hora_cierre

    # Lista de horarios ocupados
    horarios_ocupados = {turno.hora for turno in turnos_reservados}

    # Generamos la lista de horarios disponibles
    horario_actual = hora_apertura
    disponibilidad = []

    while horario_actual < hora_cierre:
        if horario_actual not in horarios_ocupados:
            disponibilidad.append(horario_actual.strftime("%H:%M"))

        # Avanzamos en intervalos de 30 minutos
        horario_actual = (datetime.combine(datetime.today(), horario_actual) + timedelta(minutes=30)).time()

    return {"disponibilidad": disponibilidad}
