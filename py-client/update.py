import requests

endpoint = "http://127.0.0.1:8000/api/products/10/update"

data = {
  "title":"Hello World from an old friend!",
  "price": 450.99
}
get_res = requests.put(endpoint, json=data)
print(get_res.json())