import pinecone
import os
from dotenv import load_dotenv

load_dotenv()



class PineconeService:
    def __init__(self):
        pinecone.init(
            api_key = os.getenv("PINECONE_API_KEY"),
            environment = os.getenv("PINECONE_ENV")
        )
        self.index = pinecone.Index(os.getenv("PINECONE_INDEX"))
    
    def upsert(self, vectors):
        self.index.upsert(vectors = vectors)

    def query(self, vector, top_k = 5):
        return self.index.query(vector=vector.tolist(), top_k= top_k, include_metadata=True)
