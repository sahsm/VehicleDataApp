# Vehicle Sales Data Dashboard

## Project Overview

This project is an interactive web application built with **Streamlit** to explore vehicle listing data through simple and intuitive visualizations.

The dashboard allows users to inspect the dataset and analyze relationships between vehicle mileage and price.

The project demonstrates the development and deployment of an interactive data application using Python, Pandas, Plotly, and Streamlit.

## Dashboard Features

Users can:

- Preview a sample of the vehicle listings dataset
- View key dataset metrics including total listings, average price, and average mileage
- Generate an interactive histogram of vehicle mileage
- Explore the relationship between vehicle mileage and price using a scatter plot

## Dataset

The dataset contains vehicle listings with information such as price, mileage, model year, condition, fuel type, transmission, and other vehicle characteristics.

The application uses the dataset to provide interactive exploratory visualizations.

## Technologies Used

- Python
- Pandas
- Plotly
- Streamlit
- Git & GitHub
- Render

## Project Structure

```text
VehicleDataApp/
│
├── .streamlit/
│   └── config.toml
│
├── notebooks/
│   └── EDA.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── vehicles.csv
```

## Running the Project Locally

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Then run the Streamlit application:

```bash
streamlit run app.py
```

## Live Application

The dashboard is deployed on Render and can be accessed here:

https://vehicledataapp.onrender.com

## Author

**Sara Menger**

Junior Data Scientist  
Python | SQL | Machine Learning | Data Analytics
