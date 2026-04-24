import torch 
from transformers import CLIProcessor, CLIPModel

class CLIPModelWrapper:
    def __init__(self):
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

    def encode_text(self, text):
        inputs = self.processor(text=[text], return_tensors="pt", padding = True)
        with torch.no_grad():
            embeddings = self.model.get_text_features(**input)
        return embeddings[0].numpy()
    
    def encode_image(self, image):
        inputs = self.processor(images=[image],return_tensors="pt")
        with torch.no_grad():
            embeddings = self.model.get_image_features(**inputs)
        return embeddings[0].numpy()
