import requests
import json
data = {"page":"1",
 "page_size": "10",
 "ordering": "create_time"}
# data = json.loads(data)
print(data)
headers =[]
# headers = json.loads(headers)
print(headers)
res = requests.get("http://211.103.136.242:8064/categories/115/skus/", headers=headers, data=data)
print(res.text)