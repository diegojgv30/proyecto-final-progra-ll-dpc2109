# Sistema de Control Estudiantil

Proyecto Final de Programación II desarrollado utilizando Flask, SQLite, SQLAlchemy, Flask-Login y GitHub.

---

# Descripción

El Sistema de Control Estudiantil es una aplicación web que permite administrar información académica dentro de una institución educativa.

El sistema incluye:

* Inicio de sesión.
* Control de acceso por roles.
* Gestión de estudiantes.
* Gestión de asignaturas.
* Gestión de calificaciones.
* Base de datos SQLite.
* Trabajo colaborativo mediante Git y GitHub.

---

# Tecnologías Utilizadas

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

# Estructura del Proyecto

```text
.
├── app
│   ├── controllers
│   ├── forms
│   ├── models
│   ├── static
│   └── templates
│
├── config
│   ├── __init__.py
│   ├── database.py
│   └── settings.py
│
├── instance
│   └── control_estudiantil.db
│
├── crear_db.py
├── cargar_datos.py
├── requirements.txt
├── run.py
├── README.md
└── GUIA_DESARROLLO.md
```

---

# Carpeta de Configuración

El proyecto utiliza una carpeta denominada:

```text
config/
```

para centralizar la configuración del sistema.

## settings.py

Contiene la configuración general de Flask:

* SECRET_KEY
* Configuración de SQLAlchemy
* Configuración de la conexión a la base de datos

## database.py

Contiene la instancia principal de SQLAlchemy utilizada por todos los modelos del sistema.

Esta estructura permite separar la configuración de la lógica de negocio y sigue los estándares de desarrollo establecidos para el proyecto.

---

# Documentación del Proyecto

Antes de comenzar a desarrollar cualquier módulo todos los integrantes deben leer:

```text
README.md
GUIA_DESARROLLO.md
```

## README.md

Contiene:

* Instalación.
* Configuración.
* Uso del proyecto.
* Git y GitHub.
* Creación de ramas.
* Solución de problemas.

## GUIA_DESARROLLO.md

Contiene:

* Normas de desarrollo.
* Normas de diseño.
* Estructura del proyecto.
* Flujo de trabajo.
* Buenas prácticas.
* Reglas de colaboración.

---

# Requisitos

El proyecto puede ejecutarse en cualquiera de los siguientes entornos:

* Windows 10
* Windows 11
* Linux
* WSL2 (Opcional)

Software requerido:

* Python 3.12 o superior.
* Git.
* Visual Studio Code (Recomendado).

---

# Verificar Instalaciones

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

# Clonar el Proyecto

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

# Crear Entorno Virtual

## Windows

```powershell
python -m venv venv
```

## Linux / WSL

```bash
python3 -m venv venv
```

---

# Activar Entorno Virtual

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

Si el entorno se activa correctamente aparecerá:

```text
(venv)
```

al inicio de la línea de comandos.

---

# Instalar Dependencias

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

# Crear la Base de Datos

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

# Cargar Datos Iniciales

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

# Usuarios de Prueba

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

# Ejecutar el Proyecto

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

Abrir en el navegador:

```text
http://127.0.0.1:5000/login
```

---

# Flujo de Trabajo con Git

## Actualizar el Proyecto Antes de Comenzar

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

# Ramas de Trabajo

Para evitar conflictos y mantener organizado el desarrollo, cada integrante debe trabajar exclusivamente en su propia rama.

La rama principal del proyecto es:

```text
main
```

Ningún integrante debe trabajar directamente sobre la rama principal.

---

## Ramas Asignadas

| Integrante | Rama                        |
| ---------- | --------------------------- |
| Diego      | branch-integrante-diego     |
| David      | branch-integrante-david     |
| Alejandra  | branch-integrante-alejandra |
| Lizzette   | branch-integrante-lizzette  |

---

# Crear una Rama por Primera Vez

Después de clonar el proyecto:

```bash
git checkout main

git pull origin main
```

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

# Verificar la Rama Actual

```bash
git branch
```

Ejemplo:

```text
* branch-integrante-david
  main
```

---

# Cambiar a una Rama

```bash
git checkout nombre-rama
```

Ejemplo:

```bash
git checkout branch-integrante-david
```

---

# Reglas para el Uso de Ramas

Cada integrante debe:

* Trabajar únicamente en su propia rama.
* Realizar commits únicamente en su rama.
* Subir cambios únicamente a su rama.

No debe:

* Trabajar directamente sobre main.
* Trabajar sobre la rama de otro integrante.
* Realizar merge directamente a main.

---

# Flujo de Trabajo Diario

## 1. Actualizar la rama principal

```bash
git checkout main

git pull origin main
```

## 2. Cambiar a la rama personal

Ejemplo:

```bash
git checkout branch-integrante-david
```

## 3. Realizar cambios

Desarrollar las funcionalidades asignadas.

## 4. Guardar cambios

```bash
git add .

git commit -m "Descripcion del cambio realizado"
```

## 5. Subir cambios

```bash
git push
```

## 6. Informar al responsable de integración

Cuando el trabajo esté listo para revisión.

---

# Distribución de Trabajo

El proyecto está dividido en cuatro partes para facilitar el trabajo colaborativo.

La asignación definitiva de módulos será realizada por el equipo.

## Persona 1

Estado actual:

Esta parte ya se encuentra desarrollada.

Incluye:

* Arquitectura general del sistema.
* Configuración Flask.
* Configuración de base de datos.
* Login.
* Dashboard.
* Roles y permisos.
* Integración final.
* Resolución de conflictos Git.

Archivos principales:

```text
app/__init__.py

app/models/

config/
├── database.py
└── settings.py

crear_db.py
cargar_datos.py

README.md
GUIA_DESARROLLO.md
```

---

## Persona 2

Responsable de uno de los módulos funcionales del sistema.

Posibles áreas:

* Gestión de estudiantes.
* Gestión de asignaturas.
* Gestión de calificaciones.
* Reportes.

La asignación será definida por el equipo.

---

## Persona 3

Responsable de uno de los módulos funcionales del sistema.

Posibles áreas:

* Gestión de estudiantes.
* Gestión de asignaturas.
* Gestión de calificaciones.
* Reportes.

La asignación será definida por el equipo.

---

## Persona 4

Responsable de uno de los módulos funcionales del sistema.

Posibles áreas:

* Gestión de estudiantes.
* Gestión de asignaturas.
* Gestión de calificaciones.
* Reportes.

La asignación será definida por el equipo.

---

# Archivos Protegidos

Los siguientes archivos no deben modificarse sin coordinación previa con el responsable de integración:

```text
app/__init__.py

app/models/

config/
├── database.py
├── settings.py

crear_db.py
cargar_datos.py
```

---

# Verificación Antes de Subir Cambios

Ejecutar:

```bash
python run.py
```

Verificar:

* El sistema inicia correctamente.
* No existen errores en la consola.
* El login funciona correctamente.
* Las páginas desarrolladas funcionan correctamente.

Luego ejecutar:

```bash
git status
```

Después de realizar commit debe mostrar:

```text
working tree clean
```

---

# Solución de Problemas

## Error al Crear el Entorno Virtual

### Linux / WSL

```bash
sudo apt update

sudo apt install python3-venv
```

Si el problema continúa:

```bash
sudo apt install python3.12-venv
```

---

## Error de Dependencias

### Windows

```powershell
python -m pip install --upgrade pip
```

### Linux / WSL

```bash
pip install --upgrade pip
```

Instalar nuevamente:

```bash
pip install -r requirements.txt
```

---

## La Base de Datos no Existe

Ejecutar:

```bash
python crear_db.py

python cargar_datos.py
```

---

## Verificar SQLite

### Windows

Descargar SQLite desde:

https://www.sqlite.org/download.html

### Linux / WSL

```bash
sudo apt install sqlite3
```

Abrir la base de datos:

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

# Responsable de Integración

El responsable de integración del proyecto es:

```text
Diego
```

Responsabilidades:

* Mantener estable la rama main.
* Revisar cambios de los integrantes.
* Resolver conflictos de Git.
* Integrar módulos al proyecto final.
* Aprobar modificaciones estructurales.

---

# Regla de Integración

Ningún integrante debe realizar merge directamente sobre:

```text
main
```

Toda integración deberá ser revisada previamente por el responsable de integración.

---

# Objetivo Final

Construir una aplicación web funcional que permita administrar estudiantes, asignaturas y calificaciones utilizando Flask, SQLite, SQLAlchemy, Git y GitHub, aplicando buenas prácticas de programación orientada a objetos, desarrollo web y trabajo colaborativo.
