import streamlit as st
import pandas as pd

# carga de datos, conexion df
ruta_zni = 'data/ZNI.csv'
df = pd.read_csv(ruta_zni)

st.header('Estado de la Prestación del Servicio de Energía')
st.subheader('Zonas no Interconectadas (ZNI)')
st.text('Conjunto de Datos')

# analisis de los datos
filas = df.shape[0]
columnas =  df.shape[1]

# visualizacion de los datos

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader('Numero Filas')
        st.text(filas)

with col2:
    with st.container(border=True):
         st.subheader('Número de columnas')
         st.text(columnas)

# otra forma de mostrar los datos

col3, col4 = st.columns(2)
with col3:
    st.metric('Numero de filas', filas, border=True)
with col4:
    st.metric ('Numero de columnas', columnas, border=True)


 #st.dataframe(df)
