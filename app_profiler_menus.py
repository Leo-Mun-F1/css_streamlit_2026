import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# Dummy STEM data
data_science_data = pd.DataFrame({ "Method":["Regression Analysis","Cluster Analysis",
"Time Series Analysis" ,"Factor Analysis","Sentiment Analysis"], 
"Descriptins":["Statistical method to model relationships between variables",
"Groups similar data points into clusters" ,
"Analyzes data over time to detect trends" ,
"Reduces data complexity by identifying underlying factors",
"Analyzes text data to determine sentiment"], 
 "Applications":["Forecasting, Optimization" ,
"Customer Segmentation, Pattern Discovery" ,
"Forecasting, Anomaly Detection" ,
"Dimensionality reduction, Pattern discovery" ,
"Customer feedback, Opinion mining"]
    
})

computer_data = pd.DataFrame({
    "PC Model": ["Alienware Aurora R15", "Corsair One i500", "Alienware Area-51","Dell Tower Plus", "Acer Predator Orion 5000"],
    "Geekbench 6 (multi-core)": [22494 , 21560, 21786, 19181, 16534],
    "1080p Frame Rate (GTA V)":[186, 186, 185, 182, 169]
    
})

cars_data = pd.DataFrame({
    "Car Model":["Rimac Nevera R", "Hennessey Venom F5", "Lotus Evija", "Bugatti Chiron Super Sport 300+", "SSC Tuatara", "Koenigsegg Jesko", "Koenigsegg Regera", "Bugatti Veyron Super Sport", "Koenigsegg One:1", "McLaren Speedtail"],
    "Horsepower":[2079, 1817, 2012, 1578, 1750, 1578, 1479, 1183, 1341, 1050],
    "Top Speed":["412 km/h (256 mph)", "484 km/h (301 mph)", "320 km/h (200 mph)", "440 km/h (273 mph)", "443 km/h (275 mph)", "418 km/h (260 mph)", "403 km/h (250 mph)", "431 km/h (268 mph)", "440 km/h (273 mph)", "403 km/h (250 mph)"]
})

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Mr ML Munyai"
    field = "Data Science"
    institution = "University of Venda"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    
    st.image(
    "https://i.pinimg.com/736x/f9/b1/81/f9b18101f25798c593ef6beca8e20f5f.jpg",
    caption="Green Rain"
)

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Top 5 Data Science Methods", "Top 5 Data Analysis PC", "Top 5 Sports Cars"]
    )

    if data_option == "Top 5 Data Science Methods":
        st.write("### Top 5 Data Science Methods")
        st.dataframe(data_science_data)
        # Add widget to filter by Energy levels
     

    elif data_option == "Top 5 Data Analysis PC":
        st.write("### Top 5 Data Analysis PC")
        st.dataframe(computer_data)
        # Add widget to filter by Brightness
        computer_filter = st.slider("Filter by Geekbench 6 (multi-core)", 16000, 22500, (16000, 22500))
        filtered_computer = computer_data[
            computer_data["Geekbench 6 (multi-core)"].between(computer_filter[0], computer_filter[1])
        ]
        st.write(f"Filtered Results for Brightness Range {computer_filter}:")
        st.dataframe(filtered_computer)

    elif data_option == "Top 10 Sports Cars":
        st.write("### Top 10 Sports Cars")
        st.dataframe(cars_data)
        # Add widgets to filter by temperature and humidity
        
        Horsepower_filter = st.slider("Filter by Horsepower", 1000, 3000, (1000, 3000))
        filtered_cars = cars_data[
            cars_data["Horsepower"].between(Horsepower_filter[0], Horsepower_filter[1])
        ]
        st.write(f"Filtered Results for Horsepower {Horsepower_filter}:")
        st.dataframe(filtered_cars)
        
        

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "jane.doe@example.com"

    st.write(f"You can reach me at {email}.")
























