from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99},
]

@app.route('/', methods=['GET'])
def get_products():
    return jsonify({
        "status": "ok",
        "data": products
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "products",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
