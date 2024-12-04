import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df_012 = pd.read_csv('diabetes_012_health_indicators_BRFSS2015.csv')

# Data preprocessing
X = df_012.drop('Diabetes_012', axis=1)  # Drop the target variable
y = df_012['Diabetes_012']               # Target variable (0: healthy, 1: prediabetic, 2: diabetic)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Function to take user input for prediction with detailed explanations
def take_user_input():
    print("Please provide the following health-related information:")

    # Asking for health-related features
    HighBP = float(input("High Blood Pressure (1 for Yes, 0 for No): "))
    HighChol = float(input("High Cholesterol (1 for Yes, 0 for No): "))
    CholCheck = float(input("Cholesterol Check in past 5 years (1 for Yes, 0 for No): "))
    BMI = float(input("Body Mass Index (BMI): "))
    Smoker = float(input("Are you a Smoker? (1 for Yes, 0 for No): "))
    Stroke = float(input("Have you had a Stroke? (1 for Yes, 0 for No): "))
    HeartDiseaseorAttack = float(input("Heart Disease or Attack (1 for Yes, 0 for No): "))
    PhysActivity = float(input("Physical Activity in past 30 days (1 for Yes, 0 for No): "))
    Fruits = float(input("Do you consume fruits frequently? (1 for Yes, 0 for No): "))
    Veggies = float(input("Do you consume vegetables frequently? (1 for Yes, 0 for No): "))
    HvyAlcoholConsump = float(input("Heavy Alcohol Consumption (1 for Yes, 0 for No): "))
    AnyHealthcare = float(input("Do you have any Healthcare? (1 for Yes, 0 for No): "))
    NoDocbcCost = float(input("Did you avoid seeing a doctor due to cost? (1 for Yes, 0 for No): "))
    GenHlth = float(input("How would you rate your General Health? (1 = Excellent, 2 = Very Good, 3 = Good, 4 = Fair, 5 = Poor): "))
    MentHlth = float(input("How many days in the past 30 days did you have bad Mental Health? (0-30): "))
    PhysHlth = float(input("How many days in the past 30 days did you have bad Physical Health? (0-30): "))
    DiffWalk = float(input("Do you have Difficulty Walking? (1 for Yes, 0 for No): "))
    Sex = float(input("What is your Sex? (1 for Male, 0 for Female): "))

    # Providing detailed instructions for Age
    print("\nPlease enter your Age category based on the following scale:")
    print("13 = 80+ years old")
    print("12 = 70-74 years old")
    print("11 = 65-69 years old")
    print("10 = 60-64 years old")
    print("9  = 55-59 years old")
    print("8  = 50-54 years old")
    print("7  = 45-49 years old")
    print("6  = 40-44 years old")
    print("5  = 35-39 years old")
    print("4  = 30-34 years old")
    print("3  = 25-29 years old")
    print("2  = 18-24 years old")
    print("1  < 18 years old")
    Age = float(input("Enter your Age category: "))

    # Providing detailed instructions for Education Level
    print("\nPlease enter your Education Level based on the following scale:")
    print("1 = Never attended school or only kindergarten")
    print("2 = Grades 1 through 8 (Elementary School)")
    print("3 = Grades 9 through 11 (Some High School)")
    print("4 = Grade 12 or GED (High School Graduate)")
    print("5 = Some college or technical school")
    print("6 = College graduate")
    Education = float(input("Enter your Education Level: "))

    # Providing detailed instructions for Income Level
    print("\nPlease enter your Income Level based on the following scale:")
    print("1 = Less than $10,000")
    print("2 = $10,000 to less than $15,000")
    print("3 = $15,000 to less than $20,000")
    print("4 = $20,000 to less than $25,000")
    print("5 = $25,000 to less than $35,000")
    print("6 = $35,000 to less than $50,000")
    print("7 = $50,000 to less than $75,000")
    print("8 = $75,000 or more")
    Income = float(input("Enter your Income Level: "))

    # Create a DataFrame for user input
    user_data = pd.DataFrame({
        'HighBP': [HighBP], 'HighChol': [HighChol], 'CholCheck': [CholCheck], 'BMI': [BMI], 'Smoker': [Smoker],
        'Stroke': [Stroke], 'HeartDiseaseorAttack': [HeartDiseaseorAttack], 'PhysActivity': [PhysActivity],
        'Fruits': [Fruits], 'Veggies': [Veggies], 'HvyAlcoholConsump': [HvyAlcoholConsump],
        'AnyHealthcare': [AnyHealthcare], 'NoDocbcCost': [NoDocbcCost], 'GenHlth': [GenHlth],
        'MentHlth': [MentHlth], 'PhysHlth': [PhysHlth], 'DiffWalk': [DiffWalk], 'Sex': [Sex],
        'Age': [Age], 'Education': [Education], 'Income': [Income]
    })

    return user_data

def personalized_health_feedback(prediction, user_data):
    if prediction == 0:
        print("You are healthy! Keep up the good work maintaining your health.")
        print("Here are some tips to stay on track:")
        print("- Follow a balanced diet rich in fruits, vegetables, lean proteins, and whole grains.")
        print("- Stay physically active: Aim for at least 30 minutes of moderate activity most days.")
        print("- Regularly monitor your health with annual check-ups.")
    elif prediction == 1:
        print("You are prediabetic. This is a great time to make changes and prevent diabetes.")
        print("Here’s what you can do:")
        print("- Cut down on sugar and refined carbohydrates (e.g., white bread, sugary drinks).")
        print("- Increase fiber intake by adding more vegetables and whole grains to your meals.")
        print("- Aim for at least 150 minutes of exercise per week (e.g., brisk walking, cycling).")
        print("- Monitor your blood sugar levels regularly and consult a healthcare professional.")
    else:
        print("You are diabetic. It’s crucial to manage your condition actively to stay healthy.")
        print("Consider these steps:")
        print("- Follow a structured meal plan designed for diabetes management.")
        print("- Avoid high-sugar foods and focus on low glycemic index (GI) options.")
        print("- Ensure consistent physical activity and take medications as prescribed.")
        print("- Regularly track blood sugar levels and consult your healthcare provider.")

    print("\n--- Additional Personalized Suggestions ---")

    # BMI-related feedback
    bmi = user_data['BMI'].iloc[0]
    if bmi < 18.5:
        print("Your BMI indicates underweight. Focus on gaining weight healthily with nutrient-rich foods.")
        print("- Include calorie-dense, nutritious foods like nuts, seeds, and whole grains.")
        print("- Consider strength training to build muscle mass.")
    elif 18.5 <= bmi <= 24.9:
        print("Your BMI is within a healthy range. Continue with balanced eating and regular exercise.")
        print("- Maintain this by tracking portion sizes and staying active.")
    elif 25 <= bmi <= 29.9:
        print("Your BMI indicates overweight. Aim for a calorie deficit by eating mindfully and exercising regularly.")
        print("- Try smaller portion sizes and avoid late-night snacking.")
        print("- Include more plant-based meals in your diet.")
    else:
        print("Your BMI indicates obesity. Consider consulting a dietitian to create a sustainable weight-loss plan.")
        print("- Focus on gradual weight loss of 1-2 pounds per week.")
        print("- Reduce processed and fast foods, and choose home-cooked meals.")

    # Smoking-related feedback
    if user_data['Smoker'].iloc[0] == 1:
        print("You are a smoker. Quitting smoking can significantly improve your overall health.")
        print("- Seek support: Smoking cessation programs and apps can help.")
        print("- Replace smoking with healthier habits like chewing gum or exercising.")
        print("- Long-term benefits include better lung function, lower heart disease risk, and improved skin health.")

    # Physical activity-related feedback
    if user_data['PhysActivity'].iloc[0] == 0:
        print("You reported no recent physical activity. Regular exercise can boost heart health and reduce diabetes risk.")
        print("- Start small: Even 10 minutes a day can make a difference.")
        print("- Choose enjoyable activities like walking, dancing, or swimming.")
        print("- Gradually increase your activity level to meet fitness goals.")

    # Dietary habits
    if user_data['Fruits'].iloc[0] == 0:
        print("You consume few fruits. Aim to include 1-2 servings of fruits daily for essential vitamins.")
        print("- Try adding fruits to breakfast or as snacks.")
        print("- Opt for seasonal fruits to enjoy variety and freshness.")
    if user_data['Veggies'].iloc[0] == 0:
        print("You consume few vegetables. Increase your vegetable intake to at least 2 servings daily for better health.")
        print("- Incorporate vegetables into your meals, like salads or soups.")
        print("- Experiment with different cooking methods like steaming or roasting.")

    # Alcohol consumption feedback
    if user_data['HvyAlcoholConsump'].iloc[0] == 1:
        print("You reported heavy alcohol consumption. Reducing alcohol can improve liver health and lower disease risk.")
        print("- Consider setting limits, such as no more than 1-2 drinks per occasion.")
        print("- Alternate alcoholic drinks with water to stay hydrated.")
        print("- Explore non-alcoholic beverages for social occasions.")

    # Stress and mental health feedback
    ment_health_days = user_data['MentHlth'].iloc[0]
    if ment_health_days > 10:
        print("You reported many days of poor mental health. Managing stress can significantly benefit your overall well-being.")
        print("- Try relaxation techniques like meditation, deep breathing, or yoga.")
        print("- Maintain a consistent sleep schedule for better mental clarity.")
        print("- Engage in hobbies or social activities to reduce stress.")

    # Physical health feedback
    phys_health_days = user_data['PhysHlth'].iloc[0]
    if phys_health_days > 10:
        print("You reported frequent physical health challenges. Consider consulting a healthcare provider for further evaluation.")
        print("- Ensure proper hydration and a balanced diet to support overall health.")
        print("- Track symptoms to identify patterns and seek targeted solutions.")

    # Difficulty walking
    if user_data['DiffWalk'].iloc[0] == 1:
        print("You reported difficulty walking. Low-impact exercises like swimming or chair exercises might help improve mobility.")
        print("- Consult a physical therapist for tailored exercises.")
        print("- Use assistive devices like walking sticks if needed.")

    # Income and healthcare access
    if user_data['NoDocbcCost'].iloc[0] == 1:
        print("You reported avoiding doctor visits due to cost. Look into community health programs or clinics that offer affordable care.")
        print("- Research local health initiatives or free medical camps.")
        print("- Many pharmacies offer discounted preventive care services.")

    # Sleep feedback
    if user_data['GenHlth'].iloc[0] >= 4:  # Fair or Poor general health
        print("Poor general health can often be linked to insufficient or irregular sleep.")
        print("- Aim for 7-8 hours of quality sleep per night.")
        print("- Create a bedtime routine, such as reading or light stretching.")

    print("\nRemember, small consistent changes can lead to significant health improvements over time. You’ve got this!")

def predict_diabetes_status_with_visualization(user_data):
    probabilities = model.predict_proba(user_data)[0]  # Get probabilities for each class

    # Visualize the probabilities
    classes = ['Healthy', 'Prediabetic', 'Diabetic']
    plt.figure(figsize=(8, 5))
    sns.barplot(x=classes, y=probabilities, color="blue")
    plt.title("Probabilities for Health Status")
    plt.ylabel("Probability")
    plt.show()


user_data = take_user_input()
prediction = model.predict(user_data)
personalized_health_feedback(prediction, user_data)
predict_diabetes_status_with_visualization(user_data)