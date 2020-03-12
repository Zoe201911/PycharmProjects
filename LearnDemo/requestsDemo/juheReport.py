import  requests

import urllib3
urllib3.disable_warnings()

url = "http://v.juhe.cn/weather/index"

par = {
    "cityname":"苏州",
    "dtype":"json",
    "format":"2",
    "key":"80b4d4e1d870d257d3344fcf2d08f64a"
}


r = requests.post(url,params=par)

print(r.text)