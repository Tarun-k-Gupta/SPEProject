# import gdown

# file_id = '1xmmuwp7AyF4YC9GyM9uP532UVze3X884'
# url = f'https://drive.google.com/uc?id={file_id}'

# output = "./models"  # Specify the output file name

# gdown.download(url, output, quiet=False)


import gdown
import zipfile
import os

# File ID of the zip file on Google Drive
file_id = '1xmmuwp7AyF4YC9GyM9uP532UVze3X884'
url = f'https://drive.google.com/uc?id={file_id}'

# Output directory for the downloaded zip file
downloaded_folder = "./BERTModels"

# Download the zip file
zip_output = os.path.join(downloaded_folder, 'BERTModels.zip')
gdown.download(url, zip_output, quiet=False)

# Create a directory for extracting the contents
# extracted_folder = os.path.join(downloaded_folder)
# os.makedirs(downloaded_folder, exist_ok=True)

# Extract the contents of the zip file
with zipfile.ZipFile(zip_output, 'r') as zip_ref:
    zip_ref.extractall(downloaded_folder)

# Remove the downloaded zip file if needed
os.remove(zip_output)