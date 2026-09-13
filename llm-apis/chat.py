



from google import genai
from google.genai import types 
from dotenv import load_dotenv 
import os 

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model = "gemini-3.6-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a python tutor, Answer simply"
    )
)

r1 = chat.send_message("what is list?")
print("AI: ", r1.text)

r2 = chat.send_message("Give an example of what you just explained.")
print("\nAI: ", r2.text)



print("\n---streaming---")
response_stream = client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents="Explain python loops in 3 sentences."
)

for chunk in response_stream:
    print(chunk.text, end="", flush=True)
print()