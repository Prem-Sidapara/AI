

import chromadb
from google import genai
from dotenv import load_dotenv
import os 

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# chroma db setup 
db = chromadb.Client()
collection = db.create_collection("company_knowledge")

def get_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=text
    )
    return result.embeddings[0].values


# knowledge base
knowledge = [
    "TechNova's office timings are 10:00 AM to 6:00 PM Monday to Friday.",
    "Employees get 20 days of paid annual leave per calendar year at TechNova.",
    "The Wi-Fi network for guests at TechNova is 'TN-Guest' and password is 'TechNova@2026'.",
    "TechNova reimburses up to ₹3,000 per month for home internet expenses.",
    "The IT support desk can be reached at extension 404 or support@technova.internal."
]

print("Storing documents in Vector BD...")

collection.add(
    documents=knowledge,
    embeddings=[get_embedding(doc) for doc in knowledge],
    ids = [f"id_{i}" for i in range(len(knowledge))]
)

print(f"✅ Stored {collection.count()} documents.\n")

# RAG qurey function 
def ask_rag(question: str)-> str:

    # Step A: retrive relevant context
    q_embed = get_embedding(question)
    result = collection.query(
        query_embeddings= [q_embed],
        n_results=2
    )
    retrived_docs = result["documents"][0]
    context = "\n".join(retrived_docs)

    print(f"--- retireved context ---")
    for doc in retrived_docs:
        print(f"- {doc}")
    print("----------------------------\n")

    # step B: augmented prompt 
    prompt = f"""You are an internal assistant. Answer the user 
question strictly using the provided context. If the answer cannot 
be found in the context, say "I don't have that information."

Context:
{context}

Question:
{question}
"""
    
    # step C: generation
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )
    return response.text

# test 
question = "how much internet bill can i claim per month?"
print(f"Question: {question}\n")
answer = ask_rag(question)
print(f"Answer: \n{answer}")