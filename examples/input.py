# test out the endpoint
import requests 
from dymopy import Dymo
from dymopy.client import make_params

base_url = 'http://localhost:3000'
body = {
    'top': 'hello', 
    'bottom': 'world',
    'copies': str(1),
    'side': 'Left'}

resp = requests.post(base_url, params=body)
resp.json()