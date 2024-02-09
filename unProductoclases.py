from bs4 import BeautifulSoup
import requests
import time


class BookScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
            "Accept-Language": "en-MX, en;q=0.9"
        }

    def _find_element_text(self, tag, attrs):
        element = self.soup.find(tag, attrs)
        return element.text.strip() if element else None

    def scrape_book_info(self):
        response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(response.content, 'html.parser')

        title_element = self.soup.find('span', class_='base')
        title = title_element.text.strip() if title_element else None

        author_element = self.soup.find('div', class_='autor')
        author = author_element.a.text.strip() if author_element else None

        editorial_element = self.soup.find('div', class_='editoriales')
        editorial = editorial_element.a.text.strip() if editorial_element else None

        isbn_elements = self.soup.find('div', class_='isbn').find_all('span')
        isbn = isbn_elements[0].text.strip() if isbn_elements else None

        cover_element = self.soup.find('div', class_='product format product-item-format tapa blanda')
        cover = cover_element.p.text.strip() if cover_element else None

        price_element = self.soup.find('span', class_='price')
        price = price_element.text.strip() if price_element else None

        sip_element = self.soup.find('div', class_='data item content')
        sip = sip_element.text.strip() if sip_element else None

        pages_element = self._find_element_text('li', {'data-li': 'Número de páginas'})
        pages = pages_element.split(':')[-1].strip() if pages_element else None

        lan_element = self._find_element_text('li', {'data-li': 'Idioma'})
        lan = lan_element.split(':')[-1].strip() if lan_element else None

        date_element = self._find_element_text('li', {'data-li': 'Fecha de publicación'})
        date = date_element.split(':')[-1].strip() if date_element else None

        dim_element = self._find_element_text('li', {'data-li': 'Dimensiones'})
        dim = dim_element.split(':')[-1].strip() if dim_element else None

        img_element = self.soup.select('div.single-image-product a img')
        img = img_element[0].get('data-srclazy')

        return {
            'title': title,
            'author': author,
            'editorial': editorial,
            'isbn': isbn,
            'cover': cover,
            'price': price,
            'sip': sip,
            'pages': pages,
            'language': lan,
            'publication_date': date,
            'dimensions': dim,
            'image': img
        }

url = "https://www.gandhi.com.mx/harry-potter-y-la-camara-secreta-ed-minalima"
scraper = BookScraper(url)
book_info = scraper.scrape_book_info()
print(book_info)
