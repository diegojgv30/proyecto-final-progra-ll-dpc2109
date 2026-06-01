from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from werkzeug.security import check_password_hash

from app.forms.login_form import LoginForm
from app.models.usuario import Usuario
from app.controllers.permisos import rol_requerido

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        usuario = Usuario.query.filter_by(
            correo=form.correo.data
        ).first()

        if usuario and check_password_hash(
            usuario.password,
            form.password.data
        ):

            login_user(usuario)

            return redirect(
                url_for("auth.dashboard")
            )

        flash("Credenciales incorrectas")

    return render_template(
        "auth/login.html",
        form=form
    )


@auth.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "dashboard/index.html",
        usuario=current_user
    )


@auth.route("/logout")
def logout():

    logout_user()

    return redirect(
        url_for("auth.login")
    )


@auth.route("/solo-admin")
@login_required
@rol_requerido("Administrador")
def solo_admin():

    return "Area exclusiva de administradores"