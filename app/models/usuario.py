from config.database import db
from flask_login import UserMixin


class Usuario(UserMixin, db.Model):

    __tablename__ = "usuarios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    correo = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    activo = db.Column(
        db.Boolean,
        default=True
    )

    rol_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Usuario {self.nombre}>"