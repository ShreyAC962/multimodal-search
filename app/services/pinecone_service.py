import os
from pinecone import Pinecone

class PineconeService:
    def __init__(self):

        self.pc = Pinecone(
            api_key=os.getenv("PINECONE_API_KEY")
        )

        self.index = self.pc.Index(os.getenv("PINECONE_INDEX"))

    def upsert(self, vectors):
        self.index.upsert(vectors=vectors)

    def query(self, vector, top_k=5):
        return self.index.query(
            vector=vector.tolist(),
            top_k=top_k,
            include_metadata=True
        )