import requests
import json
import urllib3
urllib3.disable_warnings()


def login():
    """
    登录IOT接口，返回token和userId值
    :return:
    """
    listLogin = []
    urlUser = "https://portal.tineco.com/api/users/user.do"
    pars = {
        "todo": "ITLogin",
        "me": "15221810663",
        "password": "e10adc3949ba59abbe56e057f20f883e",
        "resource": "1234qazw",
        "country": "Chinese",
        "org": "TEK",
        "edition": "default"
    }

    r = requests.post(urlUser, json=pars, verify=False)

    token = r.json()["token"]
    print(token)
    userId = r.json()["userId"]

    result = r.json()["result"]
    listLogin.append(token)
    listLogin.append(userId)
    if result == "ok":
        print("登录成功")
    else:
        print("登录失败")

    return listLogin

loginPar = login()

url = "https://portal.tineco.com/api/iot/devmanager.do"
pars = {
    "toType": "9rotkh",
    "payloadType": "j",
    "toRes": "3bm9",
    "payload": {},
    "td": "q",
    "toId": "b5694567-89d9-4bee-a852-321391fed600",
    "cmdName": "gci",
    "auth": {
        "token": loginPar[0],
        "resource": "IOSE5444E2FE",
        "userid": loginPar[1],
        "with": "users",
        "realm": "ecouser.net"
    }
}

r = requests.post(url,json=pars,verify=False)
