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
            'HighBP': request.form.get('HighBP', 0),
            'HighChol': request.form.get('HighChol', 0),
            'CholCheck': request.form.get('CholCheck', 0),
            'BMI': request.form.get('BMI', 0),
            'Smoker': request.form.get('Smoker', 0),
            'Stroke': request.form.get('Stroke', 0),
            'HeartDiseaseorAttack': request.form.get('HeartDiseaseorAttack', 0),
            'PhysActivity': request.form.get('PhysActivity', 0),
            'Fruits': request.form.get('Fruits', 0),
            'Veggies': request.form.get('Veggies', 0),
            'HvyAlcoholConsump': request.form.get('HvyAlcoholConsump', 0),
            'AnyHealthcare': request.form.get('AnyHealthcare', 0),
            'NoDocbcCost': request.form.get('NoDocbcCost', 0),
            'GenHlth': request.form.get('GenHlth', 0),
            'MentHlth': request.form.get('MentHlth', 0),
            'PhysHlth': request.form.get('PhysHlth', 0),
            'DiffWalk': request.form.get('DiffWalk', 0),
            'Sex': request.form.get('Sex', 0),
            'Age': request.form.get('Age', 0),
            'Education': request.form.get('Education', 0),
            'Income': request.form.get('Income', 0),
        }])

        # Get prediction and feedback
        prediction, feedback, plot_url = predict_diabetes(user_data)
        return render_template('result.html', prediction=prediction, feedback=feedback, plot_url=plot_url)
    except Exception as e:
        return f"Error processing request: {str(e)}", 400
    
if __name__ == '__main__':
    app.run(debug=True)
