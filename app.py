import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Vehicle Sales Dashboard")

st.markdown("""  
This interactive dashboard allows you to explore vehicle listing data.
Use the controls below to generate visualizations.
""")

car_data = pd.read_csv("vehicles.csv")

st.write("Dataset Overview:")
st.dataframe(car_data.head())

hist_button = st.button("Show Mileage Distribution")

if hist_button:
    st.write("Distribution of vehicle mileage (odometer readings)")
    fig_hist = px.histogram(car_data, x="odometer",
                            title="Mileage Distribution")
    st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.button("Show Price vs Mileage Relationship")

if scatter_button:
    st.write("Relationship between vehicle mileage and price.")
    fig_scatter = px.scatter(car_data, x="odometer",
                             y="price", title='Price vs Mileage')
    st.plotly_chart(fig_scatter, use_container_width=True)
