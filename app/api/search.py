from fastapi import APIRouter, UploadFile, File
from app.api.services.embedding_service import get_text_embedding, get_image_embedding
from app.api.services.pinecone_service import PineconeService
from app.utils.image_utils import load_image