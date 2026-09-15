


from google import genai
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=text
    )
    return np.array(result.embeddings[0].values)


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

texts = ["car", "automobile", "vehicle", "apple", "mango"]
embeddings = [get_embedding(t) for t in texts]

print(f"Embedding size: {len(embeddings[0])} numbers\n")


for i in range(1, len(texts)):
    score = cosine_similarity(embeddings[0], embeddings[i])
    print(f"car - {texts[i]:<12} similarity: {score:.3f}")
