from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):

    correo = StringField(
        "Correo",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Contraseña",
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Iniciar sesión")