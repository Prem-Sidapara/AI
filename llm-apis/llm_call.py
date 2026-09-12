
from google import genai
from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv()

# API key setup
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# LLM call
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain machine learning in 2 sentences."
)

respone2 = client.models.generate_content(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a sarcastic assistant who answer exactly 1 sentence with emojis."
    ),
    contents="what is machine learning?"
)

# print(response.text)
print(respone2.text)