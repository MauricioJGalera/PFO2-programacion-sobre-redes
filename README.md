# PFO 2: Sistema de Gestión de Tareas con API y Base de Datos
Este proyecto implementa una API REST básica usando Flask y SQLite, con registro de usuarios, inicio de sesión y una página de bienvenida.

## Tecnologías utilizadas
Python 3

Flask

SQLite

Werkzeug (para hash de contraseñas)

HTML (para la vista de bienvenida)


## 🗂️ Estructura del Proyecto
![image](https://github.com/user-attachments/assets/e4ecda8f-2120-4867-b6b2-acad48d4c9f1)

## Instalación y ejecución
1. Crear entorno virtual (opcional pero recomendado)
   
`python -m venv venv`

`.venv\Scripts\activate`

2. Instalar dependencias
   
`pip install -r requirements.txt`

3. Ejecutar el servidor

`python servidor.py`

La API se iniciará en: http://localhost:5000

## Endpoints disponibles
POST /registro

Registra un nuevo usuario.

Request JSON:
{
  "usuario": "nombre",
  "contraseña": "1234"
}

Respuesta exitosa:
{ "mensaje": "Usuario registrado correctamente" }


POST /login

Inicia sesión con usuario y contraseña.

Request JSON:
{
  "usuario": "nombre",
  "contraseña": "1234"
}

Respuesta exitosa:
{ "mensaje": "Bienvenido nombre" }

GET /tareas

Muestra un HTML de bienvenida.

Accedé desde el navegador a:
http://localhost:5000/tareas

