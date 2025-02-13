import streamlit as st
import google.generativeai as genai

# Set up Google Gemini
genai.configure(api_key=st.secrets["GOOGLE_GEMINI_API_KEY"])  # Use secrets.toml

def health_report_page():
    # Title
    st.title("Health Report Summary")
    st.write("Upload your health report (PDF or text file), and we'll summarize it for you!")

    # File uploader
    uploaded_file = st.file_uploader("Upload Health Report", type=["pdf", "txt"])

    if uploaded_file is not None:
        # Read the file content
        if uploaded_file.type == "application/pdf":
            import PyPDF2
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            file_content = ""
            for page in pdf_reader.pages:
                file_content += page.extract_text()
        else:
            file_content = uploaded_file.read().decode("utf-8")

        # Use Gemini to summarize the report
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Summarize this health report in simple language and provide health tips based on the data:\n\n{file_content}"
        response = model.generate_content(prompt)

        # Store the result in session state
        st.session_state.health_report_result = response.text

    # Display the result if it exists in session state
    if "health_report_result" in st.session_state:
        st.subheader("Summary of Your Health Report")
        st.write(st.session_state.health_report_result)
        
        
# import streamlit as st
# import google.generativeai as genai

# # Set up Google Gemini
# genai.configure(api_key=st.secrets["GOOGLE_GEMINI_API_KEY"])

# def health_report_page():
#     # Title
#     st.title("Health Report Summary")
#     st.write("Upload your health report (PDF or text file), and we'll summarize it for you!")

#     # File uploader
#     uploaded_file = st.file_uploader("Upload Health Report", type=["pdf", "txt"])

#     if uploaded_file is not None:
#         # Read the file content
#         if uploaded_file.type == "application/pdf":
#             import PyPDF2
#             pdf_reader = PyPDF2.PdfReader(uploaded_file)
#             file_content = ""
#             for page in pdf_reader.pages:
#                 file_content += page.extract_text()
#         else:
#             file_content = uploaded_file.read().decode("utf-8")

#         # Use Gemini to summarize the report
#         model = genai.GenerativeModel('gemini-pro')
#         prompt = f"Summarize this health report in simple language and provide health tips based on the data:\n\n{file_content}"
#         response = model.generate_content(prompt)

#         # Display the summary and tips
#         st.subheader("Summary of Your Health Report")
#         st.write(response.text)