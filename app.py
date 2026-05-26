import pandas as pd
import streamlit as st
import utils as ut
from PIL import Image
from utils import PATH

# Configuración de la página
st.set_page_config(page_title="SMEC",
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
    st.title("Síndrome Metabólico de Enfermedad Cardiovascular")

    # Texto de introducción
    st.write(
        """
Determinar si un paciente al cual se le realizan diferentes estudios clínicos
para hallar enfermedades como: Hipertensión, Hiperglusemia, Colesterol HDL
bajo, Hipertriglidicemia, Trastorno de cintura-altura y poliúrea. Además, se
le preguntan datos como: Edad, Género, si fuma y si consume licor.
Todo esto con la finalidad de diagnosticar si la persona posee un síndrome
metabólico asociado a enfermedad cardiovascular (SMEC), a la cual llamaremos
enferdedad, una variable categórica que vamos a predecir a través del modelo
de Bosques Aleatorios (Random Forest).
Los datos se encuentran en la carpeta:\n\n
https://drive.google.com/drive/folders/1IynJDozf6bXvoPjegsGMstVvijMhvpaf?
usp=drive_link
"""
    )

    # imagen 
    imagen = Image.open(PATH + "media/imagen_fondo.jpeg")
    st.image(
        image=imagen,
        caption="Enfermedad Cardiovascular", 
        width=700
        )
    
    # Subtítulo 
    st.header("Key Performance Indicators (KPIs)")

    # Texto de conceptualización
    st.write(
"""
- KPI: Identificar a través de los parámetros de las enfermedades de base de
cada paciente, y sus datos médicos generales como el género, la edad, si
consume o no, tabaco y alcohol, para determinar si el paciente puede padecer
SMEC.
"""
    )









