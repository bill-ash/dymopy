# test out the endpoint
import requests 
from dymopy import Dymo
from dymopy.client import make_params

base_url = 'http://localhost:3000'

body = {
    'top': 'hello', 
    'bottom': 'rob with copies',
    'copies': str(3),
    'side': 'Left'
    }

resp = requests.post(base_url, params=body)
resp.json()