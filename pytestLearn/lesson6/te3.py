import requests

url = "http://127.0.0.1:81/zentao/user-login.html"

body = {
    "referer":"http://127.0.0.1:81/zentao/my/",
    "password":"jiami",
    "keepLogin[]":"on",
    "account":"account"
}

r = requests.post(url,data= body)

print(r.text)

print(r.content.decode("utf-8"))#不显示乱码，正常显示中文

if "parent.location" in r.content.decode(("utf-8")):
    print("登录成功")
else:
    print('登录失败')