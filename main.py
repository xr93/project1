import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import plotly.express as px

# Set the title of the main page
st.title("Welcome to the Covid-19 Data App")

# Add a subtitle
st.subheader("Explore Covid-19 Data with Ease")

# Add some markdown content
st.markdown("""
This is a simple data visualization app using Streamlit.

### Features:
- *Interactive visualizations* for Covid-19 data.
- *Easy-to-use interface* for exploring trends.
- *Real-time updates* with the latest data.

Enjoy exploring and stay informed!
""")

# Add an image (replace 'image_url' with an actual URL or local file path)
#st.image("https://via.placeholder.com/800x400.png?text=Covid-19+Data+Visualization", caption="Covid-19 Data Insights", use_column_width=True)

# Add an interactive button
if st.button("Click to Learn More"):
    st.write("Stay tuned for more features coming soon!")



st.title("Overview")

# Load dataset
df = pd.read_csv("dataset.csv")

st.dataframe(df)

pd.set_option('display.max_columns', 100)

sns.set()

df = pd.read_csv("analysis.csv")

# Define age bins and labels
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
labels = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-100"]

# Categorize ages into bins (right=False ensures correct binning)
df["AGE_GROUP"] = pd.cut(df["AGE"], bins=bins, labels=labels, right=False)

# Count the number of cases in each age group
age_group_counts = df["AGE_GROUP"].value_counts().sort_index().to_frame(name="Number of Cases")

      
