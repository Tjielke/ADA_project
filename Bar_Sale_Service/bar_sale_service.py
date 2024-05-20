import logging
import os
from flask import Flask, request
from resources.sale import Bar_sale,Status
from db import Base, engine
from flask import jsonify

from pub_sub_utils import create_subscription, create_topic

#logging.getLogger().setLevel(logging.INFO)
#create_topic("adaprojects", "inventory_update") # make sure to change the project id
#create_subscription("adaprojects", "inventory_update", "inventory_update_sub")
#create_topic("adaprojects", "balance_update")
#create_subscription("adaprojects", "balance_update", "balance_update_sub")

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
Base.metadata.create_all(engine)

@app.route('/bar_sale', methods=['POST'])
def create_sale():
    try:
        if request.is_json:
            req_data = request.get_json()
            print("Request data:", req_data)  # Debugging print
            return Bar_sale.create(req_data)
        else:
            return jsonify({'message': 'Request must be JSON'}), 415
    except Exception as e:
        print(f"An error occurred: {e}")  # Debugging print
        return jsonify({'message': 'An internal error occurred'}), 500

@app.route('/bar_sale/<d_id>', methods=['GET'])
def get_delivery(d_id):
    return Bar_sale.get(d_id)

@app.route('/bar_sale/<d_id>/status', methods=['PUT'])
def update_delivery_status(d_id):
    status = request.args.get('status')
    return Status.update(d_id, status)

@app.route('/bar_sale/<d_id>', methods=['DELETE'])
def delete_delivery(d_id):
    return Bar_sale.delete(d_id)

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0')