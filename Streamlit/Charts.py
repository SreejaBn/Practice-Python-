import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st. title("Charts")

chart_data= pd.DataFrame(
    np.random.randn(20, 3),
    columns= ['A', 'B', 'C']
)

st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)

st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Scatter Chart")
st.scatter_chart(chart_data)

st.subheader("Map")
map_data= pd.DataFrame(
    np.random.randn(40,2)/[25,25] + [28.7, 77.1],
    columns= ['latitude', 'longitude']
)
st.map(map_data, color="#A1C423", size=20)

st.subheader("Myplotlib Chart")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label= 'A')
ax.plot(chart_data['B'], label= 'B')
ax.plot(chart_data['C'], label= 'C')
ax.set_title("Pylot line Chart")
ax.legend()
st.pyplot(fig)
