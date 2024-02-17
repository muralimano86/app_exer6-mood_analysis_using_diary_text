import streamlit as st
import plotly.express as px
from backend import diary_tone

filenames, positivity, negativity = diary_tone()

st.title("Diary Tone")
st.subheader("Positivity")
pos_fig = px.line(x=filenames, y=positivity, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_fig)

st.subheader("Negativity")
neg_fig = px.line(x=filenames, y=negativity, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_fig)