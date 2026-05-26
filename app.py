from flask import Flask, render_template, request, jsonify
import joblib
import os
from features import extract_features, get_feature_names

app = Flask(__name__)

# Load the trained model on startup
MODEL_PATH = 'model.pkl'
model = None

def load_model():
    """Load the trained model"""
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print(f"Model loaded successfully from {MODEL_PATH}")
    else:
        print(f"ERROR: Model file '{MODEL_PATH}' not found!")
        print("Please run train.py first to create the model.")

# Load model when app starts
load_model()

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Predict if a URL is phishing or legitimate"""
    try:
        # Check if model is loaded
        if model is None:
            return jsonify({
                'error': 'Model not loaded. Please train the model first by running train.py'
            }), 500
        
        # Get URL from request
        data = request.get_json()
        url = data.get('url', '').strip()
        
        if not url:
            return jsonify({
                'error': 'URL is required'
            }), 400
        
        # Extract features
        features = extract_features(url)
        feature_values = [[features[name] for name in get_feature_names()]]
        
        # Make prediction
        prediction = model.predict(feature_values)[0]
        prediction_proba = model.predict_proba(feature_values)[0]
        
        # Calculate confidence and risk score
        confidence = max(prediction_proba) * 100  # How confident the model is overall
        risk_score = prediction_proba[1] * 100    # Phishing probability specifically
        
        # Prepare response
        result = {
            'prediction': 'PHISHING' if prediction == 1 else 'LEGITIMATE',
            'confidence': round(confidence, 2),
            'risk_score': round(risk_score, 2),
            'url': url
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

if __name__ == '__main__':
    print("=" * 60)
    print("AI PHISHING DETECTOR - WEB APPLICATION")
    print("=" * 60)
    print("\nStarting Flask server...")
    print("Access the application at: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
