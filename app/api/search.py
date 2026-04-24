from fastapi import APIRouter, UploadFile, File, Form
from PIL import Image
from io import BytesIO

from app.services.embedding_service import get_text_embedding, get_image_embedding
from app.services.pinecone_service import PineconeService
from app.utils.image_utils import load_image
from app.utils.fusion import fuse_embeddings

router = APIRouter()
pinecone_service = PineconeService()


# TEXT ONLY SEARCH
@router.get("/text-search")
def text_search(query : str):
    text_emb = get_text_embedding(query)
    final_emb = fuse_embeddings(text_emb=text_emb)
    results = pinecone_service.query(final_emb)
    return results

# IMAGE ONLY SEARCH
@router.post("/image-search")
async def image_search(file : UploadFile = File(...)):
    image = load_image(file.file)
    image_emb = get_image_embedding(image)
    final_emb = fuse_embeddings(image_emb=image_emb)
    results = pinecone_service.query(final_emb)
    return results


# TEXT + IMAGE SEARCH (HYBRID)
@router.post("/hybrid-search")
async def hybrid_search(
    query: str = Form(None),
    file: UploadFile = File(None)
):
    text_emb = None
    image_emb = None

    if query:
        text_emb = get_text_embedding(query)
    if file:
        image = load_image(file.file)
        image_emb = get_image_embedding(image)
    
    final_emb = fuse_embeddings(text_emb, image_emb)

    results = pinecone_service.query(final_emb)

    return results


