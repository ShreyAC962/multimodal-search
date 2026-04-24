import numpy as np

def normalize(vec):
    # normalize a vector to a unit length
    return vec / np.linalg.norm(vec)

def fuse_embeddings(text_emb = None, image_emb = None):
    # Handles - text only, image only and text + image
    if text_emb is not None and image_emb is not None:
        emb = 0.6 * np.array(text_emb) + 0.4 * np.array(image_emb)
    elif text_emb is not None:
        emb = np.array(text_emb)
    elif image_emb is not None:
        emb = np.array(image_emb)
    else:
        raise ValueError("No imput provided")
    return normalize(emb)
