from flask import Flask, request, render_template_string
import joblib
import numpy as np

app = Flask(__name__)

# Load the model once when the app starts
model = joblib.load('iris_rf_model.pkl')
class_names = ['Setosa', 'Versicolor', 'Virginica']

# --- INLINE HTML TEMPLATE ---
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Iris Classifier</title>
    <style>
        body { font-family: sans-serif; text-align: center; padding: 50px; }
        .container { display: inline-block; border: 1px solid #ddd; padding: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input { margin: 10px 0; padding: 8px; width: 90%; }
        button { padding: 10px 20px; background-color: #28a745; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #218838; }
        .result { margin-top: 20px; font-size: 1.5em; color: #333; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Iris Species Predictor</h2>
        <form action="/predict" method="post">
            <input type="number" step="0.1" name="sl" placeholder="Sepal Length (cm)" required><br>
            <input type="number" step="0.1" name="sw" placeholder="Sepal Width (cm)" required><br>
            <input type="number" step="0.1" name="pl" placeholder="Petal Length (cm)" required><br>
            <input type="number" step="0.1" name="pw" placeholder="Petal Width (cm)" required><br>
            <button type="submit">Predict</button>
        </form>

        {% if result %}
            <div class="result">Result: {{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # Render the HTML string defined above
    return render_template_string(html_template)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features
        features = [
            float(request.form['sl']),
            float(request.form['sw']),
            float(request.form['pl']),
            float(request.form['pw'])
        ]
        
        # Predict
        prediction = model.predict([features])[0]
        predicted_class = class_names[prediction]
        
        # Re-render the same HTML with the result variable
        return render_template_string(html_template, result=predicted_class)
        
    except Exception as e:
        return render_template_string(html_template, result=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)