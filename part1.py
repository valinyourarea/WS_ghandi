from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Configura las opciones para Chrome en modo headless
chrome_options = Options()
# Descomenta las siguientes líneas si deseas ejecutar en modo headless
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# Inicializa el driver de Selenium con el ChromeDriver administrado por webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navega a la página
driver.get("https://best.aliexpress.com/?gatewayAdapt=glo2esp&browser_redirect=true")

# Lista de palabras clave
palabras_clave = ['smartphone', 'laptop', 'camera', 'headphones', 'watch']

# Lista para almacenar las URL
urls = []

# Bucle para buscar cada palabra y obtener la URL correspondiente
for palabra in palabras_clave:
    # Encontrar el campo de búsqueda y escribir la palabra
    search_box = driver.find_element("id", "search-words")
    search_box.clear()
    search_box.send_keys(palabra)
    search_box.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)

    # Obtener la URL de la página actual y agregarla a la lista
    url_resultado = driver.current_url
    urls.append(url_resultado)

    print(f"La URL para la palabra '{palabra}' es: {url_resultado}")

# Imprimir la lista de URL
print("Lista de URL:")
for url in urls:
    print(url)

# Cierra el navegador
driver.quit()
