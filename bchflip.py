from flask import Flask, request, jsonify

import urllib2
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bitflip API Server'

@app.route('/address', methods=['GET', 'POST'])
def address():
    if request.method == 'POST':
        # generate_new_address()
        response = jsonify(address="xxxxxxxxx", created=True)
        return response
    else:
        # get_address()
        response = jsonify(address="xxxxxxxxx", created=False)
        return response

@app.route('/address/<address>')
def get_address_balance(address):
    address_response = urllib2.urlopen('https://bch-chain.api.btc.com/v3/address/%s' % address)
    data = json.load(address_response)

    if data['data'] is None:
        response = jsonify(balance='0', exists=False)
    else:
        balance = data['data']['balance']
        response = jsonify(balance=balance, exists=True)
    return response
