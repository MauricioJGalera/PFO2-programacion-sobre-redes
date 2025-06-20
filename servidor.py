from flask import Flask, request, jsonify, render_template
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# ---------- Inicializar la base de datos ----------
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# ---------- Ruta: Registro ----------
@app.route('/registro', methods=['POST'])
def registrar_usuario():
    datos = request.get_json()
    usuario = datos.get('usuario')
    password = datos.get('password')

    if not usuario or not password:
        return jsonify({'error': 'Usuario y password requeridos'}), 400

    hash_password = generate_password_hash(password)

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, password) VALUES (?, ?)", (usuario, hash_password))
        conn.commit()
        conn.close()
        return jsonify({'mensaje': 'Usuario registrado correctamente'})
    except sqlite3.IntegrityError:
        return jsonify({'error': 'El usuario ya existe'}), 409

# ---------- Ruta: Login ----------
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    password = datos.get('password')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and check_password_hash(resultado[0], password):
        return jsonify({'mensaje': f'Bienvenido {usuario}'}), 200
    else:
        return jsonify({'error': 'Credenciales inválidas'}), 401

# ---------- Ruta: Tareas (GET) ----------
@app.route('/tareas', methods=['GET'])
def tareas():
    return render_template('index.html')

# ---------- Iniciar servidor ----------
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
