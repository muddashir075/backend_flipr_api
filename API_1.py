from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

customers = []

@app.route('/api/customers/add', methods=['POST'])
def add_customer():
    data = request.get_json()

    if not all(key in data for key in ('name', 'email', 'mobileNumber', 'city')):
        return jsonify({'error': 'Missing data'}), 400

    customer_id = str(uuid.uuid4())
    customer_name = data['name']
    email = data['email']
    mobile_number = data['mobileNumber']
    city = data['city']

    new_customer = {
        'customerId': customer_id,
        'name': customer_name,
        'email': email,
        'mobileNumber': mobile_number,
        'city': city
    }

    customers.append(new_customer)

    return jsonify({'message': 'Customer added successfully', 'customerId': customer_id})

if __name__ == '__main__':
    app.run(debug=True)
