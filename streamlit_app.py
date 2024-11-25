import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler

# Load dataset
data = pd.read_csv("C:/Users/MAHITHA/Downloads/Final_EV_Fleet_Dataset.csv")

# List of columns to be used in the dropdown
columns_to_display = [
    "Acceleration 0 - 100 km/h", 
    "Top Speed", 
    "Electric Range", 
    "Total Power", 
    "Total Torque", 
    "Wheelbase", 
    "Gross Vehicle Weight (GVWR)", 
    "Cargo Volume", 
    "Battery Capacity", 
    "Maintenance Cost", 
    "Battery Level", 
    "Range",
    "Make"
]

# Streamlit Sidebar for column selection
st.sidebar.header("Select columns for Visualizations")
x_axis = st.sidebar.selectbox("Select X-axis Parameter", options=["Select X"] + columns_to_display)
y_axis = st.sidebar.selectbox("Select Y-axis Parameter", options=["Select Y"] + columns_to_display)

# Ensure selected columns are numeric for plotting
if x_axis != "Select X" and y_axis != "Select Y":  # Make sure user selects an actual column
    # Clean the data: Drop rows with missing values for the selected columns
    data_clean = data.dropna(subset=[x_axis, y_axis])

    # Normalize data if necessary (example: Min-Max scaling for the selected columns)
    scaler = MinMaxScaler()
    data_clean[x_axis] = scaler.fit_transform(data_clean[[x_axis]])
    data_clean[y_axis] = scaler.fit_transform(data_clean[[y_axis]])

    # Create Bar Chart
    bar_fig = px.bar(data_clean, x=x_axis, y=y_axis, title=f"Bar Chart of {x_axis} vs {y_axis}", color="Make")

    # Create Histogram for selected X-axis column
    hist_fig = px.histogram(data_clean, x=x_axis, title=f"Histogram of {x_axis}")

    # Create Box Plot for selected Y-axis column
    box_fig = px.box(data_clean, y=y_axis, title=f"Box Plot of {y_axis}")

    # Create Pie Chart based on "Make" column
    pie_fig = px.pie(data, names='Make', title="Pie Chart of Vehicle Make")


    # Create Area Chart (for cumulative trend analysis)
    area_fig = px.area(data_clean, x=x_axis, y=y_axis, title=f"Area Chart of {x_axis} vs {y_axis}", color="Make")
    


    # Display the charts
    st.title("EV Fleet Analysis")

    # Display Bar Chart
    st.plotly_chart(bar_fig, use_container_width=True)

    # Display Histogram
    st.plotly_chart(hist_fig, use_container_width=True)

    # Display Box Plot
    st.plotly_chart(box_fig, use_container_width=True)

    # Display Pie Chart
    st.plotly_chart(pie_fig, use_container_width=True)
    

    # Display Area Chart
    st.plotly_chart(area_fig, use_container_width=True)

  

else:
    st.warning("Please select columns for both X and Y axes.")
