import pandas as pd
import streamlit as st
import utils as ut
from PIL import Image
from utils import PATH

# Configuración de la página
st.set_page_config(page_title="Centro de Análisis Crediticio",
                   page_icon="❤️‍🩹",
                   layout="wide",
                   initial_sidebar_state="expanded")  # Ctrl + S -> Guardar

# Barra lateral (Menú)
ut.generarMenu()

# Contenido principal 
col_1, col_2, col_3 = st.columns(
    spec=[0.2,1,0.2],
    gap="small",
    vertical_alignment="center",
    border=False,
    width="stretch"
)

with col_2:
    # Título
    st.title("Visión integral 360° del comportamiento crediticio en Colombia")

    # Texto de introducción
    st.write(
        """
El proyecto “Visión integral 360° del comportamiento crediticio” surge como una iniciativa orientada al análisis del comportamiento de la cartera financiera en Colombia, tomando como eje principal la información de entidades bancarias y municipios del país durante el período comprendido de último corte de 2025. A partir de una base de datos amplia y estructurada, que integra variables relacionadas con colocaciones, captaciones, tipos de entidades financieras y distribución territorial del crédito, se busca identificar patrones, tendencias y variaciones en el comportamiento financiero de las diferentes regiones del país.

El análisis de datos aplicado al sector financiero permite comprender cómo evoluciona la dinámica crediticia en los municipios colombianos, evidenciando diferencias regionales, niveles de acceso al crédito, concentración de cartera y posibles riesgos asociados al comportamiento económico de cada territorio. Asimismo, este proyecto pretende transformar grandes volúmenes de información en conocimiento útil para la toma de decisiones estratégicas, tanto para entidades financieras como para organismos de control, investigadores y actores económicos interesados en el desarrollo financiero nacional.

"""
    )

    # imagen 
    imagen = Image.open(PATH + "media/Imagen_Inicio.png")
    st.image(
        image=imagen,
        caption="Cartera Financiera en Colombia", 
        width=600
        )
    
    # Subtítulo 
    st.header("Key Performance Indicators (KPIs)")

    # Texto de conceptualización
    st.write(
"""
- KPI: Identificar a través de los parámetros de parametros financieros de base de
la cartera,  entidades finacieras,demograficas, municipios y departamentos y comportamientos estadisticos a partir de estos.
"""
    )









