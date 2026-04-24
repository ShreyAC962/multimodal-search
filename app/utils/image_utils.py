from PIL import Image
import io

MAX_IMAGE_SIZE_MB = 5

def load_image(file):
    try:
        contents = file.read()
        
        if len(contents) == 0:
            raise ValueError("Empty file")
        
        size_mb = len(contents)/(1024*1024)

        if size_mb > MAX_IMAGE_SIZE_MB:
            raise ValueError("Image too large (max 5MB)")
        
        image = Image.open(io.BytesIO(contents))
        # Ensure valid imageS
        image.verify()

        # Convert to RGB (CLIP requirement)
        image = image.convert("RGB")
        image = image.resize((224, 224))

        return image
    
    except Exception as e:
        raise ValueError(f"Invalid image file: {str(e)}")
    