import requests
import urllib3

urllib3.disable_warnings()



urlUser = "https://portal.tineco.com/api/users/user.do"

pars = {
    "todo":"ITLogin",
    "me":"15221810663",
    "password":"e10adc3949ba59abbe56e057f20f883e",
    "resource":"1234qazw",
    "country":"Chinese",
    "org":"TEK",
    "edition":"default"
}

r = requests.post(urlUser,json=pars,verify=False)

token = r.json()["token"]
print(token)

result = r.json()["result"]
if result == "ok":
    print("登录成功")
else:
    print("登录失败")

userId = r.json()["userId"]
print(userId)

urlIOT = "https://portal.tineco.com/api/iot/devmanager.do"

pars1 = {
    "toType": "9rotkh",
    "payloadType": "j",
    "toRes": "3bm9",
    "payload": {},
    "td": "q",
    "toId": "b5694567-89d9-4bee-a852-321391fed600",
    "cmdName": "gci",
    "auth": {
        "token": token,
        "resource": "IOSE5444E2FE",
        "userid": userId,
        "with": "users",
        "realm": "ecouser.net"
    }
}

r2 = requests.post(urlIOT,json=pars1,verify=False)