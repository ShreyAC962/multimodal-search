import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

class PineconeService:

    def __init__(self):
        api_key = os.getenv("PINECONE_API_KEY")
        index_name = os.getenv("PINECONE_INDEX")

        if not api_key:
            raise ValueError("Missing PINECONE_API_KEY")

        self.pc = Pinecone(api_key=api_key)
        self.index = self.pc.Index(index_name)

    def upsert(self, vectors):
        # safety check
        if not vectors:
            raise ValueError("No vectors to upsert")

        self.index.upsert(vectors=vectors)

    def query(self, vector, top_k=5):

        response = self.index.query(
            vector=vector.tolist(),
            top_k=top_k,
            include_metadata=True
        )

        results = []
        for match in response.matches:
            results.append({
                "id": match.id,
                "score": float(match.score),
                "metadata": match.metadata
            })

        return {"results": results}