from app import create_app, db

from app.models.rol import Rol
from app.models.usuario import Usuario

from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():

    if not Rol.query.first():

        administrador = Rol(nombre="Administrador")
        docente = Rol(nombre="Docente")
        estudiante = Rol(nombre="Estudiante")

        db.session.add(administrador)
        db.session.add(docente)
        db.session.add(estudiante)

        db.session.commit()

        print("Roles creados")

    if not Usuario.query.first():

        admin = Usuario(
            nombre="Administrador",
            correo="admin@ues.edu.sv",
            password=generate_password_hash("admin123"),
            rol_id=1
        )

        docente = Usuario(
            nombre="Docente",
            correo="docente@ues.edu.sv",
            password=generate_password_hash("docente123"),
            rol_id=2
        )

        estudiante = Usuario(
            nombre="Estudiante",
            correo="estudiante@ues.edu.sv",
            password=generate_password_hash("estudiante123"),
            rol_id=3
        )

        db.session.add(admin)
        db.session.add(docente)
        db.session.add(estudiante)

        db.session.commit()

        print("Usuarios creados")

print("Proceso completado")