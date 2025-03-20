import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("LANGCHAIN_API_KEY")
if not api_key:
    print("API key is not loaded properly.")
else:
    print(f"API Key Loaded: {api_key[:5]}...")  # Print the first 5 characters for confirmation
