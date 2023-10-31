from flask import Blueprint, jsonify
from flask_restful import Api, Resource

# Import only what you need for the card functionality
from model.cards import *

card_api = Blueprint('card_api', __name__, url_prefix='/api/cardapi')
api = Api(card_api)

# Initialize card data
initCards()

class CardAPI:
    class _ReadRandom(Resource):
        def get(self):
            random_card = generateRandomCard()
            # Extract the title and image from the card data
            card_title = random_card.get("title", "")
            card_image = random_card.get("image", "")
            
            # Return only the title and image
            response = {"title": card_title, "image": card_image}
            return jsonify(response)

api.add_resource(CardAPI._ReadRandom, '/')

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(card_api)
    app.run(debug=True)
