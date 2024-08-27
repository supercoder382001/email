import requests
import json
import json

from flask import Flask,request,jsonify
# from initiate import initiate_
# from processorder import process_
# from validatevpa import validate_

app = Flask(__name__)
global parameter
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/create',methods=['POST'])
def create():
    data = request.get_json()

    # Check if data is provided
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400


    # Access individual parameters from the JSON
    param4 = data.get('orderid')
    param5 = data.get('amount')
    param6 = data.get('customerdetails', {}).get('customer_id')
    param7 = data.get('customerdetails', {}).get('customer_email')
    param8 = data.get('customerdetails', {}).get('customer_phone')
    param9 = data.get('customerdetails', {}).get('customer_name')
        # Example processing
    if not param4 or not param5 or not param6 or not param7 or not param8:
        res = {
            "message": "Missing parameters",
            "Status Code": 400
        }
        return json.dumps(res)
    req = {
        "message": True,
        "orderid":"11234567"
    }
    return json.dumps(req)


@app.route('/Process',methods=['POST'])
def process():
    data = request.get_json()

    # Check if data is provided
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    message = {
        "message": True
    }
    # Access individual parameters from the JSON
    param4 = data.get('orderid')
    param5 = data.get('amount')
    param6 = data.get('paymentmode')
    param7 = data.get('upiid')
    param8 = data.get('sessionid')

    # Example processing
    if not param4 or not param5 or not param6 or not param7:
        res = {
            "message": "Missing parameters",
            "Status Code": 400
        }
        return json.dumps(res)

    requests = {
        "message": True,
        "url": "ABC"
    }
    return json.dumps(requests)

@app.route('/Validate',methods=['POST'])
def validate():
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
    res = {
        "message": True
    }
    return json.dumps(res)

@app.route('/Status',methods=['POST'])
def status():
    data = request.get_json()

    # Check if data is provided
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # Access individual parameters from the JSON
    param4 = data.get('orderid')
    param5 = data.get('paymentid')
    # Example processing
    if not param4:
        return jsonify({"error": "Missing parameters"}), 400
    res = {
        "payment_status": "Success"
    }
    return json.dumps(res)

@app.route('/Cancel',methods=['POST'])
def Cancel():
    data = request.get_json()

    # Check if data is provided
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # Access individual parameters from the JSON
    param4 = data.get('orderid')
    param5 = data.get('paymentid')
    # Example processing
    if not param4:
        return jsonify({"error": "Missing parameters"}), 400
    res = {
        "message": True
    }
    return json.dumps(res)
