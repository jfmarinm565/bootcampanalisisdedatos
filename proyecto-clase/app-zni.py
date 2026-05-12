# bases  de datos csv ZNI DEL PROFE Y , DIVIPOLA MIA.
import pandas as pd
import streamlit as st

ruta_zni = 'data\ZNI.csv'
ruta_vivipola = 'data\DIVIPOLA.csv'

df_zni= pd.read_csv(ruta_zni)
df_divipola = pd.read_csv(ruta_vivipola)

# Traer nombre oficial del deartamento
# tabla izq es dvi y tabla derecha es divipola

# Acá comparamos las 2 tablas y creamos la columna con los valores a conservar y hacemos un merge (unir) (join) entre las tablas y se eliminan los duplicados de las tablas.

df_zni = df_zni.merge(
    df_divipola[['Código Departamento','Nombre_departamento']].drop_duplicates('Código Departamento'),left_on='ID DEPATAMENTO',right_on='Código Departamento',how='left'
)
# Eliminamos la tabla temporal que habiamos generado

df_zni['DEPARTAMENTO'] = df_zni['Nombre_departamento']
df_zni= df_zni.drop(columns=['Código Departamento','Nombre_departamento'])

# Traer nombre oficial del MUNICIPIO
# tabla izq es dvi y tabla derecha es divipola

# Acá comparamos las 2 tablas y creamos la columna con los valores a conservar
df_zni = df_zni.merge(
    df_divipola[['Codigo Municipio','Nombre Municipio']].drop_duplicates('Codigo Municipio'),left_on='ID MUNICIPIO',right_on='Codigo Municipio',how='left'
)
# Eliminamos la tabla temporal que habiamos generado

df_zni['MUNICIPIO'] = df_zni['Nombre Municipio']
df_zni= df_zni.drop(columns=['Codigo Municipio','Nombre Municipio'])

# TRAER NOMBRE OFICIAL DE LA LOCALIDAD (Centro Poblado)
df_zni = df_zni.merge(
    df_divipola[['Código Centro Poblado','Nombre Centro Poblado']].drop_duplicates('Código Centro Poblado'),
    left_on='ID LOCALIDAD',
    right_on='Código Centro Poblado',
    how='left'
)

df_zni['LOCALIDAD'] = df_zni['Nombre Centro Poblado']
df_zni = df_zni.drop(columns=['Código Centro Poblado','Nombre Centro Poblado'])

3 #Corregir nombres de DÍA DE DEMANDA MÁXIMA
# listado de nombres sin tilde y con tilde
df_zni['DÍA DE DEMANDA MÁXIMA'] = df_zni['DÍA DE DEMANDA MÁXIMA'].str.upper()
viejos =['MIERCOLES', 'SABADO']
nuevos =['MIÉRCOLES','SÁBADO']

#empaquetamos un diccionario  con los listados de la linea anterior
reemplazos = dict(zip(viejos,nuevos))

#reemplazamos usando los diccionarios
df_zni ['DÍA DE DEMANDA MÁXIMA']= df_zni ['DÍA DE DEMANDA MÁXIMA'].replace(reemplazos)
regex=True

# Agrupar los datos por departamento y por municipio
# sumando los valores de energia activa y reactiva

# CORREGIR PROBLEMAS CON COLUMNAS NUMÉRICAS QUE SON OBJECT

df_zni['ENERGÍA ACTIVA'] = df_zni['ENERGÍA ACTIVA'].str.replace('.', '', regex=False).astype(int)
df_zni['ENERGÍA REACTIVA'] = df_zni['ENERGÍA REACTIVA'].str.replace('.', '', regex=False).astype(int)

# Eliminar TODOS los registros con valores nulos Y ALMACENAR en el mismo dataframe (inplace=True)
df_zni.dropna(inplace = True)

df_zni['POTENCIA MÁXIMA'] = df_zni['POTENCIA MÁXIMA'].str.replace('.', '', regex=False)
df_zni['POTENCIA MÁXIMA'] = df_zni['POTENCIA MÁXIMA'].str.replace(',', '.', regex=False).astype(float).astype(int)

# AGRUPAR LOS DATOS POR DEPARTAMENTO Y POR MUNICIPIO
# SUMANDO LOS VALORES DE ENERGÍA ACTIVA Y REACTIVA
df_agrupado = df_zni.groupby(['DEPARTAMENTO','MUNICIPIO'])[['ENERGÍA ACTIVA', 'ENERGÍA REACTIVA']].sum()

df_pivote = df_zni.pivot_table(
    index='DEPARTAMENTO',
    columns='AÑO SERVICIO',
    values= ['ENERGÍA ACTIVA', 'ENERGÍA REACTIVA'],
    aggfunc='sum'

)
# configuracion de streamlit


# visualizacion de datos

st.image('img/head.png')
st.dataframe(df_pivote)
# hasta aca se sincronizo con gibhub
print('hola mundo')