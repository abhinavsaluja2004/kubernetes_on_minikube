from flask import Flask, jsonify

app = Flask(__name__)

def change(amount):
    # calculate the resultant change and store the result (res)
    res = []
    coins = [10, 5, 2, 1]  # Indian coin values
    coin_lookup = {10: "ten_rupee_coins", 5: "five_rupee_coins", 2: "two_rupee_coins", 1: "one_rupee_coins"}

    rupees = int(amount)  # since Indian coins are full rupee denominations

    for coin in coins:
        num, rupees = divmod(rupees, coin)
        if num:
            res.append({coin_lookup[coin]: num})
    
    return res

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make Indian currency change at route: /change'

@app.route('/change/<rupees>')
def changeroute(rupees):
    print(f"Make Change for ₹{rupees}")
    amount = float(rupees)
    result = change(amount)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
