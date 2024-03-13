import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

col_names = ["col_1", "col_2", "col_3"]
data = pd.DataFrame(np.random.randint(30, size = (30,3)), columns = col_names)

# line chart
st.header("Line Chart")
st.line_chart(data)

# bar chart
st.header("Bar chart")
st.bar_chart(data)

# pie chart
st.header("Pie Chart")
animals = ["cat", "dog", "cow", "Lion"]
height = [15,25,35,45]
fig,ax = plt.subplots()
ax.pie(height, labels = animals)
st.pyplot(fig)

# Hist plot
st.header("Hist plot")
iris_data = load_iris()
data = pd.DataFrame(iris_data.data, columns = iris_data.feature_names)
fig = plt.figure()
sns.histplot(data = data, bins = 20)
st.pyplot(fig)

# Box plot
st.header("Box plot")
fig = plt.figure()
sns.boxplot(data = data)
st.pyplot(fig)

# scatter plot
st.header("Scatter plot")
fig = plt.figure()
sns.scatterplot(data = data)
st.pyplot(fig)



