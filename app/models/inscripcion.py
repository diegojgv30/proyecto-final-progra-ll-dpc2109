from app import db


class Inscripcion(db.Model):

    __tablename__ = "inscripciones"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    estudiante_id = db.Column(
        db.Integer,
        db.ForeignKey("estudiantes.id"),
        nullable=False
    )

    asignatura_id = db.Column(
        db.Integer,
        db.ForeignKey("asignaturas.id"),
        nullable=False
    )

    calificaciones = db.relationship(
        "Calificacion",
        backref="inscripcion",
        lazy=True
    )

    def __repr__(self):
        return f"<Inscripcion {self.id}>"