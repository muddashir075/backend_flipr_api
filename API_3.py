from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

customers = []
purchase_orders = []
shipping_details = []

# API endpoint to add shipping details
@app.route('/add_shipping_details', methods=['POST'])
def add_shipping_details():
    data = request.get_json()

    # Generate a unique shipping details ID
    shipping_details_id = str(uuid.uuid4())

    new_shipping_details = {
        'shipping_details_id': shipping_details_id,
        'address': data['address'],
        'city': data['city'],
        'pincode': data['pincode'],
        'purchase_order_id': data['purchase_order_id'],
        'customer_id': data['customer_id']
    }

    shipping_details.append(new_shipping_details)

    return jsonify({'message': 'Shipping Details added successfully', 'shipping_details_id': shipping_details_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
