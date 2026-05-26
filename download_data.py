import os
import shutil
import subprocess
import sys

def install_kagglehub():
    """Install kagglehub if not already installed"""
    try:
        import kagglehub
        print("✓ kagglehub is already installed")
        return True
    except ImportError:
        print("Installing kagglehub...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "kagglehub"])
            print("✓ kagglehub installed successfully")
            return True
        except Exception as e:
            print(f"✗ Failed to install kagglehub: {e}")
            return False

def download_dataset():
    """Download the phishing detection dataset from Kaggle"""
    try:
        import kagglehub
        
        print("\n" + "=" * 60)
        print("DOWNLOADING PHISHING DETECTION DATASET")
        print("=" * 60)
        
        # Download dataset
        print("\nDownloading dataset from Kaggle...")
        print("Dataset: shashwatwork/web-page-phishing-detection-dataset")
        
        path = kagglehub.dataset_download("shashwatwork/web-page-phishing-detection-dataset")
        
        print(f"\n✓ Dataset downloaded to: {path}")
        
        # Find CSV file in the downloaded path
        csv_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.csv'):
                    csv_files.append(os.path.join(root, file))
        
        if not csv_files:
            print("✗ No CSV files found in the downloaded dataset")
            return False
        
        # Use the first CSV file found
        source_csv = csv_files[0]
        print(f"\n✓ Found CSV file: {os.path.basename(source_csv)}")
        
        # Copy to project folder as dataset.csv
        destination_csv = "dataset.csv"
        shutil.copy2(source_csv, destination_csv)
        
        print(f"✓ Copied to project folder as: {destination_csv}")
        
        # Get file size
        file_size = os.path.getsize(destination_csv)
        file_size_mb = file_size / (1024 * 1024)
        
        print(f"\n✓ File size: {file_size_mb:.2f} MB")
        
        # Count lines (approximate number of URLs)
        with open(destination_csv, 'r', encoding='utf-8') as f:
            line_count = sum(1 for _ in f) - 1  # Subtract header
        
        print(f"✓ Number of URLs: {line_count:,}")
        
        print("\n" + "=" * 60)
        print("DATASET DOWNLOAD COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print("\nYou can now run: python train.py")
        
        return True
        
    except Exception as e:
        print(f"\n✗ Error downloading dataset: {e}")
        print("\nMake sure you have:")
        print("1. Kaggle account set up")
        print("2. Kaggle API credentials configured (~/.kaggle/kaggle.json)")
        print("3. Internet connection")
        return False

def main():
    print("=" * 60)
    print("PHISHING DATASET DOWNLOADER")
    print("=" * 60)
    
    # Install kagglehub if needed
    if not install_kagglehub():
        print("\n✗ Cannot proceed without kagglehub")
        return
    
    # Download dataset
    download_dataset()

if __name__ == "__main__":
    main()
