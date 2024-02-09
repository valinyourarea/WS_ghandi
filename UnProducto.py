from bs4 import BeautifulSoup
import requests
import time


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Accept-Language": "en-MX, en;q=0.9"
}

url = "https://www.gandhi.com.mx/harry-potter-y-la-camara-secreta-ed-minalima"
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

title_element = soup.find('span', class_='base')
title = title_element.text if title_element else None

author_element = soup.find('div', class_='autor')
author = author_element.a.text if author_element else None

editorial_element = soup.find('div', class_='editoriales')
editorial = editorial_element.a.text if editorial_element else None

ISBNn = soup.find('div', class_='isbn').find_all('span')
if len(ISBNn) > 1:
    segundo_span = ISBNn[1].text
    #print(segundo_span)
else:
    print("No se encontró un segundo span.")


cover_element = soup.find('div', class_='product format product-item-format tapa blanda')
cover = cover_element.p.text if cover_element else None

price_element = soup.find('span', class_='price')
price = price_element.text if price_element else None

sip_element = soup.find('div', class_='data item content')
sip = sip_element.text if sip_element else None

pages_element = soup.find('li', {'data-li': 'Número de páginas'}).find('span', class_='attr-data')
pages = pages_element.text

lan_element = soup.find('li', {'data-li': 'Idioma'}).find('span', class_='attr-data')
lan = lan_element.text

date_element = soup.find('li', {'data-li': 'Fecha de publicación'}).find('span', class_='attr-data')
date = date_element.text.strip()

dim_element = soup.find('li', {'data-li': 'Dimensiones'}).find('span', class_='attr-data')
dim = dim_element.text.strip()

img_element = soup.select('div.single-image-product a img')
img = img_element[0].get('data-srclazy')















