import streamlit as st

from cuaderno import Cuaderno
from conceptos import Conceptos
#metadatos=>
st.set_page_config(page_title="Cuaderno de Inglés")
def cargar_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

cargar_css("estilos.css")

cuaderno = Cuaderno()
conceptos = Conceptos()
#titulo=>
st.title("Cuaderno de Inglés")
st.header("Agrega y gestiona tus palabras y conceptos")
#st.tabs pestañas navegables ==>
tab_palabras, tab_conceptos = st.tabs(["Palabras", "Conceptos"])

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
