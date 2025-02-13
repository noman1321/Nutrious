import streamlit as st
from health_report import health_report_page
from food_analysis import food_analysis_page
import random

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Nutritious App", layout="wide")

# Interactive Title and Quotes
st.title("🍎 Nutritious App 🥗")
st.write("Your personal health and nutrition assistant!")

# List of random quotes
quotes = [
    "Healthy eating is a way of life, so it’s important to establish routines that are simple, realistically, and ultimately livable.",
    "Let food be thy medicine and medicine be thy food.",
    "The food you eat can be either the safest and most powerful form of medicine or the slowest form of poison.",
    "Take care of your body. It’s the only place you have to live.",
    "Eating healthy food fills your body with energy and nutrients. Imagine your cells smiling back at you and saying: Thank you!",
]

# Display a random quote
random_quote = random.choice(quotes)
st.write(f"**Quote of the Day:**\n\n{random_quote}")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Health Report Summary", "Food Analysis"])

# Load the appropriate page
if page == "Health Report Summary":
    health_report_page()
elif page == "Food Analysis":
    food_analysis_page()
    
    
    
# import streamlit as st
# from health_report import health_report_page
# from food_analysis import food_analysis_page

# # Set page configuration (must be the first Streamlit command)
# st.set_page_config(page_title="Nutritious App", layout="wide")

# # Sidebar for navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Health Report Summary", "Food Analysis"])

# # Load the appropriate page
# if page == "Health Report Summary":
#     health_report_page()
# elif page == "Food Analysis":
#     food_analysis_page()