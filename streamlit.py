#Import the Library
import streamlit as st
import time as t

#Image
st.image("IK.jpeg")

# Title
st.title("Muslim Leader ")

#Header
st.header("Machine Learning")

#Sub Header
st.subheader("Linear Regression")

#Information
st.info("Information of the user")

#warning
st.warning("Improve your code")

#Error
st.error("Invalid Input")

#success
st.success("Your code is working")

#text
st.write("My name is Asad Mujeeb")
st.write(range(50))

#markdown
st.markdown("# Data Analyst")
st.markdown("## Data Analyst")
st.markdown(':moon:')

#caption
st.caption("Enter your caption")

# to display mathematical function
st.latex(r'''  ax^2 +by +c = 0''')

#widget

#checkbox
st.checkbox("Login")

#button
st.button("Hit Me !")

#Radio button
st.radio("Choose your Gender", ["Male", "Female", "Other"])

#selectBox
st.selectbox("Enter your course", ["AI", "Data science", "ML", "Database"])

# multi Select
st.multiselect("choose your interest", ["IT", "CS", "Telecom", "CA", "IMS"])

#select slider
st.select_slider("Rate the program", ["Good", "Bad", "Average", "Excellent"])

#slider
st.slider("Enter your age : ", 1, 30)

# number input
st.number_input("select the lucky number : ", 0,100)

#text input
st.text_input("Enter your email")

#date input
st.date_input("Graduation Year")

#time input
st.time_input("Be punctual")

#text area
st.text_area("feed us comment")

#file upload
st.file_uploader("choose your resume/folder")

#color picker
st.color_picker("Theme")

#progress
st.progress(75)

#spinner
with st.spinner("Loading") :
    t.sleep(5)

#baloons
st.balloons()    

#sidebar
st.sidebar.image("free palestine.jpeg")
st.sidebar.text_input("Enter email")
st.sidebar.text_input("Enter key")
st.sidebar.button("successfully")
st.sidebar.radio("Having Expertise", ["Beginner", "Internediate", "Pro-level"])


#Data visualization
import numpy as np
import pandas as pd
#bar chart
st.title("Bar chart")
data = pd.DataFrame(np.random.rand(50,2), columns = ["x","y"])
st.bar_chart(data)

#line chart
st.title("Line chart")
st.line_chart(data)