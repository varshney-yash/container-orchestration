from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "Palmer",
        "email": "palmer@example.com",
        "address": "123 Tech Lane",
        "orders": ["order-001", "order-002"]
    },
    {
        "id": 2,
        "name": "Alex Smith",
        "email": "alex@example.com",
        "address": "456 Data Drive",
        "orders": ["order-003"]
    },
    {
        "id": 3,
        "name": "Jordan Lee",
        "email": "jordan@example.com",
        "address": "789 Cloud Court",
        "orders": [] 
    }
]

@app.route('/', methods=['GET'])
def get_users():
    return jsonify({
        "status": "ok",
        "data": users
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "users",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9003)