import streamlit as st
import pandas as pd

# Function to load CSV files into dataframes
@st.cache_data
def load_data():
    trips = pd.read_csv('datasets/trips.csv')
    cars = pd.read_csv('datasets/cars.csv')
    cities = pd.read_csv('datasets/cities.csv')

    return trips, cars, cities

# Loading the data by calling the function
trips, cars, cities = load_data()

# Merge trips with cars (joining on car_id)
trips_merged = trips.merge(cars, left_on="car_id", right_on="id", how="left")

# Merge with cities for car's city (joining on city_id)
trips_merged = trips_merged.merge(cities, left_on="city_id", right_on="city_id", how="left")

# Dropping unnecessary id columns
trips_merged = trips_merged.drop(columns=["id_x", "car_id", "customer_id", "city_id", "id_y"])

