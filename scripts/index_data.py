import json
import numpy as np
import requests

from PIL import Image
from io import BytesIO

from app.api.services.embedding_service import get_text_embedding, get_image_embedding
from app.api.services.pinecone_service import PineconeService
from app.utils.fusion import fuse_embeddings

pinecone_service = PineconeService()

with open("data/sample_products.json") as f:
    products = json.load(f)

def load_image_from_url(url):
    # Download image from URL and convert to PIL Image
    response = requests.get(url, timeout=10)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    image = image.resize((224, 224))
    return image

def normalize(vec):
    # Normalize the vector for stable similarity search
    return vec/ np.linalg.norm(vec)

vectors = []

for product in products:
    try:
        text_embedding = get_text_embedding(product["description"])
        image = load_image_from_url(product["image_url"])
        image_embedding = get_image_embedding(image)
        combined_embedding = 0.6 * np.array(text_embedding) + 0.4 * np.array(image_embedding)

        combined_embedding = normalize(combined_embedding)
    
        # STORE IN PINECONE
        vectors.append({
            "id": product["id"],
            "values" : combined_embedding.tolist(),
            "metadata":{
                "description" : product["description"],
                "image_url" : product["image_url"],
                "category": product.get("category", "")
            }
        })

        print(f"Indexed product {product["id"]}")

    except Exception as e:
        print(f"Failed for product {product["id"]} : {str(e)}")


# Upload to Pinecone
pinecone_service.upsert(vectors)

print("Multimodal indexing completed successfully!")



