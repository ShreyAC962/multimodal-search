import torch
from transformers import CLIPProcessor, CLIPModel

class CLIPModelWrapper:

    def __init__(self):
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        self.model.eval()

    def encode_text(self, text):
        inputs = self.processor(
            text=[text],
            return_tensors="pt",
            padding=True
        )

        with torch.no_grad():
            outputs = self.model.get_text_features(**inputs)

        return outputs[0].cpu().numpy()

    def encode_image(self, image):
        inputs = self.processor(
            images=image,
            return_tensors="pt"
        )

        with torch.no_grad():
            outputs = self.model.get_image_features(**inputs)

        return outputs[0].cpu().numpy()