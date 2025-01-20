import streamlit as st
import pandas as pd

st.title("widgets")

## input text
name=st.text_input("Enter your name:")

## slider
age=st.slide("Select your age:",0,100,25)
st.write(f"Your age is:{age}")

##dropdown box
options=['python','java','c++','js']
choice=st.selectbox("Choose your favourite language:",options)
st.write(f"you selected {choice}")

if name:
    st.write(f"Hello {name}")

##upload button
uploaded_file=st.file_uploader("Choose a csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)