
import requests
from bs4 import BeautifulSoup

REQ = requests.get('https://pythonhow.com/example.html')
SOUP = BeautifulSoup(REQ.content, 'html.parser')
print(SOUP, "\n")

CITIES = SOUP.find_all('div', {'class': 'cities'})
for ITEM in CITIES:
    print(ITEM.find_all('h2')[0].text, ':', ITEM.find_all('p')[0].text)
