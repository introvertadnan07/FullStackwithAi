from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="learning_rag",
    vectors_config=VectorParams(
        size=3072,  # IMPORTANT: must match text-embedding-3-large
        distance=Distance.COSINE,
    ),
)

print("Collection created: learning_rag")
