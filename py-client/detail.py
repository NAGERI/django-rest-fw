import requests

endpoint = "http://127.0.0.1/api/products/1/"

get_res = requests.get(endpoint)
print(get_res.json())