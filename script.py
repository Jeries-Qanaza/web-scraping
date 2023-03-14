from bs4 import BeautifulSoup
import requests

def getHTMLdocument(url):
      
    # request for HTML document of given url
    response = requests.get(url)
      
    # response will be provided in JSON format
    return response.text

url_to_scrape = "https://jeries-qanaza.github.io/sdb-cards/"
html_document = getHTMLdocument(url_to_scrape)

soup = BeautifulSoup(html_document, 'html.parser')

print(soup.prettify())
