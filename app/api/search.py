from fastapi import APIRouter, UploadFile, File
from app.api.services.embedding_service import get_text_embedding, get_image_embedding
from app.api.services.pinecone_service import PineconeService
from app.utils.image_utils import load_image

router = APIRouter()
pinecone_service = PineconeService()

@router.get("/text-search")
def text_search(query : str):
    embedding = get_text_embedding(query)
    results = pinecone_service.query(embedding)
    return results


@router.post("/image-search")
async def image_search(file : UploadFile):
    image = load_image(file.file)
    embedding = get_image_embedding(image)
    results = pinecone_service.query(embedding)
    return {
        "embedding_dim" : len(embedding),
        "results" : results
    }


