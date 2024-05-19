import logging
import os
from flask import Flask, request
from resources.sale import Bar_sale,Status
from db import Base, engine

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
Base.metadata.create_all(engine)

@app.route('/bar_sale', methods=['POST'])
def create_sale():
    req_data = request.get_json()
    return Bar_sale.create(req_data)

@app.route('/deliveries/<d_id>', methods=['GET'])
def get_delivery(d_id):
    return Bar_sale.get(d_id)

@app.route('/deliveries/<d_id>/status', methods=['PUT'])
def update_delivery_status(d_id):
    status = request.args.get('status')
    return Status.update(d_id, status)

@app.route('/deliveries/<d_id>', methods=['DELETE'])
def delete_delivery(d_id):
    return Bar_sale.delete(d_id)

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5002)), host='0.0.0.0')