import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Train the model
df = pd.read_csv("Hours_vs_SGPA.csv")
X = df[['Hours Study']]
y = df['Semester SGPA']
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("SGPA Predictor")
hours = st.number_input("Enter study hours", min_value=0.0, max_value=24.0, step=0.5)

if st.button("Predict SGPA"):
    prediction = model.predict([[hours]])[0]
    st.success(f"Predicted SGPA: {prediction:.2f}")
