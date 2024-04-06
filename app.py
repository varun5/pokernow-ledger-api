import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def minimize_transactions(ledger):
    positives = [(name, net) for name, net in ledger.items() if net > 0]
    negatives = [(name, -net) for name, net in ledger.items() if net < 0]
    positives.sort(key=lambda x: x[1], reverse=True)
    negatives.sort(key=lambda x: x[1], reverse=True)
    transactions = []
    for neg_name, neg_net in negatives:
        while neg_net > 0:
            pos_name, pos_net = positives[0]
            transaction_amount = min(neg_net, pos_net)
            transactions.append((neg_name, pos_name, transaction_amount))
            neg_net -= transaction_amount
            pos_net -= transaction_amount
            if pos_net == 0:
                positives.pop(0)
            else:
                positives[0] = (pos_name, pos_net)
    return transactions

@app.route('/get_ledger', methods=['GET'])
def get_ledger():
    base_url = request.args.get('url')
    if not base_url:
        return jsonify({'error': 'URL parameter is missing'}), 400
    
    url = base_url + '/players_sessions'
    
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data from the URL'}), 500
    
    data = response.json()
    ledger = {}
    players_infos = data.get("playersInfos", {})
    for player, info in players_infos.items():
        names_list = info.get("names", [])
        if names_list:
            name = names_list[0]
        else:
            name = "Unknown"
        net = info.get("net")
        if net is not None:
            ledger[name] = net
    
    return jsonify(ledger)

@app.route('/get_transactions', methods=['GET'])
def get_transactions():
    base_url = request.args.get('url')
    if not base_url:
        return jsonify({'error': 'URL parameter is missing'}), 400
    
    url = base_url + '/players_sessions'
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data from the URL'}), 500
    
    data = response.json()
    ledger = {}
    players_infos = data.get("playersInfos", {})
    for player, info in players_infos.items():
        names_list = info.get("names", [])
        if names_list:
            name = names_list[0]
        else:
            name = "Unknown"
        net = info.get("net")
        if net is not None:
            ledger[name] = net
    
    transactions = minimize_transactions(ledger)
    
    return jsonify({'transactions': transactions})

@app.route('/get_payment_strings', methods=['GET'])
def get_payment_strings():
    base_url = request.args.get('url')
    if not base_url:
        return jsonify({'error': 'URL parameter is missing'}), 400
    
    url = base_url + '/players_sessions'
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data from the URL'}), 500
    
    data = response.json()
    ledger = {}
    players_infos = data.get("playersInfos", {})
    for player, info in players_infos.items():
        names_list = info.get("names", [])
        if names_list:
            name = names_list[0]
        else:
            name = "Unknown"
        net = info.get("net")
        if net is not None:
            ledger[name] = net
    
    transactions = minimize_transactions(ledger)
    
    payment_strings = []
    for transaction in transactions:
        payment_amount = transaction[2] / 100  # Convert cents to dollars
        payment_strings.append(f"{transaction[0]} pays {transaction[1]} ${payment_amount}")
    
    return jsonify({'payment_strings': payment_strings})

if __name__ == '__main__':
    app.run()  # For development purposes only, remove debug=True for production deployment
