import requests

#打开浏览器无界面，会话管理
s = requests.session()
print(s.cookies)

r = s.get("http://47.104.190.48:8080/login")

print(s.cookies)

r2 = s.get("http://47.104.190.48:8080/login")