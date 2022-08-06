import requests

data  = {"data":"hello"}
payload = {"Content-Type": "application/json"}
url = "http://127.0.0.1:8000/api1/post/"
out = requests.post(url,headers=payload,json=data)
print(out.text)
url = "http://127.0.0.1:8000/api1/get/"
out = requests.get(url,headers=payload,json=data)
print(out.text)