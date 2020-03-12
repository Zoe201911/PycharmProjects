import  requests
import json
import urllib3
urllib3.disable_warnings()

url = "https://www.cnblogs.com/yoyoketang"
r = requests.get(url,verify = False)
# print(r.text)
print(json.loads(r.text))