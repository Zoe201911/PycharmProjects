import requests

#忽略warning

import urllib3
urllib3.disable_warnings()

r = requests.get('https://api.github.com/events',verify = False)

#JSON格式

print(r.json())

#返回的状态码

print(r.status_code)

#返回headers

print(r.headers)