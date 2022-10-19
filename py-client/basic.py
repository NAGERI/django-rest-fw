import requests

endpoint = "http://127.0.0.1:8000/api/"
endpoint_any = "https://httpbin.org/anything/"

get_res = requests.get(endpoint)

print(get_res.json())
