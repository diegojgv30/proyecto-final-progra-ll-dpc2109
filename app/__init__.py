from flask import Flask
from flask_login import LoginManager

from config.database import db

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):

    from app.models.usuario import Usuario

    return Usuario.query.get(int(user_id))


def create_app():

    app = Flask(__name__)

    app.config.from_object("config.settings.Config")

    db.init_app(app)

    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    from app.controllers.auth_controller import auth

    app.register_blueprint(auth)

    from app.models import (
        Rol,
        Usuario,
        Estudiante,
        Asignatura,
        Inscripcion,
        Calificacion
    )

    return app