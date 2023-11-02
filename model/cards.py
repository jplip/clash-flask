from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api, Resource
import random
import json

app = Flask(__name__)

cards_api = Blueprint('cards_api', __name__, url_prefix='/api/cards')
api = Api(cards_api)

card_data = []

def initCards():
    global card_data
    try:
        with open("carddb.json", "r") as file:
            card_data = json.load(file)
            print("Successfully loaded JSON data:", card_data)
    except FileNotFoundError:
        card_data = []
        print("File not found.")
    except Exception as e:
        print("Error:", e)

class RandomCard(Resource):
    def get(self):
        initCards()  # Ensure card_data is up to date
        random_card = generateRandomCard()
        return jsonify(random_card)

def generateRandomCard():
    if card_data:
        return random.choice(card_data)
    else:
        return {"error": "No card data available"}

api.add_resource(RandomCard, '/rand')

if __name__ == "__main__":
    app.register_blueprint(cards_api)
    app.run(debug=True)
