import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
db_path = os.getenv("DB_PATH_CUADERNO", "cuaderno.db")

def crear_tabla():
    with sqlite3.connect(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cuaderno (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                word TEXT NOT NULL,
                translate  TEXT NOT NULL
            )
        """)

def insertar_palabra(word, translate):
    with sqlite3.connect(db_path) as conn:
        conn.execute("INSERT INTO cuaderno (word, translate) VALUES (?, ?)", (word, translate))
        conn.commit()

def listar_palabras():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute("SELECT * FROM cuaderno")
        return cursor.fetchall()
    
class Cuaderno:
    def __init__(self, txt_path="palabras.txt"):
        self.txt_path = txt_path
        crear_tabla()

    def _exportar_txt(self):
        with open(self.txt_path, "w", encoding="utf-8") as f:
            for palabra in self.obtener_palabras():
                f.write(f"{palabra[1]} - {palabra[2]}\n")

    def agregar_palabra(self, word, translate):
        insertar_palabra(word, translate)
        self._exportar_txt()

    def obtener_palabras(self):
        return listar_palabras()

    def eliminar_palabra(self, id_):
        with sqlite3.connect(db_path) as conn:
            conn.execute("DELETE FROM cuaderno WHERE id = ?", (id_,))
            conn.commit()
        self._exportar_txt()