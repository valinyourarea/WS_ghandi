from bs4 import BeautifulSoup
import requests
import json
import time


class BookScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
            "Accept-Language": "en-MX, en;q=0.9"
        }
        self.book_info = {}

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
        characteristics_dict['pages'] = self._get_text(soup.find('li', {'data-li': 'Número de páginas'}).find('span', class_='attr-data')) if soup.find('li', {'data-li': 'Número de páginas'}) else "No se encontró el elemento 'Número de páginas'"
        characteristics_dict['language'] = self._get_text(soup.find('li', {'data-li': 'Idioma'}).find('span', class_='attr-data')) if soup.find('li', {'data-li': 'Idioma'}) else "No se encontró el elemento 'Idioma'"
        characteristics_dict['publication_date'] = self._get_text(soup.find('li', {'data-li': 'Fecha de publicación'}).find('span', class_='attr-data'), strip=True) if soup.find('li', {'data-li': 'Fecha de publicación'}) else "No se encontró el elemento 'Fecha de publicación'"
        characteristics_dict['dimensions'] = self._get_text(soup.find('li', {'data-li': 'Dimensiones'}).find('span', class_='attr-data'), strip=True) if soup.find('li', {'data-li': 'Dimensiones'}) else "No se encontró el elemento 'Dimensiones'"
        return characteristics_dict

    def _get_image(self, soup):
        img_element = soup.select('div.single-image-product a img')
        return img_element[0].get('data-srclazy') if img_element else None


class JSONWriter:
    def write_to_json(data, file_name):
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Información del libro almacenada en {file_name}")

    def print_json_data(file_name):
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
            print("Contenido del archivo JSON:")
            print(json.dumps(data, indent=4))


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Accept-Language": "en-MX, en;q=0.9"
}

url = "https://www.gandhi.com.mx/derroche-mapa-de-las-lenguas"

start_time = time.time()

book_scraper = BookScraper(url)
book_scraper.scrape_book_info()

json_file_name = 'book_info.json'
JSONWriter.write_to_json(book_scraper.book_info, json_file_name)
JSONWriter.print_json_data(json_file_name)

end_time = time.time()
execution_time = end_time - start_time
print(f"Time of execution: {execution_time} seconds")
