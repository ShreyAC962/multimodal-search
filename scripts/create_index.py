import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=api_key)

index_name = os.getenv("PINECONE_INDEX")

# delete if exists (safe dev reset)
if index_name in pc.list_indexes().names():
    pc.delete_index(index_name)

# create index
pc.create_index(
    name=index_name,
    dimension=512,  
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region=os.getenv("PINECONE_ENV")
    )
)

print("Pinecone index created successfully")