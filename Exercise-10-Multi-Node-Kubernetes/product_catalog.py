from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 1200},
        {"id": 2, "name": "Phone", "price": 800},
        {"id": 3, "name": "Headphones", "price": 150}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)