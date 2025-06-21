import requests

BASE_URL = "http://localhost:5000"

def registrar():
    print("\n--- Registro de usuario ---")
    usuario = input("Usuario: ")
    password = input("Password: ")
    datos = {"usuario": usuario, "password": password}
    try:
        respuesta = requests.post(f"{BASE_URL}/registro", json=datos)
        print("→", respuesta.json().get("mensaje", "Error"))
    except Exception as e:
        print("Error al conectar con el servidor:", e)

def login():
    print("\n--- Inicio de sesión ---")
    usuario = input("Usuario: ")
    password = input("Password: ")
    datos = {"usuario": usuario, "password": password}
    try:
        respuesta = requests.post(f"{BASE_URL}/login", json=datos)
        print("→", respuesta.json().get("mensaje", "Error"))
    except Exception as e:
        print("Error al conectar con el servidor:", e)

def ver_tareas():
    print("\n--- Página de bienvenida (/tareas) ---")
    try:
        respuesta = requests.get(f"{BASE_URL}/tareas")
        print(respuesta.text)  # muestra HTML plano
    except Exception as e:
        print("Error al conectar con el servidor:", e)

def menu():
    while True:
        print("\n=== Menú ===")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Ver /tareas")
        print("4. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrar()
        elif opcion == "2":
            login()
        elif opcion == "3":
            ver_tareas()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
