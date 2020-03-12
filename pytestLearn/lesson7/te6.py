import requests
import json

url = "http://japi.juhe.cn/qqevaluate/qq"
par = {
    "key":"8dbee1fcd8627fb6699bce7b986adc45",
    "qq":"1045385131"
}

r = requests.get(url,params = par)

print(r.text) #复制出来，在线解析

print(r.json())

print(r.json().get('reason',"Meizhaodao"))

