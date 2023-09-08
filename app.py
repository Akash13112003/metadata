from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Pantry API base URL with your actual Pantry ID
PANTRY_API_URL = "https://getpantry.cloud/apiv1/pantry/5763dd7d-3117-4f89-b909-428b48d34a75/basket/newBasket72"


@app.route('/add-item', methods=['POST'])
def add_item():
    data = request.get_json()
    basket_key = data.get('key')
    value = data.get('value')
    url = f"{PANTRY_API_URL}/{basket_key}"

    response = requests.post(url, json={"value": value})

    if response.status_code == 200:
        return jsonify({"message": "Item added successfully"})
    else:
        return jsonify({"error": "Failed to add item"}), 500


@app.route('/get-item', methods=['GET'])
def get_item():
    basket_key = request.args.get('basket_key')
    url = f"{PANTRY_API_URL}/{basket_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        value = data.get('value')
        if value is not None:
            return jsonify({"value": value})
        else:
            return jsonify({"error": "Item not found"}), 404
    else:
        return jsonify({"error": "Failed to fetch item"}), 500


# Implement the remaining endpoints: /list-baskets, /update-item, and /delete-item

@app.route('/list-baskets', methods=['GET'])
def list_baskets():
    # Implement listing baskets under the specified Pantry using the Pantry ID
    pass


@app.route('/update-item', methods=['PUT'])
def update_item():
    data = request.get_json()
    basket_key = data.get('basket_key')
    value = data.get('value')
    url = f"{PANTRY_API_URL}/{basket_key}"

    response = requests.put(url, json={"value": value})

    if response.status_code == 200:
        return jsonify({"message": "Item updated successfully"})
    else:
        return jsonify({"error": "Failed to update item"}), 500


@app.route('/delete-item', methods=['DELETE'])
def delete_item():
    basket_key = request.args.get('basket_key')
    url = f"{PANTRY_API_URL}/{basket_key}"

    response = requests.delete(url)

    if response.status_code == 200:
        return jsonify({"message": "Item deleted successfully"})
    else:
        return jsonify({"error": "Failed to delete item"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9443)
