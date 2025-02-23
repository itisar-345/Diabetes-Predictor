from flask import Flask, render_template, request
import pandas as pd
from model_backend import predict_diabetes  # Import your backend logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve form data with default values
        user_data = pd.DataFrame([{
            'HighBP': int(request.form.get('HighBP', 0)),
            'HighChol': int(request.form.get('HighChol', 0)),
            'CholCheck': int(request.form.get('CholCheck', 0)),
            'BMI': round(float(request.form.get('BMI', 0))),
            'Smoker': int(request.form.get('Smoker', 0)),
            'Stroke': int(request.form.get('Stroke', 0)),
            'HeartDiseaseorAttack': int(request.form.get('HeartDiseaseorAttack', 0)),
            'PhysActivity': int(request.form.get('PhysActivity', 0)),
            'Fruits': int(request.form.get('Fruits', 0)),
            'Veggies': int(request.form.get('Veggies', 0)),
            'HvyAlcoholConsump': int(request.form.get('HvyAlcoholConsump', 0)),
            'AnyHealthcare': int(request.form.get('AnyHealthcare', 0)),
            'NoDocbcCost': int(request.form.get('NoDocbcCost', 0)),
            'GenHlth': int(request.form.get('GenHlth', 0)),
            'MentHlth': int(request.form.get('MentHlth', 0)),
            'PhysHlth': int(request.form.get('PhysHlth', 0)),
            'DiffWalk': int(request.form.get('DiffWalk', 0)),
            'Sex': int(request.form.get('Sex', 0)),
            'Age': int(request.form.get('Age', 0)),
            'Education': int(request.form.get('Education', 0)),
            'Income': int(request.form.get('Income', 0)),
        }])

        # Get prediction and feedback
        prediction, feedback, plot_url = predict_diabetes(user_data)
        return render_template('result.html', prediction=prediction, feedback=feedback, plot_url=plot_url)
    except Exception as e:
        return f"Error processing request: {str(e)}", 400
    
if __name__ == '__main__':
    app.run(debug=True)
