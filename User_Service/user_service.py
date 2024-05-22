import time
time.sleep(5)
import logging
import os
from flask import Flask, request
from resources.user import User
from db import Base, engine

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
Base.metadata.create_all(engine)

@app.route('/user', methods=['POST'])
def create_user():
    req_data = request.get_json()
    return User.create(req_data)

@app.route('/user/<d_id>', methods=['GET'])
def get_user(d_id):
    return User.get(d_id)

@app.route('/user/<d_id>', methods=['DELETE'])
def delete_user(d_id):
    return User.delete(d_id)

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0')