import gdown
import zipfile
import os

# File ID of the zip file on Google Drive
# file_id = '1xmmuwp7AyF4YC9GyM9uP532UVze3X884'
file_id = '1Jq-yNok4hmY6tlsO9o_A0k72df9_QW7v'
url = f'https://drive.google.com/uc?id={file_id}'

# Output directory for the downloaded zip file
target_folder = "."

# Download the zip file
zip_output = os.path.join(target_folder, 'BERTModels.zip')
gdown.download(url, zip_output, quiet=False)

# Extract the contents of the zip file
with zipfile.ZipFile(zip_output, 'r') as zip_ref:
    zip_ref.extractall(target_folder)

# Remove the downloaded zip file if needed
os.remove(zip_output)