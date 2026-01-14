# app.py
from flask import Flask, request, render_template_string, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# --- INLINE HTML TEMPLATE ---
# HTML_TEMPLATE = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Iris Classifier (Single File)</title>
#     <style>
#         body { font-family: Arial, sans-serif; max-width: 500px; margin: 50px auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; }
#         h2 { text-align: center; color: #333; }
#         .form-group { margin-bottom: 15px; }
#         label { display: block; margin-bottom: 5px; font-weight: bold; }
#         input { width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
#         button { width: 100%; background-color: #007BFF; color: white; padding: 10px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
#         button:hover { background-color: #0056b3; }
#         .result { margin-top: 20px; padding: 15px; background-color: #d4edda; color: #155724; text-align: center; border-radius: 4px; }
#         .error { margin-top: 20px; padding: 15px; background-color: #f8d7da; color: #721c24; text-align: center; border-radius: 4px; }
#     </style>
# </head>
# <body>
#     <h2>🌸 Iris Species Predictor</h2>
    
#     <form action="/" method="post">
#         <div class="form-group">
#             <label>Sepal Length (cm):</label>
#             <input type="number" step="0.1" name="sepal_length" required placeholder="5.1">
#         </div>
#         <div class="form-group">
#             <label>Sepal Width (cm):</label>
#             <input type="number" step="0.1" name="sepal_width" required placeholder="3.5">
#         </div>
#         <div class="form-group">
#             <label>Petal Length (cm):</label>
#             <input type="number" step="0.1" name="petal_length" required placeholder="1.4">
#         </div>
#         <div class="form-group">
#             <label>Petal Width (cm):</label>
#             <input type="number" step="0.1" name="petal_width" required placeholder="0.2">
#         </div>
#         <button type="submit">Classify</button>
#     </form>

#     {% if prediction %}
#     <div class="result">
#         <strong>Prediction:</strong> {{ prediction }}
#     </div>
#     {% endif %}

#     {% if error %}
#     <div class="error">
#         {{ error }}
#     </div>
#     {% endif %}
# </body>
# </html>
# """

# --- FLASK ROUTES ---

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None
    
    # 1. กำหนดค่าเริ่มต้นให้กับ val เพื่อไม่ให้หน้าเว็บ Error ตอนเปิดครั้งแรก (GET)
    val = {'sl': 5.1, 'sw': 3.5, 'pl': 1.4, 'pw': 0.2}

    if request.method == 'POST':
        try:
            if not os.path.exists('iris_model.pkl'):
                return render_template('first.html', error="Model not found!", val=val)

            model = joblib.load('iris_model.pkl')
            classes = joblib.load('iris_classes.pkl')

            # 2. รับค่าจาก Form และอัปเดตค่าใน val
            val = {
                'sl': request.form.get('sepal_length'),
                'sw': request.form.get('sepal_width'),
                'pl': request.form.get('petal_length'),
                'pw': request.form.get('petal_width')
            }

            features = [float(val['sl']), float(val['sw']), float(val['pl']), float(val['pw'])]
            prediction_idx = model.predict([features])[0]
            prediction = classes[prediction_idx].capitalize()

        except Exception as e:
            error = f"Error: {str(e)}"

    # 3. ส่งตัวแปร val เข้าไปด้วยใน render_template
    return render_template('first.html', prediction=prediction, error=error, val=val)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8001)
