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

    # Check if the share amount and other fields are whole numbers
    if share_amount.is_integer():
        share_amount = int(share_amount)
    
    if sebon_fee.is_integer():
        sebon_fee = int(sebon_fee)
    
    if broker_commission.is_integer():
        broker_commission = int(broker_commission)
    
    if total_paying_amount.is_integer():
        total_paying_amount = int(total_paying_amount)
    
    if cost_per_share.is_integer():
        cost_per_share = int(cost_per_share)
    
    if price_per_share.is_integer():
        price_per_share = int(price_per_share)

    if total_charges.is_integer():
        total_charges = int(total_charges)
    
    units = float(request.args.get('units', 0))
    buying_price = float(request.args.get('buying_price', 0))

    share_amount = round(units * buying_price, 2)
    sebon_fee = round((0.015 / 100) * share_amount, 2)

    if share_amount <= 50000:
        broker_commission = round(max(0.004 * share_amount, 10), 2)
    elif 50001 <= share_amount <= 500000:
        broker_commission = round(0.0037 * share_amount, 2)
    elif 500001 <= share_amount <= 2000000:
        broker_commission = round(0.0034 * share_amount, 2)
    elif 2000001 <= share_amount <= 10000000:
        broker_commission = round(0.003 * share_amount, 2)
    else:
        broker_commission = round(0.0027 * share_amount, 2)

    dp_charge = 25
    total_paying_amount = round(share_amount + sebon_fee + broker_commission + dp_charge, 2)
    cost_per_share = round(total_paying_amount / units, 2)
    price_per_share = round(buying_price + (broker_commission / units), 2)
    # Calculate the total charges
    total_charges = round(sebon_fee + broker_commission + dp_charge, 2)

    response_dict = {
        'Share Amount': share_amount,
        'Sebon Fee': sebon_fee,
        'Broker Commission': broker_commission,
        'DP Charge': dp_charge,
        'Price Per Share': price_per_share,
        'Total Charges': total_charges,
        'Payable Amount': total_paying_amount
    }

    return jsonify(response_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
