import requests

headers = {
    "Authorization": "Bearer 43ca8ee5713eaef2a473e17a3c6b1874b8a3a535"
  }
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
  "title":"Token Object creation done!"
}
get_res = requests.post(endpoint, json=data,headers=headers)
print(get_res.json())