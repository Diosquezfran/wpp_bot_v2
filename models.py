from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = 'users'  # Asegúrate de que coincida con tu tabla existente
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), unique=True, nullable=False)


class Mensaje(db.Model):
    __tablename__ = 'messages'  # Nombre exacto de la tabla
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    contenido = db.Column(db.Text, nullable=False)


class Servicio(db.Model):
    __tablename__ = 'services'  # Asegúrate de que coincida con tu tabla existente
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)  # Nombre del servicio
    descripcion = db.Column(db.String(255), nullable=True)  # Descripción opcional del servicio
    precio = db.Column(db.Float, nullable=False)  # Precio del servicio

    turnos = db.relationship('Turno', backref='servicio', lazy=True)  # Relación con Turno

    def __repr__(self):
        return f"<Servicio {self.nombre}>"


class Negocio(db.Model):
    __tablename__ = 'businesses'  # Asegúrate de que coincida con tu tabla existente
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)  # Nombre del negocio
    direccion = db.Column(db.String(255), nullable=False)  # Dirección del negocio
    telefono = db.Column(db.String(20), nullable=False)  # Teléfono del negocio
    hora_apertura = db.Column(db.Time, nullable=False)  # ⬅️ Nuevo campo
    hora_cierre = db.Column(db.Time, nullable=False)  # ⬅️ Nuevo campo
    servicios = db.relationship('Servicio', backref='negocio', lazy=True)  # Relación con Servicio

    def __repr__(self):
        return f"<Negocio {self.nombre}>"


class Turno(db.Model):
    __tablename__ = 'turns'  # Asegúrate de que coincida con tu tabla existente
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)  # Fecha y hora del turno
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Relación con el usuario
    servicio_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)  # Relación con el servicio

    usuario = db.relationship('Usuario', backref='turnos', lazy=True)  # Relación con Usuario
    servicio = db.relationship('Servicio', backref='turnos', lazy=True)  # Relación con Servicio

    def __repr__(self):
        return f"<Turno {self.fecha} - {self.servicio.nombre}>"
