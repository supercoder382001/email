import requests
import json
from flask import request,jsonify

def validate_():
    data = request.get_json()

    # Check if data is provided
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # Access individual parameters from the JSON
    param4 = data.get('orderid')
    param5 = data.get('upiid')
    # Example processing
    if not param4 or not param5:
        return jsonify({"error": "Missing parameters"}), 400

    # Example response

    url = "https://sandbox.cashfree.com/pg/orders"
    body = {
            "customer_details": {
                "customer_id": param6,
                "customer_email": param8,
                "customer_phone": param7,
                "customer_name": param9
            },
            "order_id": param4,
            "order_amount": param5,
            "order_currency": "INR"
        }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-version": "2023-08-01",
        "x-client-id": "TEST425000f78db163221d221dbd07000524",
        "x-client-secret": "TESTd020dacb6239e76cd735c41e9f460f5119616c81"
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()
