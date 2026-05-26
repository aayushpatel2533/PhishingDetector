import re
import math
import tldextract
from urllib.parse import urlparse

def calculate_entropy(text):
    """Calculate Shannon entropy of a string"""
    if not text:
        return 0
    
    entropy = 0
    for x in range(256):
        p_x = float(text.count(chr(x))) / len(text)
        if p_x > 0:
            entropy += - p_x * math.log2(p_x)
    return entropy

def extract_features(url):
    """Extract features from a URL for phishing detection"""
    features = {}
    
    # Basic URL metrics
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['num_hyphens'] = url.count('-')
    features['num_slashes'] = url.count('/')
    
    # Security indicators
    features['has_https'] = 1 if url.startswith('https://') else 0
    features['has_ip'] = 1 if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url) else 0
    features['has_at'] = 1 if '@' in url else 0
    
    # Subdomain analysis
    try:
        extracted = tldextract.extract(url)
        subdomain = extracted.subdomain
        features['num_subdomains'] = len(subdomain.split('.')) if subdomain else 0
    except:
        features['num_subdomains'] = 0
    
    # Suspicious keywords
    suspicious_words = ['login', 'verify', 'bank', 'secure', 'account', 
                       'update', 'free', 'lucky', 'winner']
    url_lower = url.lower()
    features['has_suspicious_word'] = 1 if any(word in url_lower for word in suspicious_words) else 0
    
    # Entropy calculation
    features['entropy'] = calculate_entropy(url)
    
    return features

def get_feature_names():
    """Return list of feature names in order"""
    return ['url_length', 'num_dots', 'num_hyphens', 'num_slashes', 
            'has_https', 'has_ip', 'has_at', 'num_subdomains', 
            'has_suspicious_word', 'entropy']
