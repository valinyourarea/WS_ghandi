from bs4 import BeautifulSoup
import requests
import json


#class principal
class BookScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Accept-Language": "en-MX, en;q=0.9"
}
        self.book_info = {}

    #metodos de los elementos del libro
    def scrape_book_info(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.book_info['title'] = self._get_title(soup)
        self.book_info['author'] = self._get_author(soup)
        self.book_info['editorial'] = self._get_editorial(soup)
        self.book_info['ISBN'] = self._get_ISBN(soup.find('div', class_='isbn'))
        self.book_info['cover'] = self._get_cover(soup)
        self.book_info['price'] = self._get_price(soup)
        self.book_info['synopsis'] = self._get_synopsis(soup)
        self.book_info.update(self._get_characteristics(soup))
        self.book_info['image'] = self._get_image(soup)

    #Este metodo permite eliminar espacios en blanco del texto
    def _get_text(self, element, strip=False):
        return element.text.strip() if element else None if strip else None

    def _get_title(self, soup):
        return self._get_text(soup.find('span', class_='base'))

    def _get_author(self, soup):
        return self._get_text(soup.find('div', class_='autor').a)

    def _get_editorial(self, soup):
        return self._get_text(soup.find('div', class_='editoriales').a)

    def _get_ISBN(self, isbn_element):
        if isbn_element:
            spans = isbn_element.find_all('span')
            return spans[1].text if len(spans) > 1 else None
        return None

    def _get_cover(self, soup):
        return self._get_text(soup.find('div', class_='product-item-format'))

    def _get_price(self, soup):
        return self._get_text(soup.find('span', class_='price'))

    def _get_synopsis(self, soup):
        return self._get_text(soup.find('div', class_='data item content'))

    def _get_characteristics(self, soup):
        characteristics_dict = {}
        characteristics_dict['pages'] = self._get_text(soup.find('li', {'data-li': 'Número de páginas'}).find('span', class_='attr-data'))
        characteristics_dict['language'] = self._get_text(soup.find('li', {'data-li': 'Idioma'}).find('span', class_='attr-data'))
        characteristics_dict['publication_date'] = self._get_text(soup.find('li', {'data-li': 'Fecha de publicación'}).find('span', class_='attr-data'), strip=True)
        characteristics_dict['dimensions'] = self._get_text(soup.find('li', {'data-li': 'Dimensiones'}).find('span', class_='attr-data'), strip=True)
        return characteristics_dict

    def _get_image(self, soup):
        img_element = soup.select('div.single-image-product a img')
        return img_element[0].get('data-srclazy') if img_element else None

#clase nueva donde se crea el documento json
class JSONWriter:
    @staticmethod
    def write_to_json(data, file_name):
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Información del libro almacenada en {file_name}")


# Uso de las clases
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Accept-Language": "en-MX, en;q=0.9"
}

url = "https://www.gandhi.com.mx/harry-potter-y-la-camara-secreta-ed-minalima"

book_scraper = BookScraper(url)
book_scraper.scrape_book_info()

JSONWriter.write_to_json(book_scraper.book_info, 'book_info.json')

# Leer el archivo JSON
with open('book_info.json', 'r') as json_file:
    data = json.load(json_file)

# Mostrar el contenido del archivo JSON
print("Contenido del archivo JSON:")
print(json.dumps(data, indent=4))
