import requests

endpoint = "http://127.0.0.1:8000/api/"
endpoint_any = "https://httpbin.org/anything/"

# get_res = requests.get(endpoint)
get_res = requests.post(endpoint,json={"title":"Hello World"})
print(get_res.json())
