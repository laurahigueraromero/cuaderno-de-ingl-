import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
db_path = os.getenv("DB_PATH_CONCEPTOS", "conceptos.db")

def crear_tabla():
    with sqlite3.connect(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS conceptos (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                concepto TEXT NOT NULL,
                definicion  TEXT NOT NULL
            )
        """)

def insertar_concepto(concepto, definicion):
    with sqlite3.connect(db_path) as conn:
        conn.execute("INSERT INTO conceptos (concepto, definicion) VALUES (?, ?)", (concepto, definicion))
        conn.commit()

def listar_conceptos():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute("SELECT * FROM conceptos")
        return cursor.fetchall()

class Conceptos:
    def __init__(self, txt_path="conceptos.txt"):
        self.txt_path = txt_path
        crear_tabla()

    def _exportar_txt(self):
        with open(self.txt_path, "w") as f:
            for c in self.obtener_conceptos():
                f.write(f"{c[1]} - {c[2]}\n")

    def agregar_concepto(self, concepto, definicion):
        insertar_concepto(concepto, definicion)
        self._exportar_txt()

    def obtener_conceptos(self):
        return listar_conceptos()

    def eliminar_concepto(self, concepto):
        with sqlite3.connect(db_path) as conn:
            conn.execute("DELETE FROM conceptos WHERE concepto = ?", (concepto,))
            conn.commit()
        self._exportar_txt()
