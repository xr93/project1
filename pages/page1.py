import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import plotly.express as px

df = pd.read_csv("analysis.csv")
st.sidebar.title("Charts")
# Multi-tab setup
tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Covid Cases by Age Group", 
        "Covid Cases by Gender and Age Group", 
        "Total Intubated Patients", 
        "ICU Admission Among Diseases", 
        "Total Deceased Patients in Other Diseases"
    ])
with tab1:
       # Define age bins and labels
        bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        labels = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-100"]
        # Create AGE_GROUP column
        df["AGE_GROUP"] = pd.cut(df["AGE"], bins=bins, labels=labels, right=False)

        # Count cases by age group
        age_group_counts = df["AGE_GROUP"].value_counts().sort_index().reset_index()
        age_group_counts.columns = ['Age Group', 'Number of Cases']

        # Create the bar chart
        fig = px.bar(
            age_group_counts, 
            x="Age Group", 
            y="Number of Cases", 
            title="Number of Cases by Age Group"
        )

        # Display the chart
        st.plotly_chart(fig)
        fig1 = px.histogram(df, x="AGE", nbins=10, title="Distribution of Cases by Age Group")
        # fig.show()
        st.plotly_chart(fig1)

with tab2:
  
        # Group data by AGE_GROUP and SEX to calculate the distribution
        distribution = df.groupby(["AGE_GROUP", "SEX"]).size().reset_index(name="Number of Cases")
        
        # Plot the distribution using a histogram
        fig2 = px.histogram(
            distribution,
            x="AGE_GROUP",
            y="Number of Cases",
            color="SEX",
            barmode="group",  # Grouped bars for gender
            title="Distribution of COVID-19 Cases by Gender and Age Group",
            labels={"AGE_GROUP": "Age Group", "Number of Cases": "Number of Cases", "SEX": "Gender"},
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        
        # Customize the layout
        fig2.update_layout(
            xaxis_title="Age Group",
            yaxis_title="Number of Cases",
            title_font_size=16,
            xaxis_tickangle=45,
            template="plotly_white"
        )
        
        # Display the plot in Streamlit
        st.plotly_chart(fig2)

with tab3:
        intubation_distribution = df["INTUBATED"].value_counts().reset_index()
        intubation_distribution.columns = ["INTUBATED", "Number of Cases"]

        # Plot the bar chart
        fig = px.bar(
            intubation_distribution,
            x="INTUBATED",
            y="Number of Cases",
            title="Distribution of Intubation Cases",
            labels={"INTUBATED": "Intubation Status", "Number of Cases": "Number of Cases"},
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        # Customize the layout
        fig.update_layout(
            xaxis_title="Intubation Status",
            yaxis_title="Number of Cases",
            title_font_size=16,
            template="plotly_white"
        )

        st.plotly_chart(fig)

with tab4:
        # List of diseases
        diseases = ["DIABETES", "COPD", "ASTHMA", "INMUSUPR", "HYPERTENSION", "CARDIOVASCULAR", "OBESITY", "CHRONIC_KIDNEY", "TOBACCO"]
        icu_patients = df[df['ICU'] == 'YES']

        data_list = []

        for disease in diseases:
            count = icu_patients[icu_patients[disease] == 'YES'][disease].count()
            data_list.append({'Disease': disease, 'Count': count})

        icu_counts = pd.DataFrame(data_list)

        fig = px.line(
            icu_counts, 
            x="Disease", 
            y="Count", 
            title="ICU Patients based on the Diseases",
            labels={"Count": "Number of ICU Patients", "Disease": "Diseases"},
            text="Count",  
            markers=True
        )

        # Show the interactive plot
        # fig.show()
        st.plotly_chart(fig)

with tab5:
        deceased_patients = df[~df['DATE_OF_DEATH'].isna()]

        diseases = ['PNEUMONIA', 'DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 
                'HYPERTENSION', 'CARDIOVASCULAR', 'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO']

        data_list = []

        for disease in diseases:
            count = deceased_patients[deceased_patients[disease] == 'YES'][disease].count()
            data_list.append({'Disease': disease, 'Count': count})

        disease_counts = pd.DataFrame(data_list)

        fig = px.bar(
            disease_counts, 
            x="Count", 
            y="Disease", 
            title="Common Diseases in Deceased Patients",
            labels={"Count": "Number of Deceased Patients", "Disease": "Diseases"},
            text="Count",  
            color="Count",  
        )
        st.plotly_chart(fig)