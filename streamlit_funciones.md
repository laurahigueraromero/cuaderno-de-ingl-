# Funciones de Streamlit

## Las que usamos en `app.py`

| Función | Para qué la usamos |
|---|---|
| `st.set_page_config()` | Configura el título de la pestaña del navegador (`page_title`). Debe ir antes que cualquier otro comando de Streamlit. |
| `st.markdown()` | Inyecta el CSS personalizado (`estilos.css`) y también títulos con formato (`## 🎯 VERBO`). |
| `st.title()` | Título principal de la página ("Cuaderno de Inglés"). |
| `st.header()` | Subtítulo debajo del título principal. |
| `st.subheader()` | Encabezados de sección más pequeños ("Agregar palabra", "Palabras guardadas"...). |
| `st.tabs()` | Crea las pestañas navegables: Palabras, Conceptos, Phrasal Verbs. |
| `st.session_state` | Diccionario persistente entre reruns; guarda el texto de los inputs, mensajes pendientes y el phrasal verb actual. |
| `st.text_input()` | Campos de texto para palabra, traducción, concepto y definición. |
| `st.columns()` | Divide el ancho en columnas (para poner botones o filas de palabra/traducción/eliminar lado a lado). |
| `st.button()` | Botones sueltos (traducir, guardar, eliminar, cargar phrasal verb). |
| `st.form()` / `st.form_submit_button()` | Agrupa los inputs de "Agregar concepto" para que solo se procesen al enviar el formulario (evita reruns en cada tecla). |
| `st.rerun()` | Fuerza que el script se vuelva a ejecutar desde arriba (para refrescar la lista tras guardar/eliminar). |
| `st.success()` | Mensaje verde de confirmación. |
| `st.warning()` | Mensaje amarillo de advertencia (campos vacíos). |
| `st.error()` | Mensaje rojo de error (fallo de red, API, etc.). |
| `st.info()` | Mensaje informativo neutro ("No hay palabras guardadas"). |
| `st.write()` | Muestra texto/datos de forma genérica. |
| `st.spinner()` | Muestra un indicador de carga mientras se espera la respuesta de la API. |
| `st.divider()` | Línea horizontal separadora. |
| `st.caption()` | Texto pequeño y secundario (el ejemplo de uso del phrasal verb). |

## Otras funciones útiles que no usamos (todavía)

| Función | Para qué sirve |
|---|---|
| `st.sidebar` | Barra lateral para navegación o filtros, fuera del flujo principal. |
| `st.selectbox()` | Menú desplegable de opciones (ej: elegir categoría de palabra). |
| `st.multiselect()` | Igual que `selectbox` pero permite elegir varias opciones. |
| `st.radio()` | Botones de opción única (ej: elegir nivel A1/A2/B1). |
| `st.checkbox()` | Casilla de verificación (ej: "marcar como aprendida"). |
| `st.slider()` | Selector numérico deslizante (ej: filtrar por dificultad). |
| `st.date_input()` | Selector de fecha (ej: fecha en que se aprendió la palabra). |
| `st.file_uploader()` | Subir archivos (ej: importar palabras desde un CSV). |
| `st.download_button()` | Botón para descargar un archivo generado (ej: exportar el cuaderno). |
| `st.dataframe()` / `st.table()` | Mostrar tablas de datos con más funcionalidad que columnas manuales (ordenar, buscar). |
| `st.metric()` | Muestra un número destacado con variación (ej: "Palabras aprendidas: 42 ▲3"). |
| `st.progress()` | Barra de progreso (ej: progreso hacia una meta de palabras). |
| `st.expander()` | Sección plegable/desplegable para ocultar contenido opcional. |
| `st.container()` | Agrupa elementos sin dividir columnas; útil para reordenar el layout. |
| `st.empty()` | Marcador de posición que se puede sobrescribir dinámicamente (útil para contenido que cambia sin rerun completo). |
| `st.toast()` | Notificación flotante temporal (alternativa más discreta a `st.success`). |
| `st.dialog()` | Ventana modal emergente (ej: confirmar antes de eliminar). |
| `st.balloons()` / `st.snow()` | Animaciones festivas (ej: al alcanzar una racha de estudio). |
| `st.cache_data()` | Decorador para cachear resultados de funciones costosas (ej: llamadas a la API) y evitar repetirlas innecesariamente. |
| `st.query_params` | Lee/escribe parámetros de la URL (útil para compartir enlaces a una vista concreta). |
| `st.stop()` | Detiene la ejecución del script en ese punto (ej: cortar el flujo si falta un dato obligatorio). |
