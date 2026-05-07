import streamlit as st
import pandas as pd

import requests
import pandas as pd
from io import StringIO




ruta_zni = 'https://github.com/juliandariogiraldoocampo/analisis_taltech/raw/refs/heads/main/explorador/ZNI.csv'
response = requests.get(ruta_zni, verify=False)

df = pd.read_csv(StringIO(response.text))

st.header('Estado de la Prestación del Servicio de Energía')
st.subheader('Zonas no Interconectadas (ZNI)')
st.text('Conjunto de Datos')

st.dataframe(df)
