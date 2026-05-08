from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
# Load model and scaler
model = joblib.load("C:/Users/Roh00/Downloads/customer_churn_prediction/churn_model.pkl")
scaler = joblib.load("C:/Users/Roh00/Downloads/customer_churn_prediction/scaler.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    tenure = float(request.form["tenure"])
    monthly_charges = float(request.form["monthly_charges"])
    total_charges = float(request.form["total_charges"])

    # Example input array
    input_data = np.array([[tenure, monthly_charges, total_charges]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction_prob = model.predict_proba(input_scaled)[0][1]

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        result = f"Customer is likely to churn ({prediction_prob * 100:.2f}% probability)"
    else:
        result = f"Customer is likely to stay ({(1 - prediction_prob) * 100:.2f}% confidence)"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)