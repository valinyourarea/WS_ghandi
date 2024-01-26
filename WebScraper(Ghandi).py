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
        }

        books.append(book_data)

# Creation of a dictionary with the book information and adding it to the list.
df = pd.DataFrame(books)
# Save the DataFrame in a CSV file named 'books.csv' without including the index
df.to_csv('books.csv', index=False)
# Print the first 10 books on the console
print(df.head(10))

# Establish connection with MySQL (be sure to fill in the correct values)
mysql_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='112233',
    database='proyecto'
)

# Create a cursor
cursor = mysql_connection.cursor()

# Create the table in MySQL (only if it does not exist)
create_table_query = """
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    price VARCHAR(50),
    cover VARCHAR(255)
)
"""
cursor.execute(create_table_query)
mysql_connection.commit()

# Insert data in the table
insert_query = "INSERT INTO books (title, author, price, cover) VALUES (%s, %s, %s, %s)"

for book_data in books:
    data_tuple = (book_data['Title'], book_data['Author'], book_data['Price'], book_data['Cover'])
    cursor.execute(insert_query, data_tuple)

# Commit the changes
mysql_connection.commit()

# Close the connection
cursor.close()
mysql_connection.close()

end_time = time.time()
execution_time = end_time - start_time
print(f"Time of execution: {execution_time} seconds")
        



