



import chromadb
from google import genai
from dotenv import load_dotenv
import os 


load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# chroma db setup 
db = chromadb.Client()
collection = db.create_collection("knowledge")

def get_embedding(text):
    result = client.models.embed_content(
        model = "gemini-embedding-2",
        contents = text
    )
    return result.embeddings[0].values

documents = [
    "Python is a programming language used for AI and machine learning",
    "Machine learning uses data to train models and make predictions",
    "The Eiffel Tower is located in Paris, France",
    "Neural networks are inspired by the human brain",
    "Football is the most popular sport in the world",
    "Deep learning is a type of machine learning using neural networks"
]

collection.add(
    documents=documents,
    embeddings = [get_embedding(d) for d in documents],
    ids=[f"doc{i}" for i in range(len(documents))]
)

print(f"Stored {collection.count()} documents\n")

# search 
query = "How do Ai systems learn from data?"
query_embedding = get_embedding(query)

results = collection.query(
    query_embeddings = [query_embedding],
    n_results = 2
)

print(f"Query: {query}\n")
print("Top matches:")
for doc in results["documents"][0]:
    print(f"  -> {doc}")