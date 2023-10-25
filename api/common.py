from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model.characters import *

common_api = Blueprint('common_api', __name__,
                   url_prefix='/api/common')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(common_api)

class testAPI:
    # not implemented
    class _Create(Resource):
        def post(self, joke):
            pass
            
    # getJokes()
    class _Read(Resource):
        def get(self):
            return jsonify(getJokes())

    # getJoke(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getJoke(id))

    # getRandomJoke()
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomJoke())
    
    # getRandomJoke()
    class _ReadCount(Resource):
        def get(self):
            count = countJokes()
            countMsg = {'count': count}
            return jsonify(countMsg)

    # put method: addJokeHaHa
    class _UpdateLike(Resource):
        def put(self, id):
            addJokeHaHa(id)
            return jsonify(getJoke(id))

    # put method: addJokeBooHoo
    class _UpdateJeer(Resource):
        def put(self, id):
            addJokeBooHoo(id)
            return jsonify(getJoke(id))

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create/<string:joke>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateLike, '/like/<int:id>')
    api.add_resource(_UpdateJeer, '/jeer/<int:id>')
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://flask.nighthawkcodingsociety.com' # run from web
    url = server + "/api/common"
    responses = []  # responses list

    # get count of jokes on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update likes/dislikes test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  # read joke by id
        ) 
    responses.append(
        requests.put(url+"/like/"+num) # add to like count
        ) 
    responses.append(
        requests.put(url+"/jeer/"+num) # add to jeer count
        ) 

    # obtain a random joke
    responses.append(
        requests.get(url+"/random")  # read a random joke
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")

#define which characters from model.character are common
class commonCharacter:
    def __init__(self, name, elixir):
        self.name = name
        self.elixir = elixir

# Sample list of Product objects
products = [
    commonCharacter("Laptop", 900),
    commonCharacter("Smartphone", 600),
    commonCharacter("Tablet", 300),
]

# Define a comparison function based on the price attribute
def compare_price(product):
    return product.elixir

# Sort the list of products by price
sorted_products = sorted(products, key=compare_price)

# Print the sorted list
for product in sorted_products:
    print(product.name, product.elixir)
    

card_data = []
card_list = [
    
]