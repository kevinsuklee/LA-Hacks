import json
import requests

from api import APP_ID, APP_KEY
from cuisines import CUISINES


ENDPOINT = 'http://api.yummly.com/v1/api/recipes'
payload = {
    '_app_id': APP_ID,
    '_app_key': APP_KEY,
    'q': '',
    'requirePictures': 'true',
    'allowedCuisine[]': None,
}

recipes = {}

for c in CUISINES:
    payload['allowedCuisine[]'] = c
    r = requests.get(ENDPOINT, params=payload)
    recipes[c] = r.json()

with open('../data/recipes.json', 'w') as f:
    json.dump(recipes, f)
