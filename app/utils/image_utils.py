import requests
from PIL import Image
from io import BytesIO

def load_image(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))
        return image.convert("RGB").resize((224, 224))

    except Exception as e:
        print(f"Image failed: {url}")
        return None