import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

ninjaBaseUrl = 'https://ananinja.dev/sa/en'
pandaBaseUrl = 'https://panda.sa/en'

def getProductName():
    product_api = "http://localhost:5000/product/6281100084013"
    response = requests.get(product_api)
    if response.status_code == 200:
        data = response.json()
        return data['productName']
    else:
        return None
    

def findUrls(productName):
    urls = {
        'ninja': None,
        'panda': None
    }
    
    # Setup Chrome options
    chrome_driver_path = ".\chromedriver.exe"
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get('https://ananinja.dev/sa/en')
    print("page is loading")
    
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    try:
        # Wait up to 10 seconds for the element to be present
        inputbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
    except Exception as e:
        print(f"Error finding or interacting with input element: {e}")
    inputbox.send_keys(productName)
    inputbox.send_keys(Keys.ENTER)
    time.sleep(5);
    try:
        product_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#container-undefined > div.grid > div:nth-child(1) > a"))
        )
        urls['ninja'] = product_link.get_attribute('href')
    except Exception as e:
        print(f"Error finding product link: {e}")
    print(urls['ninja'])
    product_link.click()
    time.sleep(5)
