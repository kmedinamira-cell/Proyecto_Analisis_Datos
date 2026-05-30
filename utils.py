from math import exp
import streamlit as st
from PIL import Image
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import graphviz as gz
from pickle import load, dump

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz
from sklearn.metrics import (
    accuracy_score, 
    recall_score, 
    f1_score, 
    roc_auc_score, 
    confusion_matrix, 
    ConfusionMatrixDisplay, 
    RocCurveDisplay, 
    PrecisionRecallDisplay
    )

# pip install scikit-learn

# Rutas
# Ruta en Colab
PATH = ""

# Ruta en Visual
#PATH = ""

def generarMenu():
    with st.sidebar:
        # Creamos dos columnas
        col_1, col_2 = st.columns(spec=2)
        with col_1:
            logo = Image.open(PATH + "media/Logo.png")
            st.image(image=logo,
                    width=110)            
        with col_2:
            st.title("Centro de Análisis Crediticio")

        st.page_link(
            page="app.py", 
            label="Introducción",
            icon="🔍")
        st.page_link(
            page="pages/pronostico.py",
            label="Análisis Estadístico",
            icon="📊"
        ) 
     
        st.page_link(
            page="pages/graficos.py",
            label="Hallazgos y Conclusiones",
            icon="🎯"
        ) 

# Función para cargar los datos
# Decorador para memoria cache
@st.cache_data
def cargar_datos():
    ruta = PATH + "Base_datos/data_saldo_captaciones_final.csv"
    df = pd.read_csv(ruta, encoding="utf-8", sep=",", index_col=0)
    return df

# Método para el análisis inicial de los datos
def eda(df: pd.DataFrame):
    with st.expander(
        "DataSet",
        expanded=False,
        icon="📂"
        ):
        st.dataframe(df, hide_index=True)
    
    with st.expander(
        "Matriz de Correlación",
        expanded=False,
        icon="📂"
        ):
        # Normalizar  datos
        df_norm = df.copy()
        # Mapear la enfermedad
        df_norm["Enfermedad"] = df_norm["Enfermedad"].map({"SI": 1, "NO": 0})
        df_corr = df_norm.corr(method="pearson", numeric_only=True)

        # Gráfico de la matriz de corr...
        fig, ax = plt.subplots(figsize=(8, 6))

        sns.heatmap(
            data=df_corr,
            annot=True,
            cmap="coolwarm",  # paleta de colores
            fmt=".2f",
            ax=ax
        )
        # mostrar  cividis - viridis - blues
        st.pyplot(fig)
    
    with st.expander(
        "Importancia de Features",
        expanded=False
        ):

        corr_target = df_corr["Enfermedad"].sort_values(ascending=False)
        st.dataframe(corr_target)

# Método para mostrar las estadísticas
def estadistico(df: pd.DataFrame):

    #Constantes 
    ancho_st = "stretch"
    alto_st = "stretch"
    bordes = True

    with st.expander("Datos Generales", expanded=False):

        #Total de los datos
        total = len(df)

        # Género
        contar_genero = df["Género"].value_counts()
        feme = contar_genero.get(0, 0)
        masc = contar_genero.get(1, 0)
        pr_feme = feme / total
        pr_masc = masc / total

        # Enfermedad
        contar_diagnos = df["Enfermedad"].value_counts()
        total_si = contar_diagnos.get("SI", 0)
        total_no = contar_diagnos.get("NO", 0)
        pr_diag_si = total_si / total
        pr_diag_no = total_no / total

        # Enfermedad vs género
        df_si = df[df["Enfermedad"] == "SI"]
        contar_genero_si = df_si["Género"].value_counts()
        feme_si = contar_genero_si.get(0, 0)
        masc_si = contar_genero_si.get(1, 0)
        pr_feme_si = feme_si / total_si if total_si else 0
        pr_masc_si = masc_si / total_si if total_si else 0

        # Organicemos con columnas
        col_1, col_2, col_3 = st.columns(
            spec=3, 
            gap="small",
            vertical_alignment="top"
            )

        with col_1:

            st.metric(
                label="Cantidad de Mujeres",
                value=feme,
                delta=f"{pr_feme:.2%}",
                delta_color="violet",
                delta_arrow="up",
                border=bordes,
                width=ancho_st,
                height=alto_st
            )

            st.metric(
                label="Cantidad de Hombres",
                value=masc,
                delta=f"{pr_masc:.2%}",
                delta_color="green",
                delta_arrow="down",
                border=bordes,
                width=ancho_st,
                height=alto_st
            )

        with col_2:

            st.metric(
                label="Diagnósticos Positivos",
                value=total_si,
                delta=f"{pr_diag_si:.2%}",
                delta_color="violet",
                delta_arrow="up",
                border=bordes,
                width=ancho_st,
                height=alto_st
            )

            st.metric(
                label="Diagnósticos Negativos",
                value=total_no,
                delta=f"{pr_diag_no:.2%}",
                delta_color="green",
                delta_arrow="down",
                border=bordes,
                width=ancho_st,
                height=alto_st
            )
        
    # análisis estadístico
    with st.expander("Datos Estadísticos", expanded=True):
        total = len(df)
        # Estadísticas de la edad
        edad_media = df["Edad"].mean()
        edad_mediana = df["Edad"].median()
        edad_moda = df["Edad"].mode()[0]
        edad_std = df["Edad"].std()
        edad_var = df["Edad"].var()
        edad_min = df["Edad"].min()
        edad_max = df["Edad"].max()
        edad_q1 = df["Edad"].quantile(0.25)
        edad_q3 = df["Edad"].quantile(0.75)
        edad_coef_var = (edad_std / edad_media) * 100 if edad_media else 0
        edad_iqr = edad_q3 - edad_q1
