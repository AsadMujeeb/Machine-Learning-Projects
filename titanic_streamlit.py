
import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestRegressor  # Corrected import
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Titanic Survival Prediction App")
    st.text("In this project we will work on Titanic data")

with data_sets:
    st.header("Titanic Datasets")
    st.text("In this project we will work on Titanic data")
    # import dataset
    df = sns.load_dataset("titanic")
    df = df.dropna()
    st.write(df.head(10))
    st.subheader("Bar Graph for Sex")
    st.bar_chart(df["sex"].value_counts())
    # other plots
    st.subheader("Bar Graph for Class")
    st.bar_chart(df["class"].value_counts())
    # barplot
    st.bar_chart(df["age"].sample(10))

with features:
    st.header("Titanic Features")
    st.text("In this project we will work on Titanic data")
    st.markdown('1. **Feature** This is 1st app features for Titanic Prediction')
    st.markdown('2. **Feature** This is 2nd app features for Titanic Prediction')
    st.markdown('3. **Feature** This is 3rd app features for Titanic Prediction')
with model_training:
    st.header("Titanic Model Training")
    st.text("In this project we will work on Titanic data")
    # making columns
    input_col, display = st.columns(2)# Renamed to avoid naming conflict
    

    # First column for user inputs
with input_col:
    n_estimators = st.selectbox("How many trees should be there ", options=(50, 100, 150, 200, None))
    max_depth = st.slider("How many people did you know", min_value=10,max_value=100, value=20, step=5)
# n_estimators = st.selectbox("How many trees should be there ", options=(50, 100, 150, 200, None))
input_col.write(df.columns)
input_feature = st.text_input("Which feature should we use ")


# Machine Learning Model
model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)  # Corrected model type to Regressor
if n_estimators == "None":
    model = RandomForestRegressor(max_depth = max_depth )
else:
    model = RandomForestRegressor(max_depth = max_depth, n_estimators = n_estimators)
# Define X and y
X = df[[input_feature]]
y = df[["fare"]]

# Fit our model
model.fit(X, y)
pred = model.predict(X)  # Corrected prediction variable

# display metrics
display.subheader("Mean absolute error is : ")
display.write(mean_absolute_error(y, pred))
display.subheader("Mean squared error is : ")
display.write(mean_squared_error(y, pred))
display.subheader("R2 score is : ")
display.write(r2_score(y, pred))







