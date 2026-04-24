import os
from dotenv import load_dotenv
from pinecone import Pinecone


load_dotenv()


class PineconeService:
    def __init__(self):
        api_key = os.getenv("PINECONE_API_KEY")
        env = os.getenv("PINECONE_ENV")
        index_name = os.getenv("PINECONE_INDEX")

        if not api_key:
            raise ValueError("PINECONE_API_KEY not found in environment")

        self.pc = Pinecone(api_key=api_key)
        self.index = self.pc.Index(index_name)
    
    def upsert(self, vectors):
        self.index.upsert(vectors=vectors)

    def query(self, vector, top_k=5):
        response = self.index.query(
            vector=vector.tolist(),
            top_k=top_k,
            include_metadata=True
        )
        # Convert to pure json
        results = []
        for match in response["matches"]:
            results.append({
                "id": match["id"],
                "score": float(match["score"]),
                "metadata": match.get("metadata", {})
            })
        return {
            "results" : results
        }