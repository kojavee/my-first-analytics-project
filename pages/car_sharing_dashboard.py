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

# Transform the pickup time and dropoff time columns 
trips_merged['pickup_date'] = pd.to_datetime(trips_merged['pickup_time']).dt.date
trips_merged['pickup_date'] = pd.to_datetime(trips_merged['pickup_time']).dt.date

# Creating a sidebar with filtering function
car_brands = trips_merged["brand"].dropna().unique() 
selected_brands = st.sidebar.multiselect("Select the Car Brand", car_brands)

# Apply filter if any brand is selected
if selected_brands:
    trips_merged = trips_merged[trips_merged["brand"].isin(selected_brands)]

# Providing business metrics
# Total number of trips 
total_trips = len(trips_merged)
# Car model with the most revenue
top_car = trips_merged.groupby("model")["revenue"].sum().idxmax()
# Total distance
total_distance = trips_merged["distance"].sum()

# Display metrics in columns
col1, col2, col3 = st.columns(3)
with col1:
 st.metric(label="Total Trips", value=total_trips)
with col2:
 st.metric(label="Top Car Model by Revenue", value=top_car)
with col3:
 st.metric(label="Total Distance (km)", value=f"{total_distance:,.2f}")

# Preview the contents of your dataframe
st.subheader("Preview of the complete car sharing dataframe")
st.write(trips_merged.head())