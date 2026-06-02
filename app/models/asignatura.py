from config.database import db


class Asignatura(db.Model):

    __tablename__ = "asignaturas"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    codigo = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    inscripciones = db.relationship(
        "Inscripcion",
        backref="asignatura",
        lazy=True
    )

    def __repr__(self):
        return f"<Asignatura {self.nombre}>"