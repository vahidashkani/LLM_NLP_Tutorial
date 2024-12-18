import streamlit as st

st.title("StreamLit")
input_text=st.text_input("What question you have in mind?")

if input_text:
    st.write(input_text.upper())
