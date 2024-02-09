from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

# Definition of headers to simulate a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Accept-Language": "en-MX, en;q=0.9"
}

url = "https://www.gandhi.com.mx/harry-potter-y-la-orden-del-fenix-edicion-hufflepuff-del-20-aniversario"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

title_element = soup.find('span', class_='base')
title = title_element.text if title_element else None

author_element = soup.find('div', class_='autor')
author = author_element.text if author_element else None

editorial_element = soup.find('div', class_='editoriales')
editorial = editorial_element.text if editorial_element else None

isbn_element = soup.find('div', class_='isbn')
isbn = isbn_element.text if isbn_element else None


img_element = soup.select('div.single-image-product a img')
img = img_element[0].get('data-srclazy')













