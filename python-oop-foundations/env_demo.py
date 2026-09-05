

from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
app_name = os.getenv("APP_NAME")
debug = os.getenv("DEBUG")

print(f"API Key: {api_key[:10]}...")
print(f"App Name: {app_name}")
print(f"Debug: {debug}")