import random 
import requests
import streamlit as st

from cuaderno import Cuaderno
from conceptos import Conceptos

# Metadatos =>
st.set_page_config(page_title="Cuaderno de Inglés")

def cargar_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

cargar_css("estilos.css")

cuaderno = Cuaderno()
conceptos = Conceptos()

# Título =>
st.title("Cuaderno de Inglés")
st.header("Agrega y gestiona tus palabras y conceptos")

# st.tabs pestañas navegables ==>
tab_palabras, tab_conceptos, tab_phrasal = st.tabs(["Palabras", "Conceptos", "Phrasal Verbs"])

with tab_palabras:
    st.subheader("Agregar palabra")
    with st.form("form_palabra", clear_on_submit=True):
        word = st.text_input("Palabra")
        translate = st.text_input("Traducción")
        if st.form_submit_button("Agregar"):
            if word and translate:
                cuaderno.agregar_palabra(word, translate)
                st.success(f"Palabra '{word}' agregada.")
            else:
                st.warning("Completa ambos campos.")

    st.subheader("Palabras guardadas")
    palabras = cuaderno.obtener_palabras()
    if palabras:
        for id_, word, translate in palabras:
            col1, col2, col3 = st.columns([3, 3, 1])
            col1.write(word)
            col2.write(translate)
            if col3.button("Eliminar", key=f"del_word_{id_}"):
                cuaderno.eliminar_palabra(word)
                st.rerun()
    else:
        st.info("No hay palabras guardadas.")

with tab_conceptos:
    st.subheader("Agregar concepto")
    with st.form("form_concepto", clear_on_submit=True):
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
        for id_, concepto, definicion in lista:
            col1, col2, col3 = st.columns([3, 3, 1])
            col1.write(concepto)
            col2.write(definicion)
            if col3.button("Eliminar", key=f"del_concepto_{id_}"):
                conceptos.eliminar_concepto(concepto)
                st.rerun()
    else:
        st.info("No hay conceptos guardados.")

# --- PESTAÑA: UN PHRASAL VERB ALEATORIO (CORREGIDA) ---
with tab_phrasal:
    st.subheader("Phrasal Verb del Día")
    st.write("¡Practica tu inglés! Presiona el botón para descubrir un verbo aleatorio.")

    # Base de datos local de verbos para elegir al azar
    LISTA_VERBOS = [
        "bring up", "call off", "carry on", "cheer up", "come across",
        "get along", "give up", "go on", "look after", "look up"
    ]

    # Inicializamos las variables en el estado de la sesión si no existen
    if "verbo_actual" not in st.session_state:
        st.session_state.verbo_actual = None
    if "definicion_actual" not in st.session_state:
        st.session_state.definicion_actual = None
    if "ejemplo_actual" not in st.session_state:
        st.session_state.ejemplo_actual = None

    # Botón para disparar la ruleta de verbos
    if st.button("🔄 Cargar un Phrasal Verb aleatorio", type="primary"):
        with st.spinner("Buscando en el diccionario..."):
            # Selecciona un verbo al azar de la lista
            verbo_elegido = random.choice(LISTA_VERBOS)
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{verbo_elegido.replace(' ', '%20')}"
            
            try:
                respuesta = requests.get(url, timeout=5)
                
                if respuesta.status_code == 200:
                    datos = respuesta.json()
                    
                    # SOLUCIÓN CRÍTICA: Acceso correcto navegando las listas [0] del JSON de la API
                    primer_resultado = datos[0]
                    primer_significado = primer_resultado['meanings'][0]
                    primera_definicion = primer_significado['definitions'][0]
                    
                    # Guardamos la información limpia en el estado de Streamlit
                    st.session_state.verbo_actual = verbo_elegido.upper()
                    st.session_state.definicion_actual = primera_definicion['definition']
                    st.session_state.ejemplo_actual = primera_definicion.get('example', None)
                else:
                    st.error(f"No se encontraron datos para {verbo_elegido.upper()} (Código {respuesta.status_code})")
            
            except requests.exceptions.RequestException as e:
                st.error(f"Error de red real al conectar con la API: {e}")
            except (KeyError, IndexError):
                st.error("La API devolvió los datos en un formato inesperado para este verbo.")

    # Si ya hay un verbo cargado en la memoria de la sesión, lo pintamos en pantalla
    if st.session_state.verbo_actual:
        st.divider()
        st.markdown(f"## 🎯 {st.session_state.verbo_actual}")
        st.write(f"**Definición:** {st.session_state.definicion_actual}")
        
        if st.session_state.ejemplo_actual:
            st.caption(f"*Ejemplo de uso:* {st.session_state.ejemplo_actual}")
        st.divider()