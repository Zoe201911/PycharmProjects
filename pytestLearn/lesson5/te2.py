import requests

#忽略warning

import urllib3
urllib3.disable_warnings()

par = {
    "key1":"value1",
    "key2":"value2"
}

#伪造请求头，模拟从浏览器发出去请求
h = {
     "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
    "Cache-Control":"max-age=0"
}


r = requests.get("http://httpbin.org/get",params=par,headers=h)
print(r.json())
print(r.text)
print(r.encoding)#查看返回的编码格式
print(r.content)