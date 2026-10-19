from flask import Flask, jsonify, request

app = Flask(__name__)
cart = []

@app.route('/cart', methods=['GET', 'POST'])
def shopping_cart():
    if request.method == 'POST':
        item = request.get_json()
        cart.append(item)
        return jsonify(item), 201
    return jsonify(cart)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    