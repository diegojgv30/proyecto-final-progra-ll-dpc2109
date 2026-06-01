from functools import wraps

from flask_login import current_user

from flask import abort


def rol_requerido(nombre_rol):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            if current_user.rol.nombre != nombre_rol:
                abort(403)

            return func(*args, **kwargs)

        return wrapper

    return decorator