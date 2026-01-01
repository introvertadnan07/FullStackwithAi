from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

# OpenAI client (safe at import time)
openai_client = OpenAI()

# Embedding model (safe at import time)
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

def get_vector_db():
    """Lazy Qdrant initialization"""
    return QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333",
        collection_name="learning_rag",
        embedding=embedding_model,
    )

def process_query(query: str) -> str:
    vector_db = get_vector_db()

    search_results = vector_db.similarity_search(query=query, k=3)

    if not search_results:
        return "I could not find relevant information in the document."

    context = "\n\n".join(
        f"Page Content: {r.page_content}\n"
        f"Page Number: {r.metadata.get('page_label')}\n"
        f"File: {r.metadata.get('source')}"
        for r in search_results
    )

    system_prompt = f"""
You are a helpful AI assistant.
Answer the user strictly based on the provided context from a PDF.
Guide the user to the correct page number to read more.

Context:
{context}
""".strip()

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
    )
    
    print(f"{response.choices[0].message.content}")
    return response.choices[0].message.content
