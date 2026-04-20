import streamlit as st
import google.generativeai as genai

# UI Configuration
st.set_page_config(page_title="AI Student Advisor", layout="centered")

# Styling to match your preference (Cream accents)
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { background-color: #FFFDD0; color: black; font-weight: bold; width: 100%; border-radius: 8px; }
    .stTextInput>div>div>input { color: #FFFDD0; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 Student Performance Predictor")
st.write("Built for PromptWars 2026 Submission")

# Sidebar
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
st.sidebar.markdown("---")
study_hours = st.sidebar.slider("Daily Study Hours", 0, 15, 6)
attendance = st.sidebar.slider("Attendance %", 0, 100, 80)
prev_gpa = st.sidebar.number_input("Previous Semester GPA", 0.0, 10.0, 7.5)

# Main Logic
if st.button("Generate AI Performance Report"):
    if not api_key:
        st.error("Missing API Key! Please paste it in the sidebar.")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # Using the most stable 2026 production model
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            As an AI Academic Advisor, analyze this B.Tech student:
            - Study Hours: {study_hours}/day
            - Attendance: {attendance}%
            - Previous GPA: {prev_gpa}
            
            Provide a semester prediction and 3 technical study tips.
            """
            
            with st.spinner("AI analyzing metrics..."):
                response = model.generate_content(prompt)
                st.success("Analysis Complete!")
                st.markdown("### Advisor's Feedback")
                st.write(response.text)
                
        except Exception as e:
            # If the model name is the issue, this helps us see the exact error
            st.error(f"System Error: {str(e)}")
            st.info("Try getting a fresh API key from 'Create API key in new project' in AI Studio.")

st.markdown("---")
st.caption("Kazi Mustafijur Rahaman | CSE AIML | PromptWars 2026")