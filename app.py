import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Deportivo", layout="centered")

st.title("Panel de rendimiento: Equipo Datos Santoto")
st.write("Estad{isticas clave de los jugadores en el semestre actual")

datos= {
    "Jugador": ["Sebastian","Juan","Manuel","Cristian"],
    "Goles": [18,14,20,1],
    "Asistencias": [5,7,10,3]
}

df = pd.DataFrame(datos)

col1,col2,col3,col4 = st.columns(4)
#""" st.write(f"Goles totales: {df["Goles"].sum()}")
#st.write(f"Asistencias totales: {df["Asistencias"].sum()}")
#st.write(f"Goleador del Equipo: {df.loc[df["Goles"].idxmax(),"Jugador"]}") """

col1.metric("Goles totales", df["Goles"].sum(),delta="+3 vs partido anterior")
col2.metric("Asistencias totales", df["Asistencias"].sum())
col3.metric("Goleador del equipo", df.loc[df["Goles"].idxmax(), "Jugador"])
col4.metric("Posición de liga del equipo", value="3er Lugar", delta="-1 puesto")

st.subheader("Estadisticas al detalle")
st.dataframe(df)

st.subheader("Comparativa de Rendimiento")
st.bar_chart(df.set_index("Jugador"))
