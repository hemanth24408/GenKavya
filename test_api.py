
import os
from dotenv import load_dotenv
from google import genai

# Load the API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in .env")
else:
    try:
        client = genai.Client(api_key=api_key)

        print("Testing Gemini API...")

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents="Reply with only the word Hello."
        )

        print("\nAPI test successful!")
        print("Gemini response:", response.text)

    except Exception as error:
        print("\nAPI test failed.")
        print("Error:", error)
