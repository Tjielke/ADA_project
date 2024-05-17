import json
import os

import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/add_user', methods=["GET", "POST"])
def check_diabetes():
    if request.method == "POST":
        acount_info = [
            {
                "name": int(request.form.get("name")),
                "birthdate": int(request.form.get("birthdate")), 
                "balance": int(request.form.get("balance")),
            }
        ]
        print(acount_info)
        # use requests library to execute the prediction service API by sending a HTTP POST request
        # use an environment variable to find the value of the diabetes prediction API
        account_api_url = os.environ['PREDICTOR_API']
        res = requests.post(account_api_url, json=json.loads(json.dumps(acount_info)))
        print(res.status_code)
        result = res.json()
        return result
    return render_template(
        "user_form.html")  # this method is called of HTTP method is GET, e.g., when browsing the link


@app.route('/add_product', methods=["GET", "POST"])
def check_diabetes():
    if request.method == "POST":
        product_info = [
            {
                "productID": int(request.form.get("productID")),
                "price": int(request.form.get("price")), 
                "inventory_amount": int(request.form.get("inventory_amount")),
            }
        ]
        print(product_info)
        # use requests library to execute the prediction service API by sending a HTTP POST request
        # use an environment variable to find the value of the diabetes prediction API
        product_api_url = os.environ['PREDICTOR_API']
        res = requests.post(product_api_url, json=json.loads(json.dumps(product_info)))
        print(res.status_code)
        result = res.json()
        return result
    return render_template(
        "user_form.html")
    
@app.route('/bar_order', methods=["GET", "POST"])
def check_diabetes():
    if request.method == "POST":
        bar_order_info = [
            {
                "orderID": int(request.form.get("orderID")),
                "DateTime": int(request.form.get("DateTime")), 
                "seller": int(request.form.get("seller")),
                "buyer": int(request.form.get("buyer"))
            }
        ]
        print(bar_order_info)
        # use requests library to execute the prediction service API by sending a HTTP POST request
        # use an environment variable to find the value of the diabetes prediction API
        bar_order_api_url = os.environ['PREDICTOR_API']
        res = requests.post(bar_order_api_url, json=json.loads(json.dumps(bar_order_info)))
        print(res.status_code)
        result = res.json()
        return result
    return render_template(
        "user_form.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


