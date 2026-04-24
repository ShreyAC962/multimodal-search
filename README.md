## MULTIMODAL SEARCH

Designed and built a production-ready multimodal semantic search system that enables users to retrieve products using both natural language queries and images individually or combined, leveraging CLIP for unified embedding generation.

Implemented a scalable backend using FastAPI and Pinecone to perform high-speed vector similarity search across large product catalogs with efficient indexing and retrieval.

Containerized and deployed the system with Docker and Kubernetes, ensuring reliability, scalability, and real-time performance for large-scale search applications.

Note : We use POST for image search because images are binary files that need to be sent in the request body using multipart form data. GET requests are limited to URL parameters and are not suitable for file uploads.

## Features

- 🔎 Text-to-image search
- 🖼️ Image-to-image search
- 🔀 Hybrid search (text + image)
- ⚡ CLIP-based multimodal embeddings
- 📦 Vector database (Pinecone)
- 🐳 Dockerized services
- ☸️ Kubernetes deployment support

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
│   │
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
pip install torch torchvision fastapi uvicorn pillow pinecone-client transformers python-dotenv

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
<<<<<<< HEAD

=======
>>>>>>> ca3b5fd3f01272d987198126e420eb96e15c59ee


🐳 Run with Docker
1. Build Docker Image
```docker build -t multimodal-search .```
2. Run Container
```docker run -p 8000:8000 --env-file .env multimodal-search```

Run with Docker Compose (Recommended)
```docker-compose up --build```

Stop:
```docker-compose down```


☸️ Kubernetes Deployment
1. Apply Deployment
```kubectl apply -f k8s/deployment.yaml```
2. Expose Service
```kubectl apply -f k8s/service.yaml```


Access API

Once running:

```http://localhost:8000/docs```

Swagger UI will show:

/text-search
/image-search
/hybrid-search

Indexing Data (IMPORTANT STEP)

Before searching, run:

```
python -m scripts.create_index
python -m scripts.index_data
```


## Tech Stack
      Python
      PyTorch
      HuggingFace Transformers (CLIP)
      Pinecone Vector DB
      FastAPI
      Docker
      Kubernetes