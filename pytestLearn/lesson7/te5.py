import requests
import json


url = "http://httpbin.org.post"

h = {
    "content-type":"application/json"
}

body = {
    "aaa":"11111",
    "bbb":"2222",
    "ddd":True,
    "eee":False
}

r = requests.post(url,json = body,headers = h)

r2 =  requests.post(url,data = json.dumps(body),headers = h)