import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
  "title":"Mixin Object creation done!"
}
get_res = requests.post(endpoint, json=data)
print(get_res.json())