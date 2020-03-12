import requests

url = "http://japi.juhe.cn/qqevaluate/qq"

pars = {
    "key":"8dbee1fcd8627fb6699bce7b986adc45",
    "qq":"1045385131"
}

h = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",

}

body = {
    "key1":"1111",
    "key2":"2222"
}


r = requests.post(url,params=pars,data=body,headers = h)