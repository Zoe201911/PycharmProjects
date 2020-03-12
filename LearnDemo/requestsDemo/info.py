import requests

s = requests.session()
url = "http://47.104.190.48:8000/login_json"
url2 = "http://47.104.190.48:8000/user_info"

h = {
    "Content-Type":"application/x-www-form-urlencoded"
}

body = {
    "username":"zoe",
    "password":"123456"
}

body2 = {
    "name":"",
    "sex":"famale",
    "age":19
}

r = s.post(url,headers = h,data=body)

print(dict(s.cookies))
# print(r.json())
# print(dict(r.cookies))
# assert r.json()['status'] == 0
# assert r.json()['msg'] == 'login success!'
# assert dict(r.cookies)['sessionid']

# r2 = s.post(url2,data=body2)
r2 = requests.post(url2,data=body2)
print(r2.text)