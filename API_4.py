from flask import Flask, request, jsonify

app = Flask(__name__)

customers = [
    {
        'customer_id': '1',
        'customer_name': 'John Doe',
        'email': 'john.doe@example.com',
        'mobile_number': '1234567890',
        'city': 'New York'
    },
    # Add more customer data as needed
]

purchase_orders = [
    {
        'purchase_order_id': '1',
        'product_name': 'Laptop',
        'quantity': 2,
        'pricing': 1200.00,
        'mrp': 1500.00,
        'customer_id': '1'
    },
    # Add more purchase order data as needed
]

shipping_details = [
    {
        'shipping_details_id': '1',
        'address': '123 Main St',
        'city': 'New York',
        'pincode': '10001',
        'purchase_order_id': '1',
        'customer_id': '1'
    },
    # Add more shipping details data as needed
]

# API endpoint to get customers with a city filter
@app.route('/get_customers_by_city', methods=['GET'])
def get_customers_by_city():
    city_filter = request.args.get('city')

    if city_filter is None:
        return jsonify({'error': 'City parameter is missing'}), 400

    filtered_customers = []

    for shipping_detail in shipping_details:
        if shipping_detail['city'].lower() == city_filter.lower():
            customer_id = shipping_detail['customer_id']
            customer = next((c for c in customers if c['customer_id'] == customer_id), None)

            if customer is not None and customer not in filtered_customers:
                filtered_customers.append(customer)

    return jsonify({'customers': filtered_customers}), 200

if __name__ == '__main__':
    app.run(debug=True)
