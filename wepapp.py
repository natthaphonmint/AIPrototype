from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# โหลดโมเดล
try:
    model = joblib.load('iris_rf_model.pkl')
except:
    model = None
    print("Warning: Model not found.")

class_names = ['Setosa', 'Versicolor', 'Virginica']

@app.route('/')
def home():
    # จุดที่ 1: เปลี่ยนเป็น first.html
    return render_template('first.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        # จุดที่ 2: เปลี่ยนเป็น first.html
        return render_template('first.html', result="Model Error")

    try:
        features = [
            float(request.form['sl']),
            float(request.form['sw']),
            float(request.form['pl']),
            float(request.form['pw'])
        ]
        
        prediction = model.predict([features])[0]
        predicted_class = class_names[prediction]
        
        # จุดที่ 3: เปลี่ยนเป็น first.html (ส่งผลลัพธ์กลับ)
        return render_template('first.html', result=predicted_class)
    
    except Exception as e:
        # จุดที่ 4: เปลี่ยนเป็น first.html (กรณี error)
        return render_template('first.html', result=f"Error: {e}")

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5002)