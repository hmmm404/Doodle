import os
import requests

BASE_URL = "https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/"
OUTPUT_DIR = "quickdraw_data"

# Fetch category list from GitHub
category_url = "https://raw.githubusercontent.com/googlecreativelab/quickdraw-dataset/master/categories.txt"
response = requests.get(category_url)
categories = response.text.splitlines()

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Download all categories
for category in categories:
    filename = f"{category}.npy"
    url = BASE_URL + filename
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    if os.path.exists(output_path):
        print(f"{filename} already exists. Skipping...")
        continue

    print(f"Downloading {filename}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"{filename} downloaded successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {filename}: {e}")
