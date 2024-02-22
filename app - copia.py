from flask import Flask, request, jsonify
from calculadora import *

app = Flask(__name__)

# Endpoint raíz que devuelve un mensaje de bienvenida
@app.route('/', methods=['GET'])
def welcome():
    return "Bienvenido al servidor de prueba!"

# Endpoint que acepta datos en formato JSON y devuelve una confirmación
@app.route('/suma', methods=['POST'])
def sume():
    data= request.json
    r= Calculadora(data["a"], data["b"]).sumar()
    return jsonify({'messege': 'Datos recibidos','result': r})

# Endpoint que devuelve el estado del servidor
@app.route('/status', methods=['GET'])
def server_status():
    return jsonify({'status': 'Activo'})

if __name__ == '__main__':
    app.run(port=6000,debug=True)  # Inicia el servidor en modo de depuración
