import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Vehicle Sales Dashboard",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Vehicle Sales Dashboard")

st.markdown(
    """
    Explore vehicle listing data through interactive visualizations.

    Use the options below to analyze mileage distribution
    and the relationship between mileage and vehicle price.
    """
)

car_data = pd.read_csv("vehicles.csv")

st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Listings", f"{car_data.shape[0]:,}")
col2.metric("Average Price", f"${car_data['price'].mean():,.0f}")
col3.metric("Average Mileage", f"{car_data['odometer'].mean():,.0f}")

with st.expander("View Dataset Sample"):
    st.dataframe(car_data.head(10), use_container_width=True)

st.divider()

st.subheader("Mileage Distribution")

fig_hist = px.histogram(
    car_data,
    x="odometer",
    nbins=50,
    title="Distribution of Vehicle Mileage",
    labels={"odometer": "Mileage"}
)

st.plotly_chart(fig_hist, use_container_width=True)

st.markdown(
    """
    This visualization shows how vehicle mileage is distributed
    across the listings in the dataset.
    """
)

st.divider()

st.subheader("Price vs. Mileage")

fig_scatter = px.scatter(
    car_data,
    x="odometer",
    y="price",
    opacity=0.5,
    title="Relationship Between Vehicle Price and Mileage",
    labels={
        "odometer": "Mileage",
        "price": "Price"
    }
)

st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown(
    """
    This chart helps explore whether vehicles with higher mileage
    tend to have lower listing prices.
    """
)
