import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Vehicle Sales Dashboard")

st.markdown("""  
This interactive dashboard allows you to explore vehicle listing data.
Use the controls below to generate visualizations.
""")

car_data = pd.read_csv("vehicles.csv")

st.subheader("Dataset Preview")

st.write(
    f"The dataset contains {car_data.shape[0]} rows and {car_data.shape[1]} columns.")
st.dataframe(car_data.head(8))

hist_button = st.button("Show Mileage Distribution")

if hist_button:
    st.write("This histogram shows the distribution of vehicle mileage.")
    fig_hist = px.histogram(car_data, x="odometer",
                            title="Mileage Distribution")
    st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.button("Show Price vs Mileage Relationship")

if scatter_button:
    st.write(
        "This scatter plot shows the relationship between vehicle mileage and price.")
    fig_scatter = px.scatter(car_data, x="odometer",
                             y="price", title='Price vs Mileage')
    st.plotly_chart(fig_scatter, use_container_width=True)
