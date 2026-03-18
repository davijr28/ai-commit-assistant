import os
from dotenv import load_dotenv
from google import genai
from prompts import PROMPT

# Load API key from .env file
load_dotenv()

# Initialize the Gemini client with the API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_commit(diff, language):
    # Use the template from prompts.py
    full_prompt = PROMPT.format(diff=diff, language=language)

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=full_prompt
    )
    return response.text.strip()
