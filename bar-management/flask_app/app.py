from flask import Flask, jsonify, request

app = Flask(__name__)

# Example route for bar sale
@app.route('/bar_sale/<int:id>', methods=['GET'])
def get_bar_sale(id):
    # Example response
    return jsonify({"id": id, "item": "Beer", "price": 5.0})

# Example route for inventory mutation
@app.route('/inventory_mutation', methods=['POST'])
def create_inventory_mutation():
    data = request.json
    # Example response
    return jsonify({"status": "success", "data": data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
