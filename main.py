import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import plotly.express as px

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

st.header('Dashboard Covid 19 Cases in Mexico')
st.selectbox("Select chart to view",['Covid Cases by Age Group', 'Covid Cases by Gender and Age Group','Total Intubated Patients', 'ICU Admission Among Diseases','Total Deceased Patients in Other Diseases']) #select one box
if st.button("Click Here to Proceed"):
    if st.selectbox == 'Covid Cases by Age Group':
        st.markdown("Number of COVID-19 Cases by Age Group")
      
    elif st.selectbox == 'Covid Cases by Gender and Age Group':
        st.markdown("Covid Cases by Gender and Age Group")
      
