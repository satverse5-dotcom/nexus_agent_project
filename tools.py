import os
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()
tavily_api_key = os.getenv("TAVILY_API_KEY")

if not tavily_api_key:
    raise RuntimeError("❌ TAVILY_API_KEY not found in .env file")

# --- LangChain + Tavily ---
from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

# --- Selenium ---
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ✅ Tavily Search Tool
tavily_search = TavilySearchResults(
    max_results=5,
    api_key=tavily_api_key
)

# ✅ Selenium Driver Helper
def get_driver():
    """Return a headless Chrome WebDriver instance."""
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # modern headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

# ✅ Selenium Web Scraper Tool
@tool
def selenium_web_scraper(url: str) -> str:
    """
    Scrapes the first 4000 characters of visible text from a webpage.
    """
    driver = None
    try:
        driver = get_driver()
        driver.get(url)

        # Wait until <body> is present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        page_text = driver.find_element(By.TAG_NAME, "body").text
        return page_text[:4000]

    except Exception as e:
        return f"❌ Error scraping {url}: {e}"

    finally:
        if driver:
            driver.quit()

# ✅ Toolkit for Agent
tool_kit = [tavily_search, selenium_web_scraper]
