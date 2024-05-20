import logging
import os
from flask import Flask, request
from resources.product import Product,Stock
from db import Base, engine

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
Base.metadata.create_all(engine)

@app.route('/product', methods=['POST'])
def create_sale():
    req_data = request.get_json()
    return Product.create(req_data)

@app.route('/product/<d_id>', methods=['GET'])
def get_delivery(d_id):
    return Product.get(d_id)

@app.route('/product/<d_id>/stock', methods=['PUT'])
def update_delivery_status(d_id):
    stock = request.args.get('stock')
    return Stock.update(d_id, stock)

@app.route('/product/<d_id>', methods=['DELETE'])
def delete_delivery(d_id):
    return Product.delete(d_id)

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0')