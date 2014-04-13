from flask import Flask, jsonify, request
from requests_oauthlib import OAuth2Session
import uuid
import random
import json

app = Flask(__name__)
delivery = OAuth2Session(r'YjcxYmU3MDJlYzg2ZjUyOTE2MmM5YzgwNDM4OGFjMGM5', token=r'66iJJMLEs5jZlGBVINWzvMldxJc6yCEDsqmc2Qhn')

users = {}
with open('data/cuisines.json') as f:
    yummly_to_delivery_cuisines = json.load(f)
with open('data/recipes.json') as f:
    recipes = json.load(f)
with open('data/cuisines.json') as f:
    cuisine_map = json.load(f)


@app.route('/survey', methods=['GET'])
def survey():
    """
    Creates a uuid for the user and send them the recipes pictures
    """
    if request.method == 'GET':
        _id = uuid.uuid4()
        while _id in users:
            _id = uuid.uuid4()
        rand_cuisines = random.sample(recipes, 5)
        chosen_recipes = []
        for c in rand_cuisines:
            recipe = random.choice(recipes[c]['matches'])
            while 'yummly' in recipe['smallImageUrls'][0]:
                recipe = random.choice(recipes[c]['matches'])
            chosen_recipes.append(recipe)
        img_urls = [r['smallImageUrls'][0] for r in chosen_recipes]
        users[_id] = recipes
        data = {
            'id': _id,
            'urls': img_urls
        }
        return jsonify(data)
    else:
        _id = request.args.get('id')
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        result = request.args.get('result').split(',')

        liked_cuisine = []
        for i, boolean in enumerate(result):
            if boolean == '1':
                recipe = users[_id][i]
                liked_cuisine.append(recipe['cuisine'])
        del users[_id]
        return get_restaurants(_id, latitude, longitude, liked_cuisine)


def get_restaurants(latitude, longitude, liked_cuisine):
    """
    Query for the
    """
    payload = {'latitude': latitude, 'longitude':longitude}
    delivery.get




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)