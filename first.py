import pandas as pd
import streamlit as st
st.title('MY FIRST APP')
data=pd.read_csv("htp.csv")
st.dataframe(data)
