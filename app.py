from flask import Flask, request, jsonify
from scraper import *
import asyncio

app = Flask(__name__)

# Endpoint raíz que devuelve un mensaje de bienvenida
@app.route('/', methods=['GET'])
def welcome():
    return "Bienvenido al servidor de prueba!"

# Endpoint que acepta datos en formato JSON y devuelve una confirmación
@app.route('/scraper', methods=['POST'])
async def exe_scraper():
    data = request.json
    
    # Crear una instancia de la clase BookScraper
    scraper = BookScraper(data["url"])

    # Realizar el scraping de los datos del libro
    await scraper.scraper_book()

    # Obtener todos los elementos del libro
    book_elements = await scraper.all_elements()

    return jsonify({'message': 'Datos recibidos', 'result': book_elements})

# Endpoint que devuelve el estado del servidor
@app.route('/status', methods=['GET'])
def server_status():
    return jsonify({'status': 'Activo'})

if __name__ == '__main__':
    app.run(port=6000, debug=True)  # Inicia el servidor en modo de depuración
