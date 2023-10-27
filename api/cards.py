from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import time
from flask import Blueprint, request, jsonify
import json
import requests


cards_api = Blueprint('cards_api', __name__,
                  url_prefix='/api/cards')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(cards_api)

def beautify_json_data(json_file_path):
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        beautified_data = []
        for item in data.get('items', []):
            beautified_item = {
                "name": item.get("name", ""),
                "maxLevel": item.get("maxLevel", 0),
            }

            medium_icon_url = item.get("iconUrls", {}).get("medium", "")
            if medium_icon_url:
                beautified_item["medium"] = medium_icon_url

            beautified_data.append(beautified_item)

        return beautified_data  # Return the processed data as a list

    except FileNotFoundError:
        return {"error": "File not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format in the file"}
    
json_list = []
json_list.append(beautify_json_data('carddb.json'))