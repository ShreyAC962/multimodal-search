from app.models.clip_model import CLIPModelWrapper

clip = CLIPModelWrapper()

def get_text_embedding(text):
    emb = clip.encode_text(text)
    return emb.flatten().astype("float32")

def get_image_embedding(image):
    emb = clip.encode_image(image)
    return emb.flatten().astype("float32")