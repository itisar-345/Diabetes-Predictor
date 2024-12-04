import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import joblib

# Load the model directly from the local file system
model_path = "model_compressed.joblib" 

try:
    model = joblib.load(model_path)
    print("Model loaded successfully from local file!")
except FileNotFoundError:
    raise Exception(f"Model file not found at {model_path}. Please check the file path.")

def predict_diabetes(user_data):
    """
    Takes user data as input, predicts diabetes status, and provides feedback.
    """

    # Print the input data for debugging
    print("User Data:", user_data)

     # Handle missing values by filling with 0 (or another appropriate value)
    user_data = user_data.fillna(0)
    print("User Data after filling missing values:", user_data)

    # Ensure correct data types
    user_data['BMI'] = user_data['BMI'].astype(float) 
    user_data['Age'] = user_data['Age'].astype(int)  
    user_data['HighBP'] = user_data['HighBP'].astype(int)
    user_data['HighChol'] = user_data['HighChol'].astype(int)
    user_data['Smoker'] = user_data['Smoker'].astype(int)
    user_data['PhysActivity'] = user_data['PhysActivity'].astype(int)
    user_data['Fruits'] = user_data['Fruits'].astype(int)
    user_data['Veggies'] = user_data['Veggies'].astype(int)
    user_data['HvyAlcoholConsump'] = user_data['HvyAlcoholConsump'].astype(int)
    user_data['AnyHealthcare'] = user_data['AnyHealthcare'].astype(int)
    user_data['NoDocbcCost'] = user_data['NoDocbcCost'].astype(int)
    user_data['GenHlth'] = user_data['GenHlth'].astype(int)
    user_data['MentHlth'] = user_data['MentHlth'].astype(int)
    user_data['PhysHlth'] = user_data['PhysHlth'].astype(int)
    user_data['DiffWalk'] = user_data['DiffWalk'].astype(int)
    user_data['Sex'] = user_data['Sex'].astype(int)
    user_data['Education'] = user_data['Education'].astype(int)
    user_data['Income'] = user_data['Income'].astype(int)

    prediction = model.predict(user_data)[0]
    probabilities = model.predict_proba(user_data)[0]
    feedback = generate_feedback(prediction, user_data)
    plot_url = generate_barplot(probabilities)
    return prediction, feedback, plot_url

def generate_feedback(prediction, user_data):
    """
    Generates personalized health feedback based on the prediction and user data.
    """
    feedback = ""

    # General feedback based on prediction
    if prediction == 0:
        feedback += "<h2>Health Status: Healthy</h2>"
        feedback += "<p>You are healthy! Keep up the good work maintaining your health.</p>"
        feedback += "<h3>Here are some tips to stay on track:</h3>"
        feedback += "<ul>"
        feedback += "<li>Follow a balanced diet rich in fruits, vegetables, lean proteins, and whole grains.</li>"
        feedback += "<li>Stay physically active: Aim for at least 30 minutes of moderate activity most days.</li>"
        feedback += "<li>Regularly monitor your health with annual check-ups.</li>"
        feedback += "</ul>"
    elif prediction == 1:
        feedback += "<h2>Health Status: Prediabetic</h2>"
        feedback += "<p>You are prediabetic. This is a great time to make changes and prevent diabetes.</p>"
        feedback += "<h3>Here’s what you can do:</h3>"
        feedback += "<ul>"
        feedback += "<li>Cut down on sugar and refined carbohydrates (e.g., white bread, sugary drinks).</li>"
        feedback += "<li>Increase fiber intake by adding more vegetables and whole grains to your meals.</li>"
        feedback += "<li>Aim for at least 150 minutes of exercise per week (e.g., brisk walking, cycling).</li>"
        feedback += "<li>Monitor your blood sugar levels regularly and consult a healthcare professional.</li>"
        feedback += "</ul>"
    else:
        feedback += "<h2>Health Status: Diabetic</h2>"
        feedback += "<p>You are diabetic. It’s crucial to manage your condition actively to stay healthy.</p>"
        feedback += "<h3>Consider these steps:</h3>"
        feedback += "<ul>"
        feedback += "<li>Follow a structured meal plan designed for diabetes management.</li>"
        feedback += "<li>Avoid high-sugar foods and focus on low glycemic index (GI) options.</li>"
        feedback += "<li>Ensure consistent physical activity and take medications as prescribed.</li>"
        feedback += "<li>Regularly track blood sugar levels and consult your healthcare provider.</li>"
        feedback += "</ul>"
        
    feedback += "<h3>Additional Personalized Suggestions:</h3><ul>"

    # BMI-related feedback
    bmi = user_data['BMI'].iloc[0]
    if bmi < 18.5:
        feedback += '<ul class="bmi-feedback">'
        feedback += "<li><strong>Your BMI indicates underweight. Focus on gaining weight healthily with nutrient-rich foods.</strong></li>"
        feedback += "<li>Include calorie-dense, nutritious foods like nuts, seeds, and whole grains.</li>"
        feedback += "<li>Consider strength training to build muscle mass.</li>"
        feedback += "</ul>"
    elif 18.5 <= bmi <= 24.9:
        feedback += '<ul class="bmi-feedback">'
        feedback += "<li><strong>Your BMI is within a healthy range. Continue with balanced eating and regular exercise.</strong></li>"
        feedback += "<li>Maintain this by tracking portion sizes and staying active.</li>"
        feedback += "</ul>"
    elif 25 <= bmi <= 29.9:
        feedback += '<ul class="bmi-feedback">'
        feedback += "<li><strong>Your BMI indicates overweight. Aim for a calorie deficit by eating mindfully and exercising regularly.</strong></li>"
        feedback += "<li>Try smaller portion sizes and avoid late-night snacking.</li>"
        feedback += "<li>Include more plant-based meals in your diet.</li>"
        feedback += "</ul>"
    else:
        feedback += '<ul class="bmi-feedback">'
        feedback += "<li><strong>Your BMI indicates obesity. Consider consulting a dietitian to create a sustainable weight-loss plan.</strong></li>"
        feedback += "<li>Focus on gradual weight loss of 1-2 pounds per week.</li>"
        feedback += "<li>Reduce processed and fast foods, and choose home-cooked meals.</li>"
        feedback += "</ul>"

    # Smoking-related feedback
    if user_data['Smoker'].iloc[0] == 1:
        feedback += '<ul class="smoking-feedback">'
        feedback += "<li><strong>You are a smoker. Quitting smoking can significantly improve your overall health.</li></strong>"
        feedback += "<li>Seek support: Smoking cessation programs and apps can help.</li>"
        feedback += "<li>Replace smoking with healthier habits like chewing gum or exercising.</li>"
        feedback += "<li>Long-term benefits include better lung function, lower heart disease risk, and improved skin health.</li>"
        feedback += "</ul>"

    # Physical activity-related feedback
    if user_data['PhysActivity'].iloc[0] == 0:
        feedback += '<ul class="activity-feedback">'        
        feedback += "<li><strong>You reported no recent physical activity. Regular exercise can boost heart health and reduce diabetes risk.</li></strong>"
        feedback += "<li>Start small: Even 10 minutes a day can make a difference.</li>"
        feedback += "<li>Choose enjoyable activities like walking, dancing, or swimming.</li>"
        feedback += "<li>Gradually increase your activity level to meet fitness goals.</li>"
        feedback += "</ul>"

    # Dietary habits
    if user_data['Fruits'].iloc[0] == 0:
        feedback += '<ul class="diet-feedback">'        
        feedback += "<li><strong>You consume few fruits. Aim to include 1-2 servings of fruits daily for essential vitamins.</li></strong>"
        feedback += "<li>Try adding fruits to breakfast or as snacks.</li>"
        feedback += "<li>Opt for seasonal fruits to enjoy variety and freshness.</li>"
        feedback += "</ul>"
    if user_data['Veggies'].iloc[0] == 0:
        feedback += '<ul class="diet-feedback">'
        feedback += "<li><strong>You consume few vegetables. Increase your vegetable intake to at least 2 servings daily for better health.</li></strong>"
        feedback += "<li>Incorporate vegetables into your meals, like salads or soups.</li>"
        feedback += "<li>Experiment with different cooking methods like steaming or roasting.</li>"
        feedback += "</ul>"

    # Alcohol consumption feedback
    if user_data['HvyAlcoholConsump'].iloc[0] == 1:
        feedback += '<ul class="alcohol-feedback">'
        feedback += "<li><strong>You reported heavy alcohol consumption. Reducing alcohol can improve liver health and lower disease risk.</li></strong>"
        feedback += "<li>Consider setting limits, such as no more than 1-2 drinks per occasion.</li>"
        feedback += "<li>Alternate alcoholic drinks with water to stay hydrated.</li>"
        feedback += "<li>Explore non-alcoholic beverages for social occasions.</li>"
        feedback += "</ul>"

    # Stress and mental health feedback
    ment_health_days = user_data['MentHlth'].iloc[0]
    if ment_health_days > 10:
        feedback += '<ul class="mental-health-feedback">'
        feedback += "<li><strong>You reported many days of poor mental health. Managing stress can significantly benefit your overall well-being.</li></strong>"
        feedback += "<li>Try relaxation techniques like meditation, deep breathing, or yoga.</li>"
        feedback += "<li>Maintain a consistent sleep schedule for better mental clarity.</li>"
        feedback += "<li>Engage in hobbies or social activities to reduce stress.</li>"
        feedback += "</ul>"

    # Physical health feedback
    phys_health_days = user_data['PhysHlth'].iloc[0]
    if phys_health_days > 10:
        feedback += '<ul class="health-issues-feedback">'
        feedback += "<li><strong>You reported frequent physical health challenges. Consider consulting a healthcare provider for further evaluation.</li></strong>"
        feedback += "<li>Ensure proper hydration and a balanced diet to support overall health.</li>"
        feedback += "<li>Track symptoms to identify patterns and seek targeted solutions.</li>"
        feedback += "</ul>"

    # Difficulty walking
    if user_data['DiffWalk'].iloc[0] == 1:
        feedback += '<ul class="walking-feedback">'
        feedback += "<li><strong>You reported difficulty walking. Low-impact exercises like swimming or chair exercises might help improve mobility.</li></strong>"
        feedback += "<li>Consult a physical therapist for tailored exercises.</li>"
        feedback += "<li>Use assistive devices like walking sticks if needed.</li>"
        feedback += "</ul>"

    # Income and healthcare access
    if user_data['NoDocbcCost'].iloc[0] == 1:
        feedback += '<ul class="healthcare-feedback">'
        feedback += "<li><strong>You reported avoiding doctor visits due to cost. Look into community health programs or clinics that offer affordable care.</li></strong>"
        feedback += "<li>Research local health initiatives or free medical camps.</li>"
        feedback += "<li>Many pharmacies offer discounted preventive care services.</li>"
        feedback += "</ul>"

    # Sleep feedback
    if user_data['GenHlth'].iloc[0] >= 4:
        feedback += '<ul class="sleep-feedback">' 
        feedback += "<li><strong>Poor general health can often be linked to insufficient or irregular sleep.</li></strong>"
        feedback += "<li>Aim for 7-8 hours of quality sleep per night.</li>"
        feedback += "<li>Create a bedtime routine, such as reading or light stretching.</li>"
        feedback += "</ul>"

    feedback += "</ul>"
    feedback += "<p><strong>Note:</strong> Remember, small consistent changes can lead to significant health improvements over time. You’ve got this!</p>"    
    
    return feedback

def generate_barplot(probabilities):
    """
    Generate a barplot for the prediction probabilities and return the image as a base64 string.
    """
    classes = ['Healthy', 'Prediabetic', 'Diabetic']
    plt.figure(figsize=(6, 4))
    plt.bar(classes, probabilities, color=['#4CAF50', '#FF9800', '#F44336'])
    plt.title("Prediction Probabilities")
    plt.ylabel("Probability")
    plt.ylim(0, 1)  # Probabilities are between 0 and 1
    plt.xticks(rotation=45)

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    # Encode the image to a base64 string
    plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
    buf.close()
    plt.close()  # Close the plot
    return plot_url

