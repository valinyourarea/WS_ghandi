from bs4 import BeautifulSoup # Sirve para extraccion de datos 
import json # Convierte a un documento tipo json
import requests # Descarga del html de los datos 
import asyncio # Sirve para hacer peticiones asincronicas
import aiohttp # Sirve para hacer solicitudes HTTP como requests pero de forma asincrona

#Main class
from bs4 import BeautifulSoup
import json
import asyncio
import aiohttp

class BookScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.title_e = None
        self.authors = None
        self.editorial_n = None
        self.isbn_c = None
        self.cover_e = None
        self.prices = None
        self.syp = None
        self.charact = None
        self.img = None

    #Se hace el scraper de nuestro libro de forma asincrona 
    async def scraper_book(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
                        "Accept-Language": "en-MX, en;q=0.9"}

        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers=self.headers) as response:
                if response.status != 200: 
                    raise Exception(f"GET request to {self.url} returned status code {response.status}")
                
                text = await response.text()
                self.soup = BeautifulSoup(text, 'html.parser')

    async def name(self):
        title_element = self.soup.find('span', class_='base')
        if title_element:
            self.title_e = title_element.text.strip()
        else:
            print("No title element found")
          
    async def author(self):
        author_element = self.soup.find('div', class_='autor')
        if author_element:
            author_link = author_element.a
            if author_link:
               self.authors = author_link.text.strip()
            else:
                print("No 'a' element found within author div")
        else:
             print("No author div element found")

    async def editorial(self):
        editorial_element = self.soup.find('div', class_='editoriales')
        if editorial_element:
            editorial_link = editorial_element.a
            if editorial_link:
                self.editorial_n = editorial_link.text.strip()
            else:
                print("No editorial element found")

    async def ISBN(self):
        isbn_element = self.soup.find('div', class_='isbn')
        isbn2 = isbn_element.find_all('span')
        if len(isbn2) > 1:
            self.isbn_c = isbn2[1].text.strip()
        else:
            print("No se encontró un segundo span.")
        
        
    async def cover(self):
        cover_element = self.soup.find('div', class_='product-item-format')
        if cover_element:
            self.cover_e = cover_element.text.strip()
        else:
            print("No cover element found")

    async def price(self):
        price_element = self.soup.find('span', class_='price')
        if price_element:
            self.prices = price_element.text.strip()
        else:
            print("No price element found")

    async def synopsis(self):
        synopsis_element = self.soup.find('div', class_='data item content')
        if synopsis_element:
            self.syp = synopsis_element.text.strip()
        else:
            print("No synopsis element found")
    

    async def characteristics(self):
        characters_list = []
        pages_element = self.soup.find('li', {'data-li': 'Número de páginas'})
        if pages_element:
             characters_list.append(('pages', pages_element.find('span', class_='attr-data').text.strip()))
        else:
            print("No pages element found")
        
        publication_date_element = self.soup.find('li', {'data-li': 'Fecha de publicación'})
        if publication_date_element:
             characters_list.append(('publication_date', publication_date_element.find('span', class_='attr-data').text.strip()))
        else:
            print("No publication date element found")
        
        language_element = self.soup.find('li', {'data-li': 'Idioma'})
        if language_element:
             characters_list.append(('language', language_element.find('span', class_='attr-data').text.strip()))
        else:
            print("No language element found")
        
        dimensions_element = self.soup.find('li', {'data-li': 'Dimensiones'})
        if dimensions_element:
            characters_list.append(('dimensions', dimensions_element.find('span', class_='attr-data').text.strip()))
        else:
            print("No dimensions element found")
        
        self.charact = characters_list


    
    async def image_cover(self):
         img_element = self.soup.select('div.single-image-product a img')
         if img_element:
           self.img = img_element[0].get('data-srclazy')
         else:
             print("No image element found")


    async def all_elements(self):
        await self.name()
        await self.author()
        await self.editorial()
        await self.ISBN()
        await self.cover()
        await self.price()
        await self.synopsis()
        await self.characteristics()
        await self.image_cover()
        attributes = {
            'name': self.title_e,
            'author': self.authors,
            'editorial': self.editorial_n,
            'ISBN': self.isbn_c,
            'cover': self.cover_e,
            'price': self.prices,
           'synopsis': self.syp,
            'characteristics': self.charact,
            'image_cover': self.img
        }
        return json.dumps(attributes, ensure_ascii=False, indent= 2) 



# Creamos una instancia de la clase
scraper = BookScraper('https://www.gandhi.com.mx/gabriel-garcia-marquez-11')

# Ejecutar los métodos en el bucle de eventos
asyncio.run(scraper.scraper_book())
print(asyncio.run(scraper.all_elements()))
