import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit.elements.lib.layout_utils import Height
import utils as ut

#Configuración de la página
st.set_page_config(
    "Gráficos", 
    "📊", 
    "wide", 
    initial_sidebar_state="expanded"
    )

ut.generarMenu()

df_inicial = ut.cargar_datos()

tipos_de_grafico = [
    "Dispersión",
    "Histograma",
    "Cajas y Bigotes",
    "Violín",
    "Mapa de Calor",
    "Barras"
]

columnas_numericas = (df_inicial.select_dtypes(include="number")
                        .columns.tolist())
columnas_categoricas = ["Enfermedad"]
alto = 300
sel_color = px.colors.qualitative.Set1

# Dibujar lo que va en la barra lateral
with st.sidebar:
    st.divider()
    st.subheader("Configuración")

    # Caja de selección
    tipo_seleccionado = st.selectbox(
        label="Tipos de Gráfico",
        options= tipos_de_grafico
        )

# Dibujamos dentro del espacio ppal
st.header("Gráficos de SMEC")
st.caption("Explora los diferentes gráficos de la data.")

with st.container(
    border=True,
    vertical_alignment="distribute",
    horizontal_alignment="center"
    ):

    if tipo_seleccionado == "Dispersión":
        # Este graf lo haremos de la siguiente manera:
        col_1, col_2, col_3 = st.columns(3)

        with col_1:
            x = st.selectbox("Variable X", columnas_numericas, key="x")
        with col_2:
            # Esta es la nueva línea mencionada - Quita en y la variable elegida en x
            opciones_y = [opcion for opcion in columnas_numericas if opcion != x]
            y = st.selectbox("Variable Y", opciones_y, key="y")            
        
        st.divider()
        st.markdown(
            f"<h4>{tipo_seleccionado} entre {x} vs {y}</h4>",
            unsafe_allow_html=True
            )
        
        # Hagamos el gráfico
        fig = px.scatter(
            data_frame=df_inicial,
            x=x,
            y=y,
            color=columnas_categoricas[0],
            color_discrete_sequence=sel_color,
            hover_data=df_inicial.columns,
            template="plotly"
        )
        fig.update_layout(height=alto)
        st.plotly_chart(
            figure_or_data=fig,
            width="stretch"
            )

    if tipo_seleccionado == "Barras":
            # Mantenemos las columnas para los selectores
            col_1, col_2, col_3 = st.columns(3)

            with col_1:
                # Para barras, el eje X suele funcionar mejor con variables categóricas
                x = st.selectbox("Variable X (Categoría)", columnas_categoricas, key="x_barras")
            with col_2:
                # El eje Y define la altura, por lo que usa columnas numéricas
                # Esta es la nueva línea mencionada - Quita en y la variable elegida en x
                opciones_y = [opcion for opcion in columnas_numericas if opcion != x]
                y = st.selectbox("Variable Y (Métrica)", opciones_y, key="y_barras")
                        
            st.divider()
            st.markdown(
                f"<h4>Gráfico de {tipo_seleccionado} de {y} por {x}</h4>",
                unsafe_allow_html=True
            )
            
            # Cambiamos px.scatter por px.bar
            fig = px.bar(
                data_frame=df_inicial,
                x=x,
                y=y,
                color=x,  # Colorea las barras según la misma categoría del eje X
                color_discrete_sequence=sel_color,
                hover_data=df_inicial.columns,
                template="plotly"
            )
            
            fig.update_layout(height=alto)
            st.plotly_chart(
                figure_or_data=fig,
                use_container_width=True  # Nota: Cambié width="content" por este parámetro que es el estándar de Streamlit
            )
    
    # Gráfico de histograma
    if tipo_seleccionado == "Histograma":
         
        col_1, col_2, col_3 = st.columns(3)

        with col_1:

            variable = st.selectbox(label="Variable",
                                    options=columnas_numericas)
        
        st.divider()
        st.markdown(f"{tipo_seleccionado} -> {variable}", text_alignment="center")

        fig = px.histogram(data_frame=df_inicial,
                           x=variable,
                           color=columnas_categoricas[0],
                           color_discrete_sequence=sel_color,
                           barmode="overlay", #['stack', 'group', 'overlay', 'relative']
                           marginal="box",
                           template="plotly"
                           )
        fig.update_layout(height=alto,
                          bargap=0.2,
                          bargroupgap=0.2,
                          yaxis_title_text='Pacientes'
                          )
        st.plotly_chart(figure_or_data=fig,
                        width="stretch")


    # Cajas y Bigotes
    if tipo_seleccionado == "Cajas y Bigotes":

        col_1, col_2, col_3 = st.columns(3)
        with col_1:

            variable = st.selectbox(label="Variable",
                                    options=columnas_numericas) 
                   
        st.divider()
        st.markdown(f"{tipo_seleccionado} -> {variable}", text_alignment="center")

        fig = px.box(data_frame=df_inicial,
                     x=variable,
                     y=columnas_categoricas[0],
                     color=columnas_categoricas[0],
                     color_discrete_sequence=sel_color,
                     points="all",  # ['all', 'outliers', 'suspectedoutliers', False]
                     template="plotly"
                     )
        
        fig.update_layout(height=alto, yaxis_title_text="Diagnóstico")

        st.plotly_chart(figure_or_data=fig, width="stretch")

    # Violín
    if tipo_seleccionado == "Violín":

        col_1, col_2, col_3 = st.columns(3)
        with col_1:

            variable = st.selectbox(label="Variable",
                                    options=columnas_numericas) 
                   
        st.divider()
        st.markdown(f"{tipo_seleccionado} -> {variable}", text_alignment="center")

        fig = px.violin(data_frame=df_inicial,
                        x=columnas_categoricas[0],   
                        y=variable,                                                                
                        color=columnas_categoricas[0],
                        box=True,
                        points="all",  
                        color_discrete_sequence=sel_color,                                         
                        template="plotly"
                    )
        fig.update_layout(height=alto,
                          xaxis_title_text='Diagnóstico de SMEC',
                          )
        st.plotly_chart(figure_or_data=fig,
                        width="stretch"
                        )   
    
    # Mapa de Calor
    if tipo_seleccionado == "Mapa de Calor":

        col_1, col_2, col_3 = st.columns(3)
        with col_1:

            colores_px = px.colors.named_colorscales()            

            colores = st.selectbox(label="Escalas de color PX",
                                    options=colores_px,
                                    index=colores_px.index("viridis")
                                    )  
                
        st.markdown(f"{tipo_seleccionado} ⮕ Correlación de Variables", text_alignment="center")

        df_corr = df_inicial.copy()
        df_corr["Enfermedad"] = df_corr["Enfermedad"].map({"SI": 1, "NO": 0})
        corr = df_corr.corr(numeric_only=True)

        fig = px.imshow(img=corr,
                        text_auto=True,
                        aspect="auto",
                        color_continuous_scale=colores,
                        template="plotly"
                        )
        fig.update_layout(height=alto)
        st.plotly_chart(figure_or_data=fig,
                        width="stretch"
                        )














