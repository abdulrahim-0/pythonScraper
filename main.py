from scrape import scrape_website, extract_body_content, clean_body_content, get_price_from_content
from product import getProductName , findUrls
def main():
    urls = findUrls("shampo sanslik")
    # print(getProductName());
    # print("Scraping webpage...")
    # html_content = scrape_website(url)
    # body_content = extract_body_content(html_content)
    # cleaned_content = clean_body_content(body_content)
    
    # print("Extracting price using AI...")
    # price = get_price_from_content(cleaned_content)
    # print(f"Found price: {price}")

if __name__ == "__main__":
    main()