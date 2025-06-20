PFO 2: Sistema de Gestión de Tareas con API y Base de Datos
Este proyecto implementa una API REST básica usando Flask y SQLite, con registro de usuarios, inicio de sesión y una página de bienvenida. Forma parte de la Propuesta Formativa Obligatoria 2 (PFO 2).

🧰 Tecnologías utilizadas
Python 3

Flask

SQLite

Werkzeug (para hash de contraseñas)

HTML (para la vista de bienvenida)

🗂️ Estructura del Proyecto
markdown
Copiar
Editar
.
├── servidor.py
├── database.db (se crea automáticamente)
├── requirements.txt
├── README.md
└── templates/
    └── bienvenida.html
⚙️ Instalación y ejecución
1. Clonar el repositorio
bash
Copiar
Editar
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
2. Crear entorno virtual (opcional pero recomendado)
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
3. Instalar dependencias
bash
Copiar
Editar
pip install -r requirements.txt
4. Ejecutar el servidor
bash
Copiar
Editar
python servidor.py
✅ La API se iniciará en: http://localhost:5000

🔐 Endpoints disponibles
🧾 POST /registro
Registra un nuevo usuario.

Request JSON:

json
Copiar
Editar
{
  "usuario": "nombre",
  "contraseña": "1234"
}
Respuesta exitosa:

json
Copiar
Editar
{ "mensaje": "Usuario registrado correctamente" }
🔑 POST /login
Inicia sesión con usuario y contraseña.

Request JSON:

json
Copiar
Editar
{
  "usuario": "nombre",
  "contraseña": "1234"
}
Respuesta exitosa:

json
Copiar
Editar
{ "mensaje": "Bienvenido nombre" }
✅ GET /tareas
Muestra un HTML de bienvenida.

Accedé desde el navegador a:
http://localhost:5000/tareas