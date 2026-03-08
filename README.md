# 🩺 Diabetes Predictor Web Application

A production-ready **Machine Learning web application** that predicts whether a user is **Healthy, Prediabetic, or Diabetic** based on responses to **20 clinically relevant health indicators**. The application delivers real-time predictions along with **personalized health feedback and visual probability insights**.

---

## 🚀 Features

* **ML-based Health Risk Classification**
  Predicts diabetes status using a trained **Random Forest Classifier** with ~**84% accuracy**.

* **20 Health Indicators**
  Includes BMI, age, blood pressure, cholesterol, lifestyle habits, physical activity, mental & physical health metrics.

* **Real-time Prediction & Feedback**
  Instant inference via Flask backend with condition-specific and lifestyle-based recommendations.

* **Probability Visualization**
  Displays prediction confidence using a dynamically generated probability bar chart.

* **Production Deployment**
  Publicly hosted on Render for real-world accessibility.

---

## 🧠 Machine Learning Model

* **Algorithm:** Random Forest Classifier

* **Dataset:** BRFSS 2015 (CDC Diabetes Health Indicators)

* **Target Classes:**

  * `0` → Healthy
  * `1` → Prediabetic
  * `2` → Diabetic

* **Model Performance:**

  * Accuracy: **~84%**
  * Optimized for inference speed and deployment size
  * Compressed using **joblib + gzip**

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask
* **Machine Learning:** scikit-learn, Pandas, NumPy
* **Visualization:** Matplotlib
* **Deployment:** Render

---

## 🔄 How It Works

1. User answers **20 health-related questions** via a web form
2. Data is preprocessed and validated on the backend
3. ML model performs real-time inference
4. User receives:

   * Diabetes risk classification
   * Personalized lifestyle & health recommendations
   * Probability visualization of predictions

---

## 🌐 Live Demo

👉 **[https://diabetes-predictor-g5yv.onrender.com/](https://diabetes-predictor-g5yv.onrender.com/)**

---

## 📦 Model Handling & Optimization

* Model trained locally using full dataset
* Serialized with **joblib compression**
* Lightweight inference pipeline optimized for web deployment
* Ensures consistent preprocessing between training and prediction

---

## ⚠️ Disclaimer

This application is **for educational and informational purposes only**.
It is **not a medical diagnostic tool** and should not replace professional medical advice.

---

## 🤝 Contributing

Contributions are welcome!
Feel free to submit pull requests for:

* UI/UX improvements
* Model enhancements
* Performance optimizations
* Feature additions

Please ensure proper testing before submitting changes.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 📧 Contact

For questions or collaboration:
**[ritisarabindra@gmail.com](mailto:ritisarabindra@gmail.com)**
