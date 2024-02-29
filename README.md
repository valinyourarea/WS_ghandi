# **WS_ghandi**

# Introduction
This code is a web scraper that extracts information about a book from Ghandi by providing a link and returns it in JSON format. It utilizes the BeautifulSoup, json, requests, asyncio, and aiohttp libraries. This code is capable of retrieving vital information such as product names, prices, descriptions, and discounts. Additionally, it offers a list of links to product images. To evaluate this extraction tool, Docker is used to manage the environment, and Postman is employed to conduct comprehensive tests of the Scraper.

# What is Ghandi?
Gandhi Bookstores was founded in June 1971. The original store measured about 150 m2 and was located at Miguel Ángel de Quevedo 128, in the southern part of Mexico City. Although small, the bookstore had its café on the mezzanine, where the first cultural activities (film screenings, theater, music, etc.) were also held, which became a characteristic of Gandhi in the subsequent years.
Today, Gandhi Bookstores has a presence in Mexico City and in several states across the Mexican Republic, (See bookstores), as well as Gandhi Bookstores in Palacio de Hierro and Walmart Supercenters. Together, Gandhi's staff, suppliers, and customers have made our company the most important chain of professional bookstores in Mexico, and surely one of the most significant in Latin America. In addition to having a website where you can purchase thousands of books from the comfort of your home.

# Requirements
- GitHub
- Bash (Windows)
- Docker (Windows) or Docker Compose (Linux)
- Postman

# Installation
**Windows** 
- [GitHub](https://github.com/)
- [Git Bash (Windows)](https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/git-bash/#:~:text=Git%20Bash%3A%20instalaci%C3%B3n%20paso%20a%20paso%201%20Primero%2C,La%20configuraci%C3%B3n%20por%20defecto%20suele%20ser%20adecuada.%20)
- [Docker](https://www.docker.com/get-started/)
- [Postman](https://drive.google.com/file/d/1LrQHQGQEd-zbskE5vLpU46Yx-8I0mGk5/view?usp=sharing)
  

**Linux**

- **GitHub**

Debian/Ubuntu
  
```sudo apt-get update```

```sudo apt-get install git```

Fedora

  ```sudo dnf install git```

Arch

  ```sudo pacman -S git```

- **Docker**
  
Debian/Ubuntu

```sudo apt-get update```

```sudo apt-get install docker.io```

```sudo apt-get install docker-compose```

Fedora

```sudo dnf install docker```

```sudo dnf install docker-compose```

Arch

```sudo pacman -S docker```

```yay -S docker-compose```

- [Postman](https://drive.google.com/file/d/1LrQHQGQEd-zbskE5vLpU46Yx-8I0mGk5/view?usp=sharing)

# How to Use The Code?

To use WS_Ghandi code, first:
**Code Description**
This code is a web scraper that extracts information about a book from a webpage and returns it in JSON format. It utilizes the BeautifulSoup, json, requests, asyncio, and aiohttp libraries.

**Requirements**

To run this code, you'll need to have the following Python libraries installed:

**beautifulsoup4**: You can install it using:

```pip install beautifulsoup4```

**aiohttp**: You can install it using:

```pip install aiohttp```

Now: 

1. move to your work space in your GIT BASH or teminal and clone the repository.

```https://github.com/valinyourarea/WS_ghandi.git```

2. Once you have the repository cloned, open the repository.

```cd ws_ghandi```

3. Now,go to put it in docker.
   
```docker compose build```

4. Run our container.

```docker compose up```

[Click here to see the example](https://drive.google.com/file/d/1Hzblw5jUKHsrivb0vVIlzvEUyB04km9n/view?usp=sharing)


5. Copy the first link and paste it in Postman with/scraper, select body and there click "raw", and you will put the JSON option (Is in blue) with the link of the Ghandi product like this image.
    
   [click here to see the example](https://drive.google.com/file/d/1xl4SSBrH7r5aiNC0xwXZj9wW2DQtmXV8/view?usp=sharing)

6. Check that the type of method in Postman is set as POST. After all that, give a click in SEND.
7. It is done. To exit, execute this:
   
```ctrl c```

```docker compose down```

```exit```

# How Was It Developed?
Here's a file with some of what was used to develop the main code, both libraries and flask are there better explained
[Click here](https://drive.google.com/file/d/17rXBThsKwtgwNPyDDwPFMcbYW4r2TYpe/view?usp=sharing)

# Future Developments
- Add support for scraping all products with a given name.
- Implement webdriver for problems when loading the page.

# Considerations

- This project currently usually does not load the description correctly in some Mercado Libre links since to be more precise it is necessary to use a webdriver due to the structure of the page.

# Collaborators

- Valeria Paredes
- Damaris Pech
- Daniel Herrera
- Isaias Lopez
- Jonathan Velasco



