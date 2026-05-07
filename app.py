import streamlit as st
import pandas as pd

ruta_zni = 'https://github.com/juliandariogiraldoocampo/analisis_taltech/raw/refs/heads/main/explorador/ZNI.csv'
df = pd.read_csv(ruta_zni)

st.header('Estado de la Prestación del Servicio de Energía')
st.subheader('Zonas no Interconectadas (ZNI)')
st.text('Conjunto de Datos')

st.dataframe(df)
