import json
import requests

from requests_oauthlib import OAuth2Session
from cuisines import CUISINES

payload = {}
delivery = OAuth2Session(r'YjcxYmU3MDJlYzg2ZjUyOTE2MmM5YzgwNDM4OGFjMGM5', token=r'66iJJMLEs5jZlGBVINWzvMldxJc6yCEDsqmc2Qhn')
url = 'https://api.delivery.com/merchant/search/delivery'

def get_cuisine(yummly_cuisine):
	return CUISINES[yummly_cuisine]
	
def location(latitude, longitude):
	payload['latitude'] = latitude
	payload['longitude'] = longitude




r = delivery.get(url, params=payload).json();

    
with open('restaurants.json', 'w') as f:
    json.dump(r, f)


# https://api.delivery.com/merchant/search/delivery?client_id=YjcxYmU3MDJlYzg2ZjUyOTE2MmM5YzgwNDM4OGFjMGM5&latitude=34.068921&longitude=-118.445181&merchant_type=R


#getting the menu

def menu(_id):
	new_url = 'https://api.delivery.com/merchant/'
	global delivery
	return delivery.get(new_url + _id + '/menu')

def guest_id():
	new_url = 'https://api.delivery.com/customer/auth/guest'
	global delivery
	return delivery.get(new_url)


#user_id will always be the guest ID from the previous function
def purchase_item(item_number, instructions = None, user_id, merchant_id):
	item = {"order_type": "delivery"}
	item['instructions': instructions]
	item['item': {'item_id': item_number, 'item_qty': 1}]
	item['client_id': user_id]
	new_url = 'https://api.delivery.com/customer/cart/' + merchant_id
	global delivery
	return delivery.post(new_url, params = item)








# functions necessary:
# 1. return list of restaurants based on cuisine and location
# 2. return menu after restaurant is selected
# 3. pass order information + credit card information + delivery 	information to delivery.com