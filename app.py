from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add_numbers():
    if request.method == 'GET':
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
    elif request.method == 'POST':
        data = request.get_json()
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))

    result = num1 + num2
    response = {'result': result}

    return jsonify(response)

@app.route('/buy', methods=['GET'])
def buy():
    data = request.get_json()
    units = float(data.get('units', 0))
    buying_price = float(data.get('buying_price', 0))

    share_amount = units * buying_price
    sebon_commission = (0.015 / 100) * share_amount

    if share_amount <= 50000:
        broker_commission = max(0.004 * share_amount, 10)
    elif 50001 <= share_amount <= 500000:
        broker_commission = 0.0037 * share_amount
    elif 500001 <= share_amount <= 2000000:
        broker_commission = 0.0034 * share_amount
    elif 2000001 <= share_amount <= 10000000:
        broker_commission = 0.003 * share_amount
    else:
        broker_commission = 0.0027 * share_amount

    dp_fee = 25
    total_paying_amount = share_amount + sebon_commission + broker_commission + dp_fee
    cost_per_share = total_paying_amount / units

    response_list = [
        {'Share Amount': share_amount},
        {'SEBON Commission': sebon_commission},
        {'Broker Commission': broker_commission},
        {'DP Fee': dp_fee},
        {'Cost Per Share': cost_per_share},
        {'Total Paying Amount': total_paying_amount}
    ]

    return jsonify(response_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
