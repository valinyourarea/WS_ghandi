from bs4 import BeautifulSoup
import requests
import json 
import time


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Accept-Language": "en-MX, en;q=0.9"
}

url = "https://www.gandhi.com.mx/harry-potter-y-la-camara-secreta-ed-minalima"
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

#Creacion de una biblioteca 
book_info = {}

#Especificaciones de cada elemento del libro
title_element = soup.find('span', class_='base')
book_info['title'] = title_element.text if title_element else None

author_element = soup.find('div', class_='autor')
book_info['author'] = author_element.a.text if author_element else None

editorial_element = soup.find('div', class_='editoriales')
book_info['editorial'] = editorial_element.a.text if editorial_element else None

ISBNn = soup.find('div', class_='isbn').find_all('span')
if len(ISBNn) > 1:
    book_info['ISBN'] = ISBNn[1].text
    #print(segundo_span)
else:
    book_info['ISNB'] = None


cover_element = soup.find('div', class_='product format product-item-format tapa blanda')
book_info['cover'] = cover_element.p.text if cover_element else None

price_element = soup.find('span', class_='price')
book_info['price'] = price_element.text if price_element else None

sip_element = soup.find('div', class_='data item content')
book_info['synopsis'] = sip_element.text if sip_element else None

pages_element = soup.find('li', {'data-li': 'Número de páginas'}).find('span', class_='attr-data')
book_info['pages'] = pages_element.text

lan_element = soup.find('li', {'data-li': 'Idioma'}).find('span', class_='attr-data')
book_info['language'] = lan_element.text

date_element = soup.find('li', {'data-li': 'Fecha de publicación'}).find('span', class_='attr-data')
book_info['publication_date'] = date_element.text.strip()

dim_element = soup.find('li', {'data-li': 'Dimensiones'}).find('span', class_='attr-data')
book_info['dimensions'] = dim_element.text.strip()

img_element = soup.select('div.single-image-product a img')
book_info['imgen'] = img_element[0].get('data-srclazy')



#Creacion del documento json
with open('book_info.json', 'w') as json_file:
    json.dump(book_info, json_file, indent = 4)

print("Información del libro almacenada en book_info.json")



# Leer el archivo JSON
with open('book_info.json', 'r') as json_file:
    data = json.load(json_file)

# Mostrar el contenido del archivo JSON
print("Contenido del archivo JSON:")
print(json.dumps(data, indent=4))














