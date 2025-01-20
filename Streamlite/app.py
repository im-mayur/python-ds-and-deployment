import streamlit as st
import numpy as np
import pandas as pd

## crete title

st.title("Hello Streamlit!")

## Display text
st.write("This is web app made with Streamlit")

df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

## Display the Dataframe
st.write("This is the Dataframe")
st.write(df)

##Create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)