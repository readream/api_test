import requests
import json
data = {"username": "python", "password": "12345678"}
# data = json.loads(data)
print(data)
headers =[]
# headers = json.loads(headers)
print(headers)
res = requests.post("http://211.103.136.242:8064/authorizations/", headers=headers, data=data)
print(res.text)