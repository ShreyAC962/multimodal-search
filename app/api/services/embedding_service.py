from app.models.clip_model import CLIPModelWrapper

clip = CLIPModelWrapper()

def get_text_embedding(text):
    return clip.encode_text(text)

def get_image_embedding(image):
    return clip.encode_image(image)