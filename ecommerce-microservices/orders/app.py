from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

orders = [
    {
        "id": "order-001",
        "user_id": 1,
        "items": [
            {"product_id": 1, "quantity": 1, "price": 999.99},
        ],
        "total": 999.99,
        "status": "delivered",
        "created_at": "2024-12-13T10:00:00"
    },
    {
        "id": "order-002",
        "user_id": 1,
        "items": [
            {"product_id": 2, "quantity": 2, "price": 499.99},
        ],
        "total": 999.98,
        "status": "processing",
        "created_at": "2024-12-14T09:30:00"
    },
]

@app.route('/', methods=['GET'])
def get_orders():
    return jsonify({
        "status": "ok",
        "data": orders
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "orders",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9002)