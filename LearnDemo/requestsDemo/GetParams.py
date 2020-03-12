#coding:utf-8
import requests

url = "http://japi.juhe.cn/qqevaluate/qq"

par = {
        "key" : "8dbee1fcd8627fb6699bce7b986adc45",
        "qq" :"283340479"


        }

#r = requests.get(url,params=par)  #get请求

r = requests.post(url,params = par)  #post请求

print("打印text",r.text)#打印返回结果文本

print("打印content",r.content)

print("打印encoding",r.encoding)

print("打印cookie",r.cookies)

print("打印header",r.headers)
