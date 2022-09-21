
###################################################################################################
####################################### importo las librerias #####################################
###################################################################################################

import pandas as pd
import plotly.express as px
import requests
import streamlit as st

# path para correr en mi pc
# cd OneDrive\Documentos\Henry\proyectos\PROYECTO_GRUPAL\SEMANA 3

###################################################################################################
####################################### kpi_day_crash_perc ########################################
###################################################################################################

st.markdown("<h1 style='text-align: center;'>kpi_day_crash_perc</h1>", unsafe_allow_html=True)

# traigo la data de la api
url1 = "http://vps-2671696-x.dattaweb.com/collision/day_crash_perc/"
response = requests.get(url1, timeout=0.5)
df_day_crash = pd.DataFrame(response.json()["data"])

# hago los rename necesarios
df_day_crash["week_day"].replace(0, "monday", inplace = True)
df_day_crash["week_day"].replace(1, "tuesday", inplace = True)
df_day_crash["week_day"].replace(2, "wednesday", inplace = True)
df_day_crash["week_day"].replace(3, "thursday", inplace = True)
df_day_crash["week_day"].replace(4, "friday", inplace = True)
df_day_crash["week_day"].replace(5, "saturday", inplace = True)
df_day_crash["week_day"].replace(6, "sunday", inplace = True)

st.markdown("Cruiosidad: Historicamente el dia con mayor cantidad de colisiones en Nueva York es el dia viernes. Esto se debe a que este dia se acostumbra salir a bares o discos por la noche y, por el consumo de alcohol, se producen mas choques de lo usual.")

# grafico con plotly
trace1 = px.bar(
    df_day_crash,
    x = "week_day",
    y = "collision_count",
    color = "week_day",    
)
# trace1.show()
st.plotly_chart(trace1) #grafico el barplot


###################################################################################################
####################################### kpi_month_crash_perc ######################################
###################################################################################################

st.markdown("<h1 style='text-align: center;'>kpi_month_crash_perc</h1>", unsafe_allow_html=True)

url2 = "http://vps-2671696-x.dattaweb.com/collision/year_month_crash_count/"
response = requests.get(url2, timeout=0.5)
df_month_crash = pd.DataFrame(response.json()["data"])
df_month_crash["month"] = df_month_crash["month"].astype("int32") 
# cambio el tipo de dato de la columna month porque sino no puedo hacer sort

df_month_crash = df_month_crash.groupby("month").sum()
df_month_crash.reset_index(inplace = True)
df_month_crash.sort_values(by = "month", inplace = True)

# hago os rename necesarios
df_month_crash["month"].replace(1, "January", inplace = True)
df_month_crash["month"].replace(2, "February", inplace = True)
df_month_crash["month"].replace(3, "March", inplace = True)
df_month_crash["month"].replace(4, "April", inplace = True)
df_month_crash["month"].replace(5, "May", inplace = True)
df_month_crash["month"].replace(6, "June", inplace = True)
df_month_crash["month"].replace(7, "July", inplace = True)
df_month_crash["month"].replace(8, "August", inplace = True)
df_month_crash["month"].replace(9, "September", inplace = True)
df_month_crash["month"].replace(10, "October", inplace = True)
df_month_crash["month"].replace(11, "November", inplace = True)
df_month_crash["month"].replace(12, "December", inplace = True)

st.markdown("Cruiosidad: Historicamente el mes con mayor cantidad de colisiones en Nueva York es Julio, dado que es el mes donde comienza el receso de verano en Estados Unidos, generando una alta densidad de trafico y siniestros viales.")

# grafico con plotly
trace2 = px.bar(
    df_month_crash,
    x = "month",
    y = "collision_count",
    color = "month",   
)
# trace2.show()
st.plotly_chart(trace2) #grafico el barplot


###################################################################################################
####################################### kpi_time_crash_perc #######################################
###################################################################################################

st.markdown("<h1 style='text-align: center;'>kpi_time_crash_perc</h1>", unsafe_allow_html=True)

url3 = "http://vps-2671696-x.dattaweb.com/collision/time_crash/"
response = requests.get(url3, timeout=0.5)
df_time_crash = pd.DataFrame(response.json()["data"])

# Agrego la columna hora
df_time_crash['hour'] = pd.to_datetime(df_time_crash['crash_time'])
df_time_crash['hour'] = df_time_crash['hour'].dt.to_period('h').dt.hour
df_time_crash = df_time_crash.sort_values("hour")
df_time_crash = df_time_crash.groupby("hour").sum()
df_time_crash.reset_index(inplace = True)

st.markdown("Cruiosidad: Historicamente el horario con mayor cantidad de colisiones es a las 16Hs, esto se debe a que es el horario en el que comienza la salida del trabajo para mucha gente, esta franja se extiende hasta las 18Hs.")

# grafico con plotly
trace3 = px.bar(
    df_time_crash,
    x = "hour",
    y = "collision_count",
    color = "hour",   
)
# trace3.show()
st.plotly_chart(trace3) #grafico el barplot


###################################################################################################
####################################### kpi_zone_crash_perc #######################################
###################################################################################################

st.markdown("<h1 style='text-align: center;'>kpi_zone_crash_perc</h1>", unsafe_allow_html=True)

url4 = "http://vps-2671696-x.dattaweb.com/collision/zone_crash/"
response = requests.get(url4, timeout=0.5)
df_colisiones_zone = pd.DataFrame(response.json()["data"])

df_colisiones_zone.sort_values(by = ["borough", "year", "month"], ascending = False, inplace = True)
df_colisiones_zone = df_colisiones_zone[["borough", "collision_count"]]
grupo = df_colisiones_zone.groupby(["borough"]).sum()
grupo.reset_index(inplace = True)
grupo.sort_values("collision_count", inplace = True)
grupo = grupo[grupo["borough"] != "Unknown"] # me quedo solo con los barios que estan definidos

st.markdown("Cruiosidad: Historicamente el barrio de Nueva York con mayor cantidad de colisiones es Brooklyn, <explicar por que creemos que puede ser el barrio con mayor cantidad de colisiones>")

# grafico con plotly
trace4 = px.bar(
    grupo,
    x = "borough",
    y = "collision_count",
    color = "borough",   
)
# trace4.show()
st.plotly_chart(trace4) #grafico el barplot