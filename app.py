import random 
import requests
import streamlit as st

from cuaderno import Cuaderno
from conceptos import Conceptos

# Metadatos =>
st.set_page_config(page_title="Cuaderno de Inglés")

def cargar_css(path):
    try:
        with open(path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

cargar_css("estilos.css")

cuaderno = Cuaderno()
conceptos = Conceptos()

# Título =>
st.title("Cuaderno de Inglés")
st.header("Agrega y gestiona tus palabras y conceptos")

# st.tabs pestañas navegables ==>
tab_palabras, tab_conceptos, tab_phrasal = st.tabs(["Palabras", "Conceptos", "Phrasal Verbs"])

# ==========================================
# --- PESTAÑA 1: PALABRAS 
# ==========================================
with tab_palabras:
    st.subheader("Agregar palabra")

    if "input_palabra_word" not in st.session_state:
        st.session_state.input_palabra_word = ""
    if "input_palabra_trans" not in st.session_state:
        st.session_state.input_palabra_trans = ""
    if "mensaje_palabra" not in st.session_state:
        st.session_state.mensaje_palabra = None

    def traducir_palabra():
        palabra = st.session_state.input_palabra_word
        if palabra:
            try:
                respuesta = requests.get(
                    "https://api.mymemory.translated.net/get",
                    params={"q": palabra.strip(), "langpair": "en|es"},
                    timeout=5,
                )
                if respuesta.status_code == 200:
                    datos = respuesta.json()
                    st.session_state.input_palabra_trans = datos["responseData"]["translatedText"]
                    st.session_state.mensaje_palabra = ("success", "¡Traducción encontrada! Modifícala si quieres y dale a Guardar.")
                else:
                    st.session_state.mensaje_palabra = ("error", f"No se pudo traducir '{palabra}'.")
            except requests.exceptions.RequestException as e:
                st.session_state.mensaje_palabra = ("error", f"Error de red al conectar con la API: {e}")
            except KeyError:
                st.session_state.mensaje_palabra = ("error", "La API devolvió los datos en un formato inesperado.")
        else:
            st.session_state.mensaje_palabra = ("warning", "Escribe una palabra antes de traducir.")

    def guardar_palabra():
        palabra = st.session_state.input_palabra_word
        traduccion = st.session_state.input_palabra_trans
        if palabra and traduccion:
            cuaderno.agregar_palabra(palabra, traduccion)
            st.session_state.mensaje_palabra = ("success", f"Palabra '{palabra}' agregada con éxito.")
            st.session_state.input_palabra_word = ""
            st.session_state.input_palabra_trans = ""
        else:
            st.session_state.mensaje_palabra = ("warning", "Completa ambos campos antes de guardar.")

    st.text_input("Palabra (Inglés)", key="input_palabra_word")
    st.text_input("Traducción o Definición", key="input_palabra_trans")

    col_btn1, col_btn2 = st.columns(2)
    col_btn1.button("🌐 Traducir", use_container_width=True, on_click=traducir_palabra)
    col_btn2.button("💾 Guardar Palabra", type="primary", use_container_width=True, on_click=guardar_palabra)

    if st.session_state.mensaje_palabra:
        tipo, texto = st.session_state.mensaje_palabra
        getattr(st, tipo)(texto)
        st.session_state.mensaje_palabra = None

    st.subheader("Palabras guardadas")
    palabras = cuaderno.obtener_palabras()
    if palabras:
        for id_, w, t in palabras:
            col1, col2, col3 = st.columns([3, 3, 1])
            col1.write(w)
            col2.write(t)
            if col3.button("Eliminar", key=f"del_word_{id_}"):
                cuaderno.eliminar_palabra(id_)
                st.rerun()
    else:
        st.info("No hay palabras guardadas.")


# ==========================================
# --- PESTAÑA 2: CONCEPTOS -----------------
# ==========================================
with tab_conceptos:
    st.subheader("Agregar concepto")
    with st.form("form_concepto_unico", clear_on_submit=True):
        concepto = st.text_input("Concepto")
        definicion = st.text_input("Definición")
        if st.form_submit_button("Agregar"):
            if concepto and definicion:
                conceptos.agregar_concepto(concepto, definicion)
                st.success(f"Concepto '{concepto}' agregado.")
            else:
                st.warning("Completa ambos campos.")

    st.subheader("Conceptos guardados")
    lista = conceptos.obtener_conceptos()
    if lista:
        for id_, comp, dfn in lista:
            col1, col2, col3 = st.columns([3, 3, 1])
            col1.write(comp)
            col2.write(dfn)
            if col3.button("Eliminar", key=f"del_concepto_{id_}"):
                conceptos.eliminar_concepto(id_)
                st.rerun()
    else:
        st.info("No hay conceptos guardados.")


# ==========================================
# --- PESTAÑA 3: PHRASAL VERBS -------------
# ==========================================
with tab_phrasal:
    st.subheader("Phrasal Verb del Día")
    st.write("¡Practica tu inglés! Presiona el botón para descubrir un verbo aleatorio.")

    LISTA_VERBOS = [
        "bring up", "call off", "carry on", "cheer up", "come across",
        "get along", "give up", "go on", "look after", "look up"
    ]

    if "verbo_actual" not in st.session_state:
        st.session_state.verbo_actual = None
    if "definicion_actual" not in st.session_state:
        st.session_state.definicion_actual = None
    if "ejemplo_actual" not in st.session_state:
        st.session_state.ejemplo_actual = None

    if st.button("🔄 Cargar un Phrasal Verb aleatorio", type="primary"):
        with st.spinner("Buscando en el diccionario..."):
            verbo_elegido = random.choice(LISTA_VERBOS)
            verbo_formateado = verbo_elegido.replace(' ', '%20')
            url_phrasal_fija = f"https://api.dictionaryapi.dev/api/v2/entries/en/{verbo_formateado}"
            
            try:
                respuesta = requests.get(url_phrasal_fija, timeout=5)
                if respuesta.status_code == 200:
                    datos = respuesta.json()
                    
                    # CORRECCIÓN DE NAVEGACIÓN JSON (Extracción con índices [0])
                    primer_resultado = datos[0]
                    primer_significado = primer_resultado['meanings'][0]
                    primera_definicion = primer_significado['definitions'][0]
                    
                    st.session_state.verbo_actual = verbo_elegido.upper()
                    st.session_state.definicion_actual = primera_definicion['definition']
                    st.session_state.ejemplo_actual = primera_definicion.get('example', None)
                else:
                    st.error(f"No se encontraron datos para {verbo_elegido.upper()} (Código {respuesta.status_code})")
            
            except requests.exceptions.RequestException as e:
                st.error(f"Error de red al conectar con la API: {e}")
            except (KeyError, IndexError):
                st.error("La API devolvió los datos en un formato inesperado para este verbo.")

    if st.session_state.verbo_actual:
        st.divider()
        st.markdown(f"## 🎯 {st.session_state.verbo_actual}")
        st.write(f"**Definición:** {st.session_state.definicion_actual}")
        
        if st.session_state.ejemplo_actual:
            st.caption(f"*Ejemplo de uso:* {st.session_state.ejemplo_actual}")
        st.divider()


# ==========================================
# --- MODO ESTUDIO -------------------------
# ==========================================
st.divider()
st.subheader("Estudio de palabras y conceptos")

if "estudio_activo" not in st.session_state:
    st.session_state.estudio_activo = False
if "estudio_items" not in st.session_state:
    st.session_state.estudio_items = []
if "indice_actual" not in st.session_state:
    st.session_state.indice_actual = 0
if "mostrar_traduccion" not in st.session_state:
    st.session_state.mostrar_traduccion = False

def empezar_estudio():
    items_palabras = [(w, t) for _, w, t in cuaderno.obtener_palabras()]
    items_conceptos = [(c, d) for _, c, d in conceptos.obtener_conceptos()]
    items = items_palabras + items_conceptos
    random.shuffle(items)
    st.session_state.estudio_items = items
    st.session_state.indice_actual = 0
    st.session_state.mostrar_traduccion = False
    st.session_state.estudio_activo = True

def revelar_traduccion():
    st.session_state.mostrar_traduccion = True

def siguiente_item():
    st.session_state.indice_actual += 1
    st.session_state.mostrar_traduccion = False

def terminar_estudio():
    st.session_state.estudio_activo = False

if not st.session_state.estudio_activo:
    st.button("📚 Empezar el estudio", on_click=empezar_estudio, type="primary")
else:
    items = st.session_state.estudio_items
    if not items:
        st.info("No hay palabras ni conceptos guardados para estudiar.")
        st.button("Salir", on_click=terminar_estudio)
    elif st.session_state.indice_actual >= len(items):
        st.success("¡Has terminado el repaso!")
        st.button("🔄 Volver a empezar", on_click=empezar_estudio, type="primary")
        st.button("Salir", on_click=terminar_estudio)
    else:
        termino, definicion = items[st.session_state.indice_actual]
        st.caption(f"{st.session_state.indice_actual + 1} de {len(items)}")
        st.markdown(f"## {termino}")
        if st.session_state.mostrar_traduccion:
            st.write(f"**Traducción/Definición:** {definicion}")
            st.button("Siguiente ➡️", on_click=siguiente_item, type="primary")
        else:
            st.button("👁️ Mostrar traducción", on_click=revelar_traduccion)
        st.button("Salir del estudio", on_click=terminar_estudio)