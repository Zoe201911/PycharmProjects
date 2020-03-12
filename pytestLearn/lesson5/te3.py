import requests

url = "http://japi.juhe.cn/qqevaluate/qq"

par = {
    "key":"8dbee1fcd8627fb6699bce7b986adc45",
    "qq":"1045385131"
}

r = requests.get(url,params=par)

print(r.json())

rea = r.json()["reason"]
print(rea)

anal = r.json()["result"]["data"]["analysis"]
print(anal)