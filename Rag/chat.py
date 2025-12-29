from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

openai_client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model,
)

# Take User Input 
user_query = input("Ask something: ")

# Relevant chunks from the vector db
search_result = vector_db.similarity_search(query=user_query, k=3)

context = "\n\n".join([
    f"Page Content: {r.page_content}\n"
    f"Page Number: {r.metadata.get('page_label')}\n"
    f"File: {r.metadata.get('source')}"
    for r in search_result
])

SYSTEM_PROMPT = f"""
You are a helpful AI assistant.
Answer the user strictly based on the provided context from a PDF.
Guide the user to the correct page number to read more.

Context:
{context}
"""

response = openai_client.chat.completions.create(
    model="chatgpt-4o-latest",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]
)

print(f"🤖: {response.choices[0].message.content}")
