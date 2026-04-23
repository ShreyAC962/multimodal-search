## MULTIMODAL SEARCH

Designed and built a production-ready multimodal semantic search system that enables users to retrieve products using both natural language queries and images, leveraging CLIP for unified embedding generation.

Implemented a scalable backend using FastAPI and Pinecone to perform high-speed vector similarity search across large product catalogs with efficient indexing and retrieval.

Containerized and deployed the system with Docker and Kubernetes, ensuring reliability, scalability, and real-time performance for large-scale search applications.

```
User → FastAPI → CLIP Model → Embedding
                         ↓
                   Pinecone DB
                         ↓
                  Top Similar Results
                         ↓
                      Response
```

### Project Structure

```
multimodal-search/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── search.py
│   │   └── upload.py
│   ├── models/
│   │   └── clip_model.py
│   ├── services/
│   │   ├── embedding_service.py
│   │   └── pinecone_service.py
│   ├── utils/
│   │   └── image_utils.py
│
├── data/
│   └── sample_products.json
│
├── scripts/
│   └── index_data.py
│
├── requirements.txt
├── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── README.md
```

### Setup
```
pip install torch torchvision fastapi uvicorn pillow pinecone-client transformers

```
Also:
Pinecone account
Google Cloud account
Docker
Kubernetes (kubectl)

### Install Dependencies
```
pip install -r requirements.txt
```
