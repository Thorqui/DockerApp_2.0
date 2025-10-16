from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # permite peticiones desde Nginx

@app.route('/')
def home():
    return "<h1>👋 Hola desde Flask Backend!</h1><p>Servidor corriendo dentro de un contenedor Docker.</p>"

@app.route('/api/saludo')
def saludo():
    return jsonify({"mensaje": "Hola desde la API Flask (dentro de Docker)!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
