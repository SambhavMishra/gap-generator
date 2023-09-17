import streamlit as st

# Create a checkbox to ask if the person studies in college
studying_in_college = st.checkbox("Do you study in college?")

# If the checkbox is checked, display a text input field for college name
college_name = ''
try:
    if studying_in_college:
        college_name = st.text_input("Which college do you study in?")
except:
    pass 
# Display the college name if provided
if college_name:
    st.write(f"You study in: {college_name}")
