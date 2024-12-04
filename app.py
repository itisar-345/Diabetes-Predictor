from flask import Flask, render_template, request
import pandas as pd
from model_backend import predict_diabetes  # Import your backend logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    user_data = pd.DataFrame([{
        'HighBP': request.form['HighBP'],
        'HighChol': request.form['HighChol'],
        'CholCheck': request.form['CholCheck'],
        'BMI': request.form['BMI'],
        'Smoker': request.form['Smoker'],
        'Stroke': request.form['Stroke'],
        'HeartDiseaseorAttack': request.form['HeartDiseaseorAttack'],
        'PhysActivity': request.form['PhysActivity'],
        'Fruits': request.form['Fruits'],
        'Veggies': request.form['Veggies'],
        'HvyAlcoholConsump': request.form['HvyAlcoholConsump'],
        'AnyHealthcare': request.form['AnyHealthcare'],
        'NoDocbcCost': request.form['NoDocbcCost'],
        'GenHlth': request.form['GenHlth'],
        'MentHlth': request.form['MentHlth'],
        'PhysHlth': request.form['PhysHlth'],
        'DiffWalk': request.form['DiffWalk'],
        'Sex': request.form['Sex'],
        'Age': request.form['Age'],
        'Education': request.form['Education'],
        'Income': request.form['Income']
    }])

    # Get prediction and feedback
    prediction, feedback, plot_url = predict_diabetes(user_data)

    return render_template('result.html', prediction=prediction, feedback=feedback, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
