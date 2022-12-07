import requests

endpoint = "http://127.0.0.1:8000/api/products/4/"

get_res = requests.get(endpoint)
print(get_res.json())