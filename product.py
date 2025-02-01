import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

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
    driver.get('https://ananinja.dev/sa/en')
    