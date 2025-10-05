import random
import sqlite3
from faker import Faker
from pathlib import Path

# Especificar ruta del archivo(Base de datos) a crear o actualizar.
ruta_bd = Path(r"D:\py_programs\BASES_DATOS\Users.db")

# Asegurar que la carpeta existe
ruta_bd.parent.mkdir(parents=True, exist_ok=True)

fake = Faker()


def generar_datos_aleatorios(num_filas):
    datos = []
    for i in range(num_filas):
        fila = {
            "ID": i + 1,
            "NAME": f"{fake.first_name()}_{random.randint(1, 100)}",
            "AGE": random.randint(18, 99),
            "EMAIL": f"{fake.user_name()}_{random.randint(1000, 9999)}@ejemplo.com",
            "ASOCIATION_NAME": random.choice(
                ["C.T. QUART", "C.V. QUART", "C.G. QUART", "C.P. QUART"]
            ),
            "SPORT": random.choice(["TENIS", "FUTBOL", "PADEL", "GOLF"]),
        }
        datos.append(fila)
    return datos


if __name__ == "__main__":
    num_filas = 100
    datos_aleatorios = generar_datos_aleatorios(num_filas)
    for dato in datos_aleatorios:
        print(dato)

    with sqlite3.connect(ruta_bd) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Users
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT,
                        AGE INTEGER,
                        EMAIL TEXT,
                        ASOCIATION_NAME TEXT,
                        SPORT TEXT)"""
        )

        for dato in datos_aleatorios:
            cursor.execute(
                """INSERT INTO Users (NAME, AGE, EMAIL, ASOCIATION_NAME, SPORT)
                              VALUES (?, ?, ?, ?, ?)""",
                (
                    dato["NAME"],
                    dato["AGE"],
                    dato["EMAIL"],
                    dato["ASOCIATION_NAME"],
                    dato["SPORT"],
                ),
            )
        conn.commit()
