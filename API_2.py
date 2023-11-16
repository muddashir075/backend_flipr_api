from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

customers = []
purchase_orders = []

# API endpoint to add a new purchase order
@app.route('/add_purchase_order', methods=['POST'])
def add_purchase_order():
    data = request.get_json()

    # Generate a unique purchase order ID
    purchase_order_id = str(uuid.uuid4())

    new_purchase_order = {
        'purchase_order_id': purchase_order_id,
        'product_name': data['product_name'],
        'quantity': data['quantity'],
        'pricing': data['pricing'],
        'mrp': data['mrp'],
        'customer_id': data['customer_id']
    }

    purchase_orders.append(new_purchase_order)

    return jsonify({'message': 'Purchase Order added successfully', 'purchase_order_id': purchase_order_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
