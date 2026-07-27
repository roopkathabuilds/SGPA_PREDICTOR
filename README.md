# 🎓 SGPA Predictor

> A Machine Learning-powered web application that predicts a student's **Semester Grade Point Average (SGPA)** based on study hours using **Linear Regression**. Built with **Python, Scikit-learn, Pandas, NumPy, and Streamlit**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📌 Overview

The **SGPA Predictor** is a regression-based machine learning application that estimates a student's expected SGPA from the number of study hours. The project demonstrates the complete machine learning workflow—from data preprocessing and model training to deployment using **Streamlit**.

This project is intended for educational purposes and showcases how predictive analytics can be applied in academic performance estimation.

---

## ✨ Features

- 📊 Predicts SGPA based on study hours
- 🤖 Linear Regression model using Scikit-learn
- 🧹 Data preprocessing with Pandas and NumPy
- 📈 Model evaluation with approximately **81% accuracy**
- 🌐 Interactive Streamlit web interface
- ⚡ Real-time SGPA prediction
- 🎯 Beginner-friendly and lightweight

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Manipulation |
| NumPy | Numerical Computing |
| Scikit-learn | Machine Learning |
| Streamlit | Web Application |
| Matplotlib *(Optional)* | Data Visualization |

---

## 📂 Project Structure

```
SGPA-Predictor/
│
├── app.py                 # Streamlit Application
├── model.py               # Model Training Script
├── sgpa_dataset.csv       # Dataset
├── predictor.pkl          # Saved ML Model
├── requirements.txt       # Dependencies
├── README.md
└── screenshots/
    ├── home.png
    └── prediction.png
```

---

## ⚙️ Machine Learning Workflow

1. Import the dataset
2. Clean and preprocess the data
3. Split data into training and testing sets
4. Train the **Linear Regression** model
5. Evaluate model performance
6. Save the trained model
7. Deploy with Streamlit
8. Predict SGPA from user input

---

## 📊 Model Information

| Attribute | Value |
|-----------|-------|
| Algorithm | Linear Regression |
| Problem Type | Regression |
| Target Variable | SGPA |
| Input Feature | Study Hours |
| Accuracy | **81%** |

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/SGPA-Predictor.git
```

Move into the project directory:

```bash
cd SGPA-Predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 💻 Usage

1. Launch the application.
2. Enter the number of study hours.
3. Click **Predict**.
4. View the estimated SGPA instantly.

---

## 📷 Screenshots

### Home Page

> Add a screenshot here

```
screenshots/home.png
```

### Prediction Output

> Add a screenshot here

```
screenshots/prediction.png
```

---

## 📈 Future Improvements

- Support multiple input features
  - Attendance
  - Previous SGPA
  - Internal marks
  - Assignment scores
- Compare multiple regression algorithms
- Model performance visualization
- Cloud deployment
- User authentication
- Database integration

---

## 📚 Learning Outcomes

This project demonstrates:

- Data preprocessing
- Feature engineering
- Regression analysis
- Model evaluation
- Model serialization
- Streamlit deployment
- End-to-end Machine Learning workflow

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---



> *"Turning study hours into meaningful academic insights through Machine Learning."*
