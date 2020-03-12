import requests
from lxml import etree
import re
import urllib3
urllib3.disable_warnings()


url = "http://47.104.190.48:8080/login_test/"

r = requests.get(url)
h = r.headers
print(h)

cookies = r.cookies

#RequestsCookieJar特殊的数据类型
print(dict(cookies))

h = {"Content-Type":"application/x-www-form-urlencoded",
     "Cookie":"csrftoken = %s"%dict(cookies)['csrftoken']
    }
print(h)

#token值从页面抓取
# demo = etree.HTML(r.text)
# nodes = demo.xpath(".//*[@name='csrfmiddlewaretoken']")
# token = nodes[0].attrib['value']

token = re.findall('name="csrfmiddlewaretoken" value="(.+?)"',r.text)

print("token:",token)
body = {"csrfmiddlewaretoken":token,"username":"zoe","password":"123456"}

r2 = requests.post(url,headers =h,data=body)#allow_redirects=False 不允许重定向

# print(r2.text)

#查看重定向历史
his= r2.history
print(his)

r302 = his[0].status_code
print("重定向码：",r302)
r302_headers = his[0].headers
print("重定向请求头",r302_headers)

r302_cookies = his[0].cookies
print("重定向请求cookie",r302_cookies)


if "登录成功" in r2.text:
    print("*********登陆成功*********")
else:
    print("********登录失败*******")

