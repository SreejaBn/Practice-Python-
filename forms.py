import streamlit as st
import pandas as pd

st.title ("Streamlit form")

with st.form(key= "sample_form"):
    st.subheader("Text Input")
    name= st.text_input("Type here")

    st.subheader("Date and Time inputs")
    date= st.date_input("Date")
    time= st.time_input("Time")

    st.subheader("Selecters")
    choice= st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
    select= st.selectbox("Choose", ["One", "Two", "Three"])
    slider= st.select_slider("Select a range", ["1", "2", "3"])
    
    st.subheader("Checkbox")
    checkbox= st.checkbox("Here", key= "one")
    checkbox2= st.checkbox("Here", value= False, key= "two")

    st.form_submit_button()
