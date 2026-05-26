import pandas as pd

ruta_base = r"C:\Users\USUARIO\OneDrive - NEUROMEDICA S.A.S\Escritorio\PROYECTO_ANALISIS_DE_DATOS"
ruta_archivo_distribucion_cartera = r"\Bases_datos\Distribución_de_cartera_por_producto_20260423.xlsx"
ruta_archivo_saldo_captaciones = r"\Bases_datos\Saldo_de_las_captaciones_y_colocaciones_por_municipios_20260429.xlsx"

data_saldo_captaciones = pd.read_excel(f"{ruta_base}\{ruta_archivo_saldo_captaciones}")
data_distribucion_cartera = pd.read_excel(f"{ruta_base}\{ruta_archivo_distribucion_cartera}")

def aplanar_columnas(columns):
    new_cols = []
    for col in columns:
        if isinstance(col,tuple):
            col = [str(c).lower().strip() for c in col
                   if c
                   and
                   "unname" not in str(c).lower()]
            new_cols.append(col[-1])
        else:a
            new_cols.append(str(col).lower().strip())
    return new_cols

data_saldo_captaciones.columns = aplanar_columnas
data_distribucion_cartera.columns = aplanar_columnas
data_distribucion_cartera.columns
data_saldo_captaciones.columns

