from flask import Flask, jsonify, request
from requests_oauthlib import OAuth2Session
import requests
import uuid
import random
import json
import os
import string
os.environ['DEBUG'] = '1'

app = Flask(__name__)
CLIENTID = r'YjcxYmU3MDJlYzg2ZjUyOTE2MmM5YzgwNDM4OGFjMGM5'
delivery = OAuth2Session(r'YjcxYmU3MDJlYzg2ZjUyOTE2MmM5YzgwNDM4OGFjMGM5', token={'access_token': r'66iJJMLEs5jZlGBVINWzvMldxJc6yCEDsqmc2Qhn'})


users = {}
with open('data/cuisines.json') as f:
    yummly_to_delivery_cuisines = json.load(f)
with open('data/recipes.json') as f:
    recipes = json.load(f)
with open('data/cuisines.json') as f:
    cuisine_map = json.load(f)


@app.route('/survey', methods=['GET', 'POST'])
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
            while 'yummly' in recipe['smallImageUrls'][0] or recipe in chosen_recipes:
                recipe = random.choice(recipes[c]['matches'])

            chosen_recipes.append(recipe)
        img_urls = [r['smallImageUrls'][0] for r in chosen_recipes]
        print "STORING ID: ", _id

        users[_id] = chosen_recipes
        data = {
            'id': _id,
            'urls': img_urls
        }
        return jsonify(data)
    else:
        print users
        _id = uuid.UUID(request.form['id'])
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        print _id
        print latitude
        print longitude
        result = request.form['result'].split(',')

        liked_cuisines = []
        for i, boolean in enumerate(result):
            if boolean == '1':
                recipe = users[_id][i]
                if 'cuisine' in recipe['attributes']:
                    liked_cuisines += recipe['attributes']['cuisine']
        del users[_id]
        # return redirect(url_for('get_restaurants', latitude=latitude, longitude=longitude, liked_cuisines=liked_cuisines))
        return 'NIGGA YOU CrAY'

        return get_restaurants(latitude, longitude, liked_cuisines)

@app.route('/fuck')
def get_restaurants(latitude, longitude, liked_cuisines):
    def cuisine_translate(cuisine):
        if cuisine in yummly_to_delivery_cuisines:
            return yummly_to_delivery_cuisines[cuisine]

    def url_fix(staging_url):
        return string.replace(staging_url, "staging.delivery.com/", "m.delivery.com/#!/merchants/")
    payload = {
        'client_id': CLIENTID,
        'latitude': latitude,
        'longitude': longitude,
        'merchant_type': 'R',
    }

    url = 'http://sandbox.delivery.com/merchant/search/delivery'

    json_response = requests.get(url, params=payload).json()
    liked_merchants_data = {"merchants": []}
    liked_merchants = liked_merchants_data["merchants"]
    merchants = json_response["merchants"]
    # print merchants

    liked_cuisines_mapped = set(map(cuisine_translate, liked_cuisines))

    for m in merchants:
        m_id = m["id"]
        summary = m["summary"]
        cuisines = set(summary["cuisines"])
        m_url = summary["url"]["complete"]
        if len(set.intersection(cuisines, liked_cuisines_mapped)) > 0:
            merchant_dict = {}
            merchant_dict["id"] = m_id
            merchant_dict["name"] = summary["name"]
            merchant_dict["cuisines"] = list(cuisines)
            merchant_dict["url"] = url_fix(m_url)
            liked_merchants.append(merchant_dict)
            # print "YES"
            # print cuisines
            # print liked_cuisines_mapped
    # return (json.dumps(liked_merchants_data))
    return jsonify(json.loads(json.dumps(liked_merchants_data)))
    # return liked_merchants_data
        # break
    # python_response = json.loads(str(json_response))
    # print python_response

@app.route('/test')
def test():

    lat = '34.068921'
    lon = '-118.445181'
    liked_cuis = set(["Japanese", "Chinese", "Indian"])
    return get_restaurants(lat, lon, liked_cuis)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
