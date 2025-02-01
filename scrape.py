import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time 
from bs4 import BeautifulSoup
import ollama

def scrape_website(website):
    print("launching browser")

    chrome_driver_path = ".\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(website)
        print("page is loading")
        html = driver.page_source
        return html
    finally:
        driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content,max_length=6000):
    return [
        dom_content[i : i  + max_length] for i in range(0, len(dom_content ), max_length)
    ]

def get_price_from_content(content):
    prompt = f"""You are a helpful AI assistant that extracts product prices from web content.
    Given the following webpage content, find and return ONLY the main product price.
    Return just the price with its currency symbol (like 99.99 or 50.00).
    If you can't find a price, return "Price not found".
    
    Content:
    {content[:10000]}  # Limiting content length to avoid token limits
    
    Price:"""
    
    response = ollama.chat(model='gemma2:27b', messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ])
    
    return response['message']['content'].strip()