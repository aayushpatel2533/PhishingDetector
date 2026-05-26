# 🛡️ AI Phishing Detector

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-black?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.8-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Accuracy](https://img.shields.io/badge/Accuracy-81.58%25-green?style=for-the-badge)

An AI-powered phishing URL detection system built with Python, Flask, and Machine Learning. Trained on 11,430 real-world URLs to classify whether a given URL is legitimate or a phishing attempt.

---

## 🚀 Features

- Real-time URL scanning via a web interface
- Random Forest ML model trained on 11,430 URLs (50/50 phishing/legitimate)
- 10 URL-based features extracted for prediction
- Shows Model Confidence and Phishing Probability separately
- Dark-themed responsive UI with green/red result indicators

---

## 🧠 How It Works

1. User enters a URL in the web interface
2. 10 features are extracted from the URL
3. A trained Random Forest model predicts if it's phishing or legitimate
4. Result is shown with confidence % and phishing probability %

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Training Dataset | 11,430 URLs |
| Legitimate URLs | 5,715 |
| Phishing URLs | 5,715 |
| Model | Random Forest (200 trees) |
| Accuracy | **81.58%** |
| Legitimate Precision | 79% |
| Phishing Precision | 85% |

### Top Features by Importance

| Feature | Importance |
|---------|-----------|
| URL Entropy | 21.13% |
| Number of Subdomains | 17.73% |
| URL Length | 13.39% |
| Number of Dots | 11.86% |
| Number of Slashes | 11.53% |
| Number of Hyphens | 10.42% |
| Suspicious Keywords | 10.28% |
| Has HTTPS | 2.43% |
| Has @ Symbol | 0.95% |
| Has IP Address | 0.27% |

---

## 🛠️ Tech Stack

- **Language:** Python 3.14
- **Web Framework:** Flask 3.1
- **ML Library:** Scikit-learn 1.8
- **Data Processing:** Pandas, NumPy
- **URL Parsing:** tldextract
- **Model Persistence:** Joblib
- **Dataset:** Kaggle — Web Page Phishing Detection Dataset (11,430 URLs)

---

## 📁 Project Structure

```
PhishingDetector/
├── app.py              # Flask web application
├── features.py         # URL feature extraction
├── train.py            # Model training script
├── download_data.py    # Dataset downloader
├── model.pkl           # Trained ML model
├── dataset.csv         # Training dataset
├── requirements.txt    # Dependencies
└── templates/
    └── index.html      # Web UI
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10+
- pip

### Steps

1. Clone the repository:
```bash
git clone https://github.com/aayushpatel2533/PhishingDetector.git
cd PhishingDetector
```

2. Install dependencies:
```bash
py -m pip install -r requirements.txt
```

3. Download dataset and train model:
```bash
py download_data.py
py train.py
```

4. Start the web app:
```bash
py app.py
```

5. Open in browser:
```
http://127.0.0.1:5000
```

---

## 🧪 Test URLs

**Legitimate:**
- `https://www.google.com`
- `https://www.github.com`
- `https://www.amazon.com`

**Phishing:**
- `http://192.168.1.1/login/verify`
- `http://secure-bank-login.tk/account/update`
- `http://free-winner.ml/claim/prize`

---

## 🔄 Future Improvements

- Train on larger dataset (100k+ URLs)
- Add WHOIS domain age feature
- Add real-time VirusTotal API integration
- Export scan history as PDF report
- Browser extension version

---

## 👨‍💻 Developer

Developed by **Aayush Patel**
GitHub: [github.com/aayushpatel2533](https://github.com/aayushpatel2533)

---

## 📄 License

This project is licensed under the MIT License.
