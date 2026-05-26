# AI Phishing Detector

A machine learning-powered web application that detects phishing URLs using Random Forest classification.

## Features

- **10 Feature Extraction**: Analyzes URLs based on length, structure, security indicators, and entropy
- **Random Forest Classifier**: Trained on legitimate and phishing URL patterns
- **Dark-Themed Web Interface**: Modern UI with green accent colors
- **Real-time Predictions**: Instant phishing detection with confidence scores
- **Risk Assessment**: Provides risk score percentage for each URL

## Project Structure

```
PhishingDetector/
├── features.py          # Feature extraction logic
├── train.py            # Model training script
├── app.py              # Flask web application
├── templates/
│   └── index.html      # Web interface
├── model.pkl           # Trained model (generated)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Step 1: Train the Model

Run the training script to create the model:

```bash
python train.py
```

This will:
- Extract features from 20 hardcoded URLs (10 legitimate, 10 phishing)
- Train a Random Forest classifier
- Display accuracy and classification report
- Save the model as `model.pkl`

### Step 2: Start the Web Application

Launch the Flask server:

```bash
python app.py
```

Access the application at: `http://127.0.0.1:5000`

### Step 3: Scan URLs

1. Enter a URL in the input field
2. Click "Scan URL" or press Enter
3. View the results:
   - **Prediction**: PHISHING or LEGITIMATE
   - **Confidence**: Model confidence percentage
   - **Risk Score**: Probability of being phishing (0-100%)

## Features Extracted

1. **url_length**: Total character count
2. **num_dots**: Number of dots in URL
3. **num_hyphens**: Number of hyphens
4. **num_slashes**: Number of slashes
5. **has_https**: HTTPS protocol indicator
6. **has_ip**: IP address presence
7. **has_at**: @ symbol presence
8. **num_subdomains**: Subdomain count
9. **has_suspicious_word**: Suspicious keyword detection
10. **entropy**: Shannon entropy of URL string

## Suspicious Keywords

The detector checks for these keywords:
- login, verify, bank, secure, account
- update, free, lucky, winner

## Technology Stack

- **Backend**: Flask (Python web framework)
- **ML Model**: scikit-learn Random Forest Classifier
- **Feature Extraction**: tldextract, regex, entropy calculation
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Model Persistence**: joblib

## API Endpoints

### GET /
Returns the main web interface

### POST /predict
Accepts JSON with URL and returns prediction

**Request:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "prediction": "LEGITIMATE",
  "confidence": 95.5,
  "risk_score": 4.5,
  "url": "https://example.com"
}
```

### GET /health
Health check endpoint

## Model Performance

The model is trained on a small dataset for demonstration purposes. For production use, train on a larger, more diverse dataset.

## Security Note

This is a demonstration project. For production use:
- Train on a larger dataset (1000+ URLs)
- Implement additional features (WHOIS data, page content analysis)
- Add rate limiting and input validation
- Use HTTPS in production
- Regularly retrain the model with new phishing patterns

## License

MIT License - Feel free to use and modify for your projects.
