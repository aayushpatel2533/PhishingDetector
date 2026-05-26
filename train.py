import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from features import extract_features, get_feature_names

# Hardcoded dataset: 10 legitimate, 10 phishing URLs (fallback)
FALLBACK_DATASET = [
    # Legitimate URLs (label = 0)
    ("https://www.google.com", 0),
    ("https://www.github.com", 0),
    ("https://www.amazon.com", 0),
    ("https://www.microsoft.com", 0),
    ("https://www.wikipedia.org", 0),
    ("https://www.stackoverflow.com", 0),
    ("https://www.reddit.com", 0),
    ("https://www.linkedin.com", 0),
    ("https://www.youtube.com", 0),
    ("https://www.apple.com", 0),
    
    # Phishing URLs (label = 1)
    ("http://secure-login-bank-verify.com/account/update", 1),
    ("http://192.168.1.1/login.php", 1),
    ("http://paypal-secure-login.verify-account.com", 1),
    ("http://free-winner-lucky-prize.com/claim", 1),
    ("http://amazon-account-update.secure-login.net", 1),
    ("http://bank-verify@malicious.com/login", 1),
    ("http://microsoft-secure-update.account-verify.com", 1),
    ("http://apple-id-login-verify.com/secure/account", 1),
    ("http://google-account-secure.verify-login.net", 1),
    ("http://netflix-free-account.winner-lucky.com", 1),
]

def load_dataset_from_csv(csv_path="dataset.csv"):
    """Load dataset from CSV file"""
    try:
        print(f"Loading dataset from {csv_path}...")
        df = pd.read_csv(csv_path)
        
        # Check if required columns exist
        if 'url' not in df.columns or 'status' not in df.columns:
            print(f"✗ CSV must have 'url' and 'status' columns")
            return None
        
        # Convert status to binary: phishing=1, legitimate=0
        df['label'] = df['status'].apply(lambda x: 1 if str(x).lower() == 'phishing' else 0)
        
        # Create dataset list
        dataset = list(zip(df['url'], df['label']))
        
        print(f"✓ Loaded {len(dataset):,} URLs from CSV")
        print(f"  - Legitimate: {df['label'].value_counts().get(0, 0):,}")
        print(f"  - Phishing: {df['label'].value_counts().get(1, 0):,}")
        
        return dataset
        
    except FileNotFoundError:
        print(f"✗ File '{csv_path}' not found")
        return None
    except Exception as e:
        print(f"✗ Error loading CSV: {e}")
        return None

def main():
    print("=" * 60)
    print("AI PHISHING DETECTOR - TRAINING")
    print("=" * 60)
    
    # Try to load dataset from CSV first
    dataset = load_dataset_from_csv("dataset.csv")
    
    if dataset is None:
        print("\n⚠ Falling back to hardcoded dataset (20 URLs)")
        dataset = FALLBACK_DATASET
    
    # Extract features from all URLs
    print("\nExtracting features from URLs...")
    X = []
    y = []
    
    for url, label in dataset:
        features = extract_features(url)
        feature_values = [features[name] for name in get_feature_names()]
        X.append(feature_values)
        y.append(label)
    
    # Convert to DataFrame for better visualization
    df = pd.DataFrame(X, columns=get_feature_names())
    df['label'] = y
    
    print(f"\nDataset shape: {df.shape}")
    print(f"Legitimate URLs: {y.count(0)}")
    print(f"Phishing URLs: {y.count(1)}")
    
    # Split dataset (80/20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"\nTraining set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}")
    
    # Train Random Forest Classifier
    print("\nTraining Random Forest Classifier...")
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy: {accuracy * 100:.2f}%")
    
    # Print classification report
    print("\nClassification Report:")
    print("=" * 60)
    print(classification_report(y_test, y_pred, 
                                target_names=['Legitimate', 'Phishing'],
                                zero_division=0))
    
    # Feature importance
    print("\nFeature Importance:")
    print("=" * 60)
    feature_importance = pd.DataFrame({
        'feature': get_feature_names(),
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    for idx, row in feature_importance.iterrows():
        print(f"{row['feature']:20s}: {row['importance']:.4f}")
    
    # Save model
    model_filename = 'model.pkl'
    joblib.dump(model, model_filename)
    print(f"\nModel saved as '{model_filename}'")
    print("=" * 60)
    print("Training completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
