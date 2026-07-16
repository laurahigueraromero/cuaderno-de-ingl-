# Cuaderno de Inglés

Aplicación para guardar y gestionar vocabulario en inglés (palabras y su traducción) y conceptos generales (concepto y su definición), con dos interfaces disponibles: terminal y web.

## Funcionalidades

- Agregar, listar y eliminar **palabras** (palabra / traducción).
- Buscar en traductor **palabras** y posibilidad de guardarla.
- Agregar, listar y eliminar **conceptos** (concepto / definición).
- Cada vez que se agrega o elimina un elemento, se exporta automáticamente a un `.txt` (`palabras.txt` y `conceptos.txt`), siempre sincronizado con la base de datos.
- Dos formas de usar la app:
  - **Terminal** (`main.py`): menú de texto con submenús.
  - **Web** (`app.py`): interfaz gráfica con [Streamlit](https://streamlit.io), con pestañas y estilos personalizados.

## Estructura del proyecto

```
cuaderno.py     Clase Cuaderno: maneja la base de datos y el txt de palabras
conceptos.py    Clase Conceptos: maneja la base de datos y el txt de conceptos
main.py         Interfaz de terminal
app.py          Interfaz web (Streamlit)
estilos.css     Estilos personalizados de la interfaz web
cuaderno.db     Base de datos SQLite de palabras (se crea sola)
conceptos.db    Base de datos SQLite de conceptos (se crea sola)
palabras.txt    Export automático de palabras (se crea sola)
conceptos.txt   Export automático de conceptos (se crea sola)
requirements.txt Dependencias del proyecto
```

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

### Interfaz de terminal

```bash
python main.py
```

Muestra un menú principal con las secciones "Palabras" y "Conceptos", cada una con su propio submenú para agregar, listar y eliminar.

### Interfaz web

```bash
python -m streamlit run app.py
```

Abre automáticamente `http://localhost:8501` en el navegador, con pestañas para Palabras y Conceptos.

## Configuración (opcional)

Las rutas de las bases de datos se pueden personalizar con variables de entorno (por ejemplo en un archivo `.env`):

```
DB_PATH_CUADERNO=cuaderno.db
DB_PATH_CONCEPTOS=conceptos.db
```

Si no se definen, se usan esos mismos valores por defecto.
