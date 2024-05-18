# Custom version
# mohist / catserver   Install forge   first
# purpur               Install fabric  first
# snapshot             Install vanilla first

# Ngrok region
# Code           Place
#-----------     ---------------------------
# ap	          Asia/Pacific (Singapore)
# au		  Australia (Sydney)
# eu		  Europe (Frankfurt)
# in		  India (Mumbai)
# jp		  Japan (Tokyo)
# sa		  South America (São Paulo)
# us		  United States (Ohio)
# us-cal-1	  United States (California)

import requests
import os
import base64
import time

def create_gitignore():
    if not os.path.exists(".gitignore"):
        encoded_content = (
            "L3dvcmtfYXJlYQ0KL3NlcnZpZG9yX21pbmVjcmFmdA0KL21pbmVjcmFmdF9zZXJ2ZXINCi9zZXJ2"
            "aWRvcl9taW5lY3JhZnRfb2xkDQovdGFpbHNjYWxlLWNzDQovdGhhbm9zDQovYmtkaXINCi92ZW5k"
            "b3INCmNvbXBvc2VyLioNCmNvbmZpZ3VyYXRpb24uanNvbg0KY29uZmlndXJhY2lvbi5qc29uDQoq"
            "LnR4dA0KKi5weWMNCioub3V0cHV0"
        )
        decoded_content = base64.standard_b64decode(encoded_content).decode()
        with open(".gitignore", 'w') as gitignore_file:
            gitignore_file.write(decoded_content)

def download_latest_release(download_path='.'):
    mirror_url = "https://elyxdev.github.io/latest"
    response = requests.get(mirror_url)

    if response.status_code == 200:
        data = response.json()
        url = data.get('url')
        version = url.split("/")[-1]
        pathto = os.path.join(download_path, version)

        with requests.get(url, stream=True) as download_response:
            download_response.raise_for_status()
            with open(pathto, 'wb') as file:
                for chunk in download_response.iter_content(chunk_size=8192):
                    file.write(chunk)

        return pathto
    else:
        response.raise_for_status()

def main():
    create_gitignore()
    downloaded_file = download_latest_release()

    if downloaded_file.endswith(".pyc"):
        os.system(f"python3 {downloaded_file}")
    else:
        os.system(f"chmod +x {downloaded_file} && ./{downloaded_file}")

if __name__ == "__main__":
    main()