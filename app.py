import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Car Sales Dashboard — Vehicles US")

car_data = pd.read_csv("vehicles.csv")

st.write("Amostra dos dados:")
st.dataframe(car_data.head())

hist_button = st.button("Criar histograma (odometer)")

if hist_button:
    st.write("Histograma da coluna odometer")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.button("Criar gráfico de dispersão (odometer vs price)")

if scatter_button:
    st.write("Dispersão: odometer vs price")
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
