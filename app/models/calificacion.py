from config.database import db


class Calificacion(db.Model):

    __tablename__ = "calificaciones"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nota = db.Column(
        db.Float,
        nullable=False
    )

    inscripcion_id = db.Column(
        db.Integer,
        db.ForeignKey("inscripciones.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Calificacion {self.nota}>"