# GUIA_DESARROLLO.md

# Guía de Desarrollo del Proyecto

## Sistema de Control Estudiantil

Este documento define las normas de desarrollo que todos los integrantes del equipo deben seguir para mantener una estructura uniforme, evitar conflictos y garantizar que el sistema final tenga una apariencia y funcionamiento consistentes.

---

# Objetivo

El objetivo de esta guía es establecer:

* Estándares de programación.
* Estándares de diseño visual.
* Flujo de trabajo con Git.
* Distribución de responsabilidades.
* Reglas para la modificación de archivos.

Todos los integrantes deben leer este documento antes de comenzar a desarrollar su módulo.

---

# Arquitectura del Proyecto

El sistema está desarrollado utilizando Flask bajo una estructura organizada por responsabilidades.

```text
app/
├── controllers/
├── forms/
├── models/
├── static/
│   ├── css/
│   ├── img/
│   └── js/
│
├── templates/
│   ├── auth/
│   ├── dashboard/
│   ├── estudiantes/
│   ├── asignaturas/
│   ├── calificaciones/
│   └── components/
│
└── __init__.py
```

---

# Distribución de Responsabilidades

## Persona 1

Responsable de:

* Arquitectura general.
* Configuración Flask.
* Base de datos.
* Login.
* Dashboard.
* Roles y permisos.
* Integración final.
* Resolución de conflictos Git.

Archivos principales:

```text
app/__init__.py
config.py
app/models/
app/controllers/auth_controller.py
app/controllers/dashboard_controller.py
```

---

## Persona 2

Responsable de:

* CRUD Estudiantes.

Archivos:

```text
app/controllers/estudiante_controller.py
app/forms/estudiante_form.py
app/templates/estudiantes/
```

---

## Persona 3

Responsable de:

* CRUD Asignaturas.

Archivos:

```text
app/controllers/asignatura_controller.py
app/forms/asignatura_form.py
app/templates/asignaturas/
```

---

## Persona 4

Responsable de:

* CRUD Calificaciones.
* Reportes.

Archivos:

```text
app/controllers/calificacion_controller.py
app/forms/calificacion_form.py
app/templates/calificaciones/
```

---

# Archivos Protegidos

Los siguientes archivos NO deben modificarse sin autorización de la Persona 1.

```text
app/__init__.py
config.py
crear_db.py
cargar_datos.py
app/models/
```

La modificación accidental de estos archivos puede afectar a todo el proyecto.

---

# Estándares de Interfaz Gráfica

Todos los módulos deben mantener la misma apariencia visual.

No se deben crear diseños independientes para cada módulo.

---

# Plantilla Base Obligatoria

Todas las vistas deben extender:

```html
{% extends "base.html" %}
```

Ejemplo:

```html
{% extends "base.html" %}

{% block title %}
Mi Página
{% endblock %}

{% block content %}

Contenido de la página.

{% endblock %}
```

No se debe crear un archivo HTML completo con:

```html
<html>
<head>
<body>
```

porque eso ya existe en:

```text
app/templates/base.html
```

---

# Componentes Comunes

Los siguientes componentes ya están creados y deben reutilizarse:

```text
Navbar
Footer
Bootstrap
style.css
```

Ubicación:

```text
app/templates/components/
app/static/css/style.css
```

---

# Bootstrap

Bootstrap es obligatorio para todo el proyecto.

Debe utilizarse para:

* Formularios.
* Tablas.
* Botones.
* Cards.
* Navegación.
* Layout.

Ejemplos recomendados:

```html
container
row
col-md-6
col-lg-4
card
table
btn
```

---

# CSS Personalizado

Todos los estilos personalizados deben agregarse únicamente en:

```text
app/static/css/style.css
```

No crear archivos CSS adicionales sin coordinación.

---

# Estilos Inline

Evitar:

```html
style="color:red"
style="width:100%"
```

Los estilos deben declararse en:

```text
style.css
```

---

# Colores

Utilizar la paleta estándar de Bootstrap.

Ejemplos:

```html
bg-primary
bg-success
bg-warning
bg-danger
text-primary
text-success
```

---

# Formularios

Todos los formularios deben seguir la misma estructura.

Ejemplo:

```html
<div class="mb-3">

    <label class="form-label">
        Nombre
    </label>

    <input
        type="text"
        class="form-control">

</div>
```

---

# Tablas

Todos los listados deben utilizar:

```html
<table class="table table-striped table-hover">
```

Ejemplo:

```html
<table class="table table-striped table-hover">

    <thead>

        <tr>
            <th>ID</th>
            <th>Nombre</th>
        </tr>

    </thead>

    <tbody>

    </tbody>

</table>
```

---

# Botones

Utilizar siempre Bootstrap.

## Crear

```html
btn btn-primary
```

## Editar

```html
btn btn-warning
```

## Eliminar

```html
btn btn-danger
```

## Consultar

```html
btn btn-info
```

## Guardar

```html
btn btn-success
```

---

# Tarjetas (Cards)

Las pantallas principales deben utilizar cards para mostrar información.

Ejemplo:

```html
<div class="card shadow-sm">

    <div class="card-body">

        Contenido

    </div>

</div>
```

---

# Responsividad

Todas las páginas deben funcionar correctamente en:

* Computadora.
* Tablet.
* Teléfono móvil.

Utilizar siempre:

```html
row
col-md
col-lg
```

Evitar tamaños fijos.

Incorrecto:

```html
width: 800px
```

Correcto:

```html
col-md-6
```

---

# Flujo de Trabajo con Git

Antes de comenzar:

```bash
git checkout main

git pull origin main
```

---

# Crear Rama Personal

Cada integrante debe trabajar únicamente en su rama.

Persona 2:

```bash
git checkout -b feature-estudiantes
```

Persona 3:

```bash
git checkout -b feature-asignaturas
```

Persona 4:

```bash
git checkout -b feature-calificaciones
```

---

# Guardar Cambios

Verificar estado:

```bash
git status
```

Agregar cambios:

```bash
git add .
```

Crear commit:

```bash
git commit -m "Descripcion del cambio"
```

Subir cambios:

```bash
git push origin nombre-rama
```

---

# Commits Recomendados

Ejemplos:

```text
Crear CRUD estudiantes
Agregar formulario asignaturas
Implementar listado calificaciones
Corregir validaciones estudiante
Mejorar interfaz dashboard
```

Evitar mensajes como:

```text
Cambios
Prueba
Update
asdf
```

---

# Verificación Antes de Subir Cambios

Ejecutar:

```bash
python run.py
```

Verificar:

* El proyecto inicia correctamente.
* No hay errores en consola.
* Las páginas cargan correctamente.

---

# Antes de Solicitar Integración

Verificar:

```bash
git status
```

Debe mostrar:

```text
working tree clean
```

---

# Manejo de Errores

Si el proyecto deja de funcionar después de una actualización:

Actualizar rama principal:

```bash
git checkout main

git pull origin main
```

Volver a la rama de trabajo:

```bash
git checkout nombre-rama
```

Revisar conflictos antes de continuar.

---

# Buenas Prácticas

## Hacer

* Crear commits frecuentes.
* Probar antes de subir cambios.
* Mantener código organizado.
* Utilizar Bootstrap.
* Reutilizar componentes existentes.

## No Hacer

* Modificar archivos protegidos.
* Subir la base de datos SQLite.
* Subir la carpeta venv.
* Crear estilos duplicados.
* Modificar trabajo de otro integrante sin autorización.

---

# Objetivo Final

Todos los módulos deben integrarse en una única aplicación web funcional, manteniendo una apariencia uniforme, una estructura organizada y un flujo de trabajo colaborativo que permita entregar un producto estable y fácil de mantener.
