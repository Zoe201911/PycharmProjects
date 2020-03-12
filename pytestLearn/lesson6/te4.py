import requests

from lxml import etree

url = "http://47.104.190.48:8000/login_test/"

body = {
    "username":'test2323',
    "password":"123456",
    "csrfmiddlewaretoken":""#动态生成的一个参数
}


r1 = requests.get(url)

#获取csrfmiddlewaretoken参数


r = requests.post(url,data=body)
