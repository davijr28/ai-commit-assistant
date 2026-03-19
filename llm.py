import os
from dotenv import load_dotenv
from google import genai
from prompts import PROMPT

# Load API key from .env file
load_dotenv()


# Function to initialize Gemini client with the API key
def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)


def generate_commit(diff, language):
    client = get_client()
    if not client:
        return None

    # Use the template from prompts.py
    full_prompt = PROMPT.format(diff=diff, language=language)

    # Note: Ensure the model name is correct for your version (e.g., "gemini-2.5-flash")
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=full_prompt
    )
    return response.text.strip()
