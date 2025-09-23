import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# --- Load environment ---
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

if not gemini_key:
    raise RuntimeError("❌ GEMINI_API_KEY not found in .env file")

def get_llm(model_name: str = "gemini-2.5-flash", temperature: float = 0.7):
    """
    Returns a ChatGoogleGenerativeAI LLM instance using GEMINI_API_KEY.
    """
    return ChatGoogleGenerativeAI(
        model=model_name,
        temperature=temperature,
        google_api_key=gemini_key   # ✅ Explicitly use your API key
    )

def get_gemini_response(prompt: str, model_name: str = "gemini-2.5-flash") -> str:
    """
    Send a prompt to Gemini and return the response text.
    """
    llm = get_llm(model_name=model_name)
    response = llm.invoke(prompt)
    return response.content
