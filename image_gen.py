from config import AUTH_TOKEN
from IPython.display import Image
import requests
from PIL import Image
from IPython.display import display

HUGGING_FACE_API_TOKEN = AUTH_TOKEN

# Hugging Face API endpoints and headers
BASE_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
REFINER_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-refiner-1.0"
headers = {"Authorization": f"Bearer {HUGGING_FACE_API_TOKEN}"}

def query(payload, api_url):
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.content

def get_image(prompt,ind):
    try:
        initial_image_bytes = query({"inputs": prompt}, BASE_API_URL)
        initial_image_path = f"static/images/{ind}.jpg"
        with open(initial_image_path, "wb") as f:
            f.write(initial_image_bytes)
        display(Image.open(initial_image_path)) 
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
