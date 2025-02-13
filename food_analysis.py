import streamlit as st
import google.generativeai as genai
from PIL import Image

# Set up Google Gemini
genai.configure(api_key=st.secrets["GOOGLE_GEMINI_API_KEY"])  # Use secrets.toml

def food_analysis_page():
    # Title
    st.title("Food Analysis")
    st.write("Upload a photo of your food, and we'll analyze if it's healthy or not!")

    # File uploader
    uploaded_image = st.file_uploader("Upload Food Photo", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Open the image
        image = Image.open(uploaded_image)

        # Display the image
        st.image(image, caption="Uploaded Food Photo", use_column_width=True)

        # Use Gemini to analyze the food
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = "Analyze this food photo and tell me if it's healthy or not. If it's not healthy, suggest a healthier alternative."
        response = model.generate_content([prompt, image])

        # Store the result in session state
        st.session_state.food_analysis_result = response.text

    # Display the result if it exists in session state
    if "food_analysis_result" in st.session_state:
        st.subheader("Food Analysis Result")
        st.write(st.session_state.food_analysis_result)
        
        
        
        
#         import streamlit as st
# import google.generativeai as genai
# from PIL import Image

# # Set up Google Gemini
# genai.configure(api_key=st.secrets["GOOGLE_GEMINI_API_KEY"])

# def food_analysis_page():
#     # Title
#     st.title("Food Analysis")
#     st.write("Upload a photo of your food, and we'll analyze if it's healthy or not!")

#     # File uploader
#     uploaded_image = st.file_uploader("Upload Food Photo", type=["jpg", "jpeg", "png"])

#     if uploaded_image is not None:
#         # Open the image
#         image = Image.open(uploaded_image)

#         # Display the image
#         st.image(image, caption="Uploaded Food Photo", use_column_width=True)

#         # Use Gemini to analyze the food
#         model = genai.GenerativeModel('gemini-pro-vision')
#         prompt = "Analyze this food photo and tell me if it's healthy or not. If it's not healthy, suggest a healthier alternative."
#         response = model.generate_content([prompt, image])

#         # Display the analysis result
#         st.subheader("Food Analysis Result")
#         st.write(response.text)