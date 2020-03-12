import requests
import urllib3
urllib3.disable_warnings()

url = "https://smc.api.xxx.com/Account/SmcLogin"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "Content-Type":"application/json"
}

body = {
"RequestStamp": "stamp-1525484256872",
"Callback": "110",
"PostTime": 1525484256111,
}

r =requests.post(url,json=body,headers = header,verify = False)