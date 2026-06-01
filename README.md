# Sistema de Control Estudiantil

Proyecto final de Programación II desarrollado con Flask, SQLite, SQLAlchemy y Flask-Login.

---

# Descripción

El Sistema de Control Estudiantil permite administrar información académica mediante una aplicación web.

El sistema incluye:

* Inicio de sesión.
* Control de acceso por roles.
* Gestión de estudiantes.
* Gestión de asignaturas.
* Gestión de calificaciones.
* Base de datos SQLite.
* Trabajo colaborativo mediante Git y GitHub.

---

# Tecnologías utilizadas

## Backend

* Python 3.12+
* Flask
* SQLAlchemy
* Flask-Login
* Flask-WTF

## Base de Datos

* SQLite

## Frontend

* HTML5
* CSS3
* Bootstrap 5

## Control de Versiones

* Git
* GitHub

---

# Requisitos

El proyecto puede ejecutarse en cualquiera de los siguientes entornos:

* Windows 10 u 11
* Linux
* WSL2 (Opcional)

Software requerido:

* Python 3.12 o superior
* Git
* Visual Studio Code (Recomendado)

---

# Verificar instalaciones

## Windows

Abrir PowerShell:

```powershell
python --version
git --version
```

## Linux / WSL

```bash
python3 --version
git --version
```

---

# Clonar el proyecto

## Windows

```powershell
git clone https://github.com/diegojgv30/proyecto-final-progra-ll-dpc2109.git

cd proyecto-final-progra-ll-dpc2109
```

## Linux / WSL

```bash
git clone https://github.com/diegojgv30/proyecto-final-progra-ll-dpc2109.git

cd proyecto-final-progra-ll-dpc2109
```

---

# Crear entorno virtual

## Windows

```powershell
python -m venv venv
```

## Linux / WSL

```bash
python3 -m venv venv
```

---

# Activar entorno virtual

## Windows - PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

## Windows - CMD

```cmd
venv\Scripts\activate
```

## Linux / WSL

```bash
source venv/bin/activate
```

Al activarse correctamente aparecerá algo similar a:

```text
(venv)
```

al inicio de la línea de comandos.

---

# Instalar dependencias

## Windows

```powershell
pip install -r requirements.txt
```

## Linux / WSL

```bash
pip install -r requirements.txt
```

Verificar instalación:

```bash
pip list
```

---

# Crear la base de datos

## Windows

```powershell
python crear_db.py
```

## Linux / WSL

```bash
python crear_db.py
```

Resultado esperado:

```text
Base de datos creada correctamente
```

---

# Cargar datos iniciales

## Windows

```powershell
python cargar_datos.py
```

## Linux / WSL

```bash
python cargar_datos.py
```

Resultado esperado:

```text
Roles creados
Usuarios creados
Proceso completado
```

---

# Usuarios de prueba

## Administrador

Correo:

```text
admin@ues.edu.sv
```

Contraseña:

```text
admin123
```

---

## Docente

Correo:

```text
docente@ues.edu.sv
```

Contraseña:

```text
docente123
```

---

## Estudiante

Correo:

```text
estudiante@ues.edu.sv
```

Contraseña:

```text
estudiante123
```

---

# Ejecutar el proyecto

## Windows

```powershell
python run.py
```

## Linux / WSL

```bash
python run.py
```

Resultado esperado:

```text
Running on http://127.0.0.1:5000
```

Abrir navegador:

```text
http://127.0.0.1:5000/login
```

---

# Flujo de trabajo con Git

## Actualizar proyecto antes de comenzar

### Windows

```powershell
git checkout main
git pull origin main
```

### Linux / WSL

```bash
git checkout main
git pull origin main
```

---

# Creación de ramas de trabajo

Para evitar conflictos y mantener organizado el desarrollo del proyecto, cada integrante debe trabajar únicamente en su propia rama.

La rama principal del proyecto es:

```text
main
```

Ningún integrante debe trabajar directamente sobre la rama `main`.

---

## Ramas asignadas

| Integrante | Rama                        |
| ---------- | --------------------------- |
| Diego      | branch-integrante-diego     |
| David      | branch-integrante-david     |
| Alejandra  | branch-integrante-alejandra |
| Lizzette   | branch-integrante-lizzette  |

---

## Crear una rama por primera vez

Después de clonar el proyecto:

```bash
git checkout main

git pull origin main
```

Crear la rama correspondiente:

### Diego

```bash
git checkout -b branch-integrante-diego

git push -u origin branch-integrante-diego
```

### David

```bash
git checkout -b branch-integrante-david

git push -u origin branch-integrante-david
```

### Alejandra

```bash
git checkout -b branch-integrante-alejandra

git push -u origin branch-integrante-alejandra
```

### Lizzette

```bash
git checkout -b branch-integrante-lizzette

git push -u origin branch-integrante-lizzette
```

---

## Verificar la rama actual

Antes de comenzar a trabajar siempre ejecutar:

```bash
git branch
```

La rama activa aparecerá marcada con un asterisco (*).

Ejemplo:

```text
* branch-integrante-david
  main
```

---

## Cambiar a la rama personal

Si se encuentra en otra rama:

```bash
git checkout nombre-rama
```

Ejemplo:

```bash
git checkout branch-integrante-david
```

---

## Regla importante

Cada integrante debe trabajar únicamente en:

* Su propia rama.
* Sus propios archivos asignados.

No debe modificar:

* La rama main.
* Las ramas de otros integrantes.
* Los archivos protegidos definidos en esta documentación.

---

## Flujo de trabajo diario

1. Actualizar la rama principal.

```bash
git checkout main

git pull origin main
```

2. Cambiar a la rama personal.

```bash
git checkout branch-integrante-nombre
```

3. Realizar cambios.

4. Guardar cambios.

```bash
git add .

git commit -m "Descripcion del cambio realizado"
```

5. Subir cambios.

```bash
git push
```

6. Informar al responsable de integración cuando el módulo esté listo para revisión.

---

# Guardar cambios

Verificar cambios:

```bash
git status
```

Agregar cambios:

```bash
git add .
```

Crear commit:

```bash
git commit -m "Descripcion del cambio realizado"
```

Subir cambios:

```bash
git push origin nombre-rama
```

Ejemplo:

```bash
git push origin feature-estudiantes
```

---

# Distribución de trabajo

## Persona 1

Responsable de:

* Arquitectura del sistema
* Configuración Flask
* Base de datos
* Login
* Dashboard
* Roles
* Integración final

Archivos principales:

```text
app/__init__.py
config.py
app/controllers/auth_controller.py
app/controllers/dashboard_controller.py
app/models/
```

---

## Persona 2

Responsable de:

* CRUD Estudiantes

Archivos:

```text
app/controllers/estudiante_controller.py
app/forms/estudiante_form.py
app/templates/estudiantes/
```

---

## Persona 3

Responsable de:

* CRUD Asignaturas

Archivos:

```text
app/controllers/asignatura_controller.py
app/forms/asignatura_form.py
app/templates/asignaturas/
```

---

## Persona 4

Responsable de:

* CRUD Calificaciones
* Reportes

Archivos:

```text
app/controllers/calificacion_controller.py
app/forms/calificacion_form.py
app/templates/calificaciones/
```

---

# Archivos protegidos

Los siguientes archivos no deben modificarse sin coordinación con la Persona 1:

```text
app/__init__.py
config.py
app/models/
crear_db.py
cargar_datos.py
```

---

# Verificación antes de subir cambios

Ejecutar:

```bash
python run.py
```

Verificar que:

* El sistema inicia correctamente.
* No existen errores en la consola.
* Se puede acceder al login.

Luego ejecutar:

```bash
git status
```

Debe mostrar:

```text
working tree clean
```

después del commit.

---

# Solución de problemas

## Error al crear entorno virtual en Linux o WSL

Instalar:

```bash
sudo apt update

sudo apt install python3-venv
```

Si el problema continúa:

```bash
sudo apt install python3.12-venv
```

---

## Error de dependencias

Actualizar pip:

### Windows

```powershell
python -m pip install --upgrade pip
```

### Linux / WSL

```bash
pip install --upgrade pip
```

Luego:

```bash
pip install -r requirements.txt
```

---

## La base de datos no existe

Ejecutar nuevamente:

```bash
python crear_db.py
```

Después:

```bash
python cargar_datos.py
```

---

## Verificar la base de datos SQLite

### Instalar SQLite

#### Windows

Descargar desde:

https://www.sqlite.org/download.html

#### Linux / WSL

```bash
sudo apt install sqlite3
```

### Abrir base de datos

```bash
sqlite3 instance/control_estudiantil.db
```

Mostrar tablas:

```sql
.tables
```

Mostrar usuarios:

```sql
SELECT id,nombre,correo,rol_id FROM usuarios;
```

Salir:

```sql
.quit
```

---

# Objetivo final

Construir una aplicación web funcional que permita administrar estudiantes, asignaturas y calificaciones utilizando Flask, SQLite, SQLAlchemy, Git y GitHub, aplicando buenas prácticas de programación orientada a objetos y trabajo colaborativo.
