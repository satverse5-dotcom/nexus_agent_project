import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("❌ GEMINI_API_KEY not found in .env file")

def check_api_key():
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=api_key
        )
        resp = llm.invoke("Hello Gemini, are you working?")
        print("✅ API key authentication succeeded")
        print(f"   Response: {resp.content[:100]}...")
        return True
    except Exception as e:
        print("❌ API key failed:", e)
        return False

if __name__ == "__main__":
    print("🔍 Testing Gemini API key authentication...")
    check_api_key()
