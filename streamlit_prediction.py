import streamlit as st
import pickle
import os
import pandas as pd

# Load the model from the pickle file
model_path = os.path.join('users', 'models', 'evmodel.pkl')  # Path to the pickle file
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title('Electric Range Prediction')

# Input fields
make = st.selectbox('Select the Make of the vehicle', ['BMW', 'Polestar', 'Tesla1', 'Tesla2', 'Volkswagen'])
battery_level = st.number_input('Enter Battery Level', min_value=0, max_value=100, step=1)
top_speed = st.number_input('Enter Top Speed (in km/h)', min_value=0, step=1)
total_power = st.number_input('Enter Total Power (in kW)', min_value=0, step=1)
total_torque = st.number_input('Enter Total Torque (in Nm)', min_value=0, step=1)
gvwr = st.number_input('Enter Gross Vehicle Weight (GVWR in kg)', min_value=0, step=1)
acceleration = st.number_input('Enter Acceleration (0-100 km/h in seconds)', min_value=0.0, step=0.1)
battery_capacity = st.number_input('Enter Battery Capacity (in kWh)', min_value=0, step=1)
range = st.number_input('Enter Range (in km)', min_value=0, step=1)

# Function to one-hot encode the selected make
def encode_make(make):
    # One-hot encoding based on the dataset columns
    encoding = {'BMW': [1, 0, 0, 0, 0],
                'Polestar': [0, 1, 0, 0, 0],
                'Tesla1': [0, 0, 1, 0, 0],
                'Tesla2': [0, 0, 0, 1, 0],
                'Volkswagen': [0, 0, 0, 0, 1]}
    
    return encoding.get(make, [0, 0, 0, 0, 0])  # Default to all zeros if no valid make is selected

# Prepare the input for prediction
encoded_make = encode_make(make)

# Combine the input features with the encoded make
prediction_input = [
    battery_level, 
    top_speed, 
    total_power, 
    total_torque, 
    gvwr, 
    acceleration, 
    battery_capacity, 
    range
] + encoded_make

# Column order that the model expects (13 features in total)
columns_order = ['Battery Level', 'Top Speed', 'Total Power', 'Total Torque', 'Gross Vehicle Weight (GVWR)', 
                 'Acceleration 0 - 100 km/h', 'Battery Capacity', 'Range', 'Make_BMW', 'Make_Polestar', 
                 'Make_Tesla1', 'Make_Tesla2', 'Make_Volkswagen']

# Make sure the prediction input is in the correct shape (1 row, 13 features)
prediction_input_df = pd.DataFrame([prediction_input], columns=columns_order)

# Prediction on button click
if st.button('Predict'):
    if make and battery_level is not None:
        # Make prediction
        predicted_range = model.predict(prediction_input_df)

        # Display result
        st.write(f'The estimated electric range is: {predicted_range[0]}')
    else:
        st.warning('Please enter all the required fields to make a prediction.')
