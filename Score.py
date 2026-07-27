import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = pd.read_csv("E:/Coding/ML Models/Hours_vs_SGPA.csv")
df = pd.DataFrame(data)

X = df[['Hours Study']]
y = df['Semester SGPA'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

hours = int(input("Enter the number of hours the student studied: "))
input_df = pd.DataFrame([[hours]], columns=['Hours Study'])
predicted_score = model.predict(input_df)
print(f"Predicted Exam Score: {predicted_score[0]:.2f}")
