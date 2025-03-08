import pickle
import os
import numpy as np
import pandas as pd

def analyze_chat(message):
    message = message.lower()
    if "smoke" in message:
        return "Smoking is a major risk factor for lung cancer. Regular smoking increases your risk by 15-30 times."
    elif "symptom" in message:
        return "Common symptoms include persistent cough, chest pain, shortness of breath, and coughing up blood."
    elif "prevent" in message:
        return "Prevention includes: not smoking, avoiding secondhand smoke, maintaining a healthy diet, and regular exercise."
    return "I can help answer questions about lung cancer risk factors and symptoms. What would you like to know?"

def predict_lung_cancer(inputs):
    try:
        model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                'saved_model', 'lung_cancer_model.pkl')
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        input_array = np.array(inputs).reshape(1, -1)
        prediction_prob = model.predict_proba(input_array)[0]
        risk_level = "High" if prediction_prob[1] > 0.5 else "Low"
        confidence = prediction_prob[1] if risk_level == "High" else prediction_prob[0]
        return f"{risk_level} Risk of Lung Cancer (Confidence: {confidence:.2%})"
    except Exception as e:
        return f"Error in prediction: {str(e)}"