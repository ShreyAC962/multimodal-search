import json
import numpy as np

from app.services.embedding_service import get_text_embedding, get_image_embedding
from app.services.pinecone_service import PineconeService
from app.utils.image_utils import load_image

pinecone_service = PineconeService()

with open("data/sample_products.json") as f:
    products = json.load(f)

vectors = []

for product in products:
    try:
        # TEXT
        text_emb = get_text_embedding(product["description"])
        if text_emb is None:
            continue

        # IMAGE
        image = load_image(product["image_url"])
        if image is None:
            print(f"Skipping {product['id']} bad image")
            continue

        image_emb = get_image_embedding(image)
        if image_emb is None:
            continue

        # FORCE SAME SHAPE
        text_emb = np.array(text_emb).flatten()
        image_emb = np.array(image_emb).flatten()

        if text_emb.shape != image_emb.shape:
            print(f"Skipping {product['id']} shape mismatch")
            continue

        # FUSION
        combined = (0.6 * text_emb + 0.4 * image_emb).astype("float32")

        vectors.append({
            "id": str(product["id"]),
            "values": combined.tolist(),
            "metadata": {
                "description": product["description"],
                "image_url": product["image_url"],
                "category": product.get("category", "")
            }
        })

        print(f"Indexed {product['id']}")

    except Exception as e:
        print(f"Failed {product['id']} -> {e}")

if len(vectors) == 0:
    raise ValueError("No valid vectors generated!")

pinecone_service.upsert(vectors)

print("Indexing completed successfully!")