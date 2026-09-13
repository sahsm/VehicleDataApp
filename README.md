# Vehicle Sales Data Dashboard

## Project Overview

This project is an interactive web application built with **Streamlit** to explore vehicle listing data through intuitive and interactive visualizations.

The dashboard allows users to examine vehicle listings, explore key dataset metrics, and analyze relationships between vehicle mileage and price.

The project demonstrates the development and deployment of an end-to-end interactive data application using Python, Pandas, Plotly, Streamlit, GitHub, and Render.

---

## Project Objective

The objective of this project is to transform raw vehicle listing data into an accessible interactive dashboard that allows users to quickly explore vehicle characteristics and identify patterns in pricing and mileage.

---

## Dashboard Features

Users can:

- Preview a sample of the vehicle listings dataset
- View key dataset metrics, including total listings, average price, and average mileage
- Generate an interactive histogram of vehicle mileage
- Explore the relationship between vehicle mileage and price using an interactive scatter plot

---

## Dataset

The dataset contains vehicle listings with information such as:

- Price
- Mileage
- Model year
- Vehicle condition
- Fuel type
- Transmission
- Other vehicle characteristics

The application uses these variables to provide interactive exploratory visualizations and make the dataset easier to understand.

---

## Methodology

The project followed a simple data application development workflow:

1. Explored the vehicle listing dataset using Pandas
2. Performed exploratory data analysis in Jupyter Notebook
3. Identified relevant metrics and relationships for visualization
4. Developed interactive visualizations using Plotly
5. Built the web application interface using Streamlit
6. Managed the project using Git and GitHub
7. Deployed the completed application on Render

---

## Results

The final result is a deployed interactive dashboard that allows users to explore vehicle listing data without directly interacting with Python code.

The application provides a simple interface for examining dataset characteristics, vehicle mileage distributions, and the relationship between mileage and vehicle price.

---

## Technologies Used

- Python
- Pandas
- Plotly
- Streamlit
- Jupyter Notebook
- Git & GitHub
- Render

---

## What I Learned

This project strengthened my experience with:

- Building interactive data applications with Streamlit
- Creating interactive data visualizations with Plotly
- Transforming exploratory analysis into a user-facing application
- Structuring a Python project for deployment
- Managing dependencies using `requirements.txt`
- Using Git and GitHub for version control and project organization
- Deploying and maintaining a web application using Render

---

## Future Improvements

Potential improvements include:

- Adding additional filters for vehicle characteristics such as model year, condition, fuel type, and transmission
- Expanding the dashboard with additional pricing and vehicle-market visualizations
- Adding more detailed summary statistics
- Improving user controls for customized data exploration
- Expanding the exploratory analysis to identify additional relationships between vehicle characteristics and price

---

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

---

## Running the Project Locally

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Live Application

The dashboard is deployed on Render and can be accessed here:

https://vehicledataapp.onrender.com

---

## Author

**Sara Menger**

Data Scientist  
Python • SQL • Machine Learning • Data Analytics
 
LinkedIn: https://linkedin.com/in/saramenger
