import json
import requests

from api import APP_ID, APP_KEY

ENDPOINT = 'http://api.yummly.com/v1/api/metadata/cuisine?_app_id={}&_app_key={}'.format(APP_ID, APP_KEY)
data = requests.get(ENDPOINT).text
cuisine_metadata = json.loads(data[data.find('['):data.rfind(']')+1])

with open('cuisines.json', 'w') as f:
    json.dump(cuisine_metadata, f)

