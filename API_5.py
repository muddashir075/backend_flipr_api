from flask import Flask, jsonify

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

# API endpoint to get customers with all purchase orders
@app.route('/get_customers_with_purchase_orders', methods=['GET'])
def get_customers_with_purchase_orders():
    customers_with_purchase_orders = []

    for customer in customers:
        customer_id = customer['customer_id']
        customer_purchase_orders = [po for po in purchase_orders if po['customer_id'] == customer_id]
        customer_data = {
            'customer_id': customer['customer_id'],
            'customer_name': customer['customer_name'],
            'email': customer['email'],
            'mobile_number': customer['mobile_number'],
            'city': customer['city'],
            'purchase_orders': customer_purchase_orders
        }
        customers_with_purchase_orders.append(customer_data)

    return jsonify({'customers_with_purchase_orders': customers_with_purchase_orders}), 200

if __name__ == '__main__':
    app.run(debug=True)
