from config.database import db


class Estudiante(db.Model):

    __tablename__ = "estudiantes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    carnet = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    nombres = db.Column(
        db.String(100),
        nullable=False
    )

    apellidos = db.Column(
        db.String(100),
        nullable=False
    )

    correo = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    inscripciones = db.relationship(
        "Inscripcion",
        backref="estudiante",
        lazy=True
    )

    def __repr__(self):
        return f"<Estudiante {self.nombres}>"