import streamlit as st
import pandas as pd
import utils as ut

# Configuración de la página
st.set_page_config(page_title="Pronóstico",
                   page_icon="❤️‍🩹",
                   layout="wide",
                   initial_sidebar_state="expanded")  # Ctrl + S -> Guardar


# Barra lateral (Menú)
ut.generarMenu()

# Cargar Datos
df_inicial = ut.cargar_datos()

# Presentar la información
st.header("Análisis Exploratorio")
# usamos un contenedor
with st.container(
    border=True,
    width="stretch",
    height="content",
    horizontal_alignment="distribute",
    vertical_alignment="distribute"
    ):    

    ut.eda(df=df_inicial)

# Análisis estadístico
st.header("Análisis Estadístico")
# usamos un contenedor
with st.container(
    border=True,
    width="stretch",
    height="content",
    horizontal_alignment="distribute",
    vertical_alignment="distribute"
    ):    

    ut.estadistico(df=df_inicial)
        
       





