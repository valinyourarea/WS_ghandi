# Import of required libraries
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import mysql.connector
import time
start_time = time.time()



# Definition of headers to simulate a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Accept-Language": "en-MX, en;q=0.9"
}

# Definition of the search string and the list for storing books
search_query = 'Harry'
books=[]

# Main loop to iterate through 10 pages of results
for page in range(1,20):
    # Construction of the search URL with page number and search string
    search_url = f"https://www.gandhi.com.mx/catalogsearch/result/index/?p={page}&q={search_query}"
    # Performing the GET request to the search URL with the headers defined
    response = requests.get(search_url,headers=headers)
    # Parsing of HTML page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extraction of HTML elements containing information about books
    products = soup.find_all("div",class_="product details product-item-details new-list-jj")

    # Iteration through the books found on the site
    for product in products:
        url_product = product.find('a', class_='product-item-link')
        link = url_product['href'] if url_product else None
        title_element = product.find('strong', class_='product name product-item-name')
        title = title_element.text if title_element else None
        author_element = product.find('div', class_='autor')
        author = author_element.text if author_element else None
        price_element = product.find('span', class_='price')
        price = price_element.text if price_element else None
        cover_element = product.find('p', class_='product-item-link')
        cover = cover_element.text if cover_element else None
        book_data = {
            'Title': title,
            'Author': author,
            'Price': price,
            "Cover": cover,
            "Link": link,
        }

        books.append(book_data)

        print(book_data)


img_element = soup.select('div.single-image-product a img')
#img = img_element[0]['src'] if img_element else None