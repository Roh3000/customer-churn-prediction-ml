# Customer Churn Prediction using Machine Learning

## 📌 Project Overview
This project predicts whether a customer is likely to churn using Machine Learning techniques.

The project includes:
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Logistic Regression
- SMOTE for handling class imbalance
- Feature Importance Analysis
- Flask Web Application

---

## 🚀 Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Seaborn
- Matplotlib
- Flask
- Joblib

---

## 📊 Machine Learning Workflow
1. Data preprocessing
2. Handling missing values
3. Encoding categorical variables
4. Feature scaling
5. Model training
6. SMOTE balancing
7. Model evaluation
8. Feature importance analysis

---

## 📈 Model Performance

### Logistic Regression with SMOTE
- Recall improved from 52% to 80%
- Better churn detection performance
- Improved F1-score

---

## 🔥 Key Business Insights
- Customers with month-to-month contracts churn more frequently
- Long-term customers are less likely to churn
- Fiber optic users showed higher churn tendency
- Long-term contracts significantly reduce churn

---

## 🌐 Flask Web App
The project also includes a Flask web application where users can:
- Enter customer details
- Predict customer churn
- View churn probability

---

## 📂 Project Structure

```bash
customer-churn-prediction-ml/
│
├── app/
├── model/
├── notebook/
├── templates/
├── churn_model.pkl
├── scaler.pkl
└── README.md
```

---

## ▶️ Run Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Flask app:

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

## 👨‍💻 Author
Rohan Kandhare
