import requests
import json

r = requests.post(
    'http://127.0.0.1:5000/save',
    data=json.dumps({'chave': 'valor'}),
    headers={'content-type': 'application/json'}
)
print(r.json())