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
        last_tx = data['data']['last_tx']
        response = jsonify(balance=balance, last_tx=last_tx, exists=True)
    return response


@app.route('/address/<address>/last_tx')
def get_last_tx(address):
    tx_response = urllib2.urlopen('https://bch-chain.api.btc.com/v3/address/%s' % address)
    data = json.load(tx_response)
    if data['data'] is None:
        response = jsonify(amount='0')
        response.status_code = 204
        return response

    last_tx = data['data']['last_tx']
    tx_response = urllib2.urlopen('https://bch-chain.api.btc.com/v3/tx/%s' % last_tx)
    data = json.load(tx_response)
    outputs = data['data']['outputs']
    total_amount = 0
    for output in outputs:
        for addr in output['addresses']:
            if addr == address:
                total_amount += int(output['value'])
    if total_amount > 0:
        status_code = 200
    else:
        # This means that something went wrong. Saying server denied.... fix this.
        status_code = 500

    response = jsonify(amount=satoshi_to_bch(total_amount))
    response.status_code = status_code
    return response


def satoshi_to_bch(satoshi):
    return satoshi * 0.00000001
