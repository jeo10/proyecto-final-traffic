import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import streamlit as st
import requests



# df = pd.read_csv(r"C:\Users\franc\OneDrive\Documentos\Henry\proyectos\PROYECTO_GRUPAL\SEMANA 4\calle_barrio_le.csv")

def vol_enc_cat(vol):
    if vol == 0: 
        return 'liberado'
    elif vol == 1:
        return 'bajo'
    elif vol == 2:
        return 'moderado'
    elif vol == 3:
        return 'alto'
    elif vol == 4:
        return 'muy alto'

data = [['liberado', 'La calle esta libre para circular.'],
        ['bajo', 'El trafico sigue sin significar un problema.'],
        ['moderado', 'La circulación comienza a ser significante.'],
        ['alto', 'Se recomienda estar alerta. Con volumen alto estamos cerca de los picos de circulación de vehiculos'],
        ['muy alto', 'No es recomendable circular por esta calle.']]

tabla_guia = pd.DataFrame(data, columns=['volumen', 'detalle'])


def estado_calles(barrio, hora, df):

    predecir = df[df.boro_le == barrio]
    predecir['hora'] = hora
    predecir = predecir[['hora', 'boro_le', 'street_le']].drop_duplicates()

    filename = "presentacion/pages/modelo_200_vol.sav"
    tree = pickle.load(open(filename, 'rb'))
    estado = tree.predict(predecir)
    resultado = pd.DataFrame()
    resultado['street_le'] = predecir.street_le
    resultado['estado'] = estado

    resultado = pd.merge(resultado, df, on = "street_le", how = "inner")
    resultado = resultado[["street", "estado"]]

    resultado = resultado.drop_duplicates()
    
    resultado['estado'] = resultado['estado'].apply(lambda x: vol_enc_cat(x))

    return resultado.sort_values("estado", ascending = False)


# res = estado_calles(0, 16, df)

url = "http://vps-2671696-x.dattaweb.com/traffic/model/"
response = requests.get(url, timeout=0.5)
df = pd.DataFrame(response.json()["data"])

barrio = st.selectbox('barrio', ("Manhattan", "Queens", "Bronx", "Staten Island", "Brooklyn"))
hora = st.selectbox('hora', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))

if(barrio == "Brooklyn"):
    barrio = 1
elif(barrio == "Staten Island"):
    barrio = 4
elif(barrio == "Queens"):
    barrio = 3
elif(barrio == "Bronx"):
    barrio = 0
elif(barrio == "Manhattan"):
    barrio = 2

st.table(tabla_guia)
st.table(estado_calles(barrio, hora, df))

