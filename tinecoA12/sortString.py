"""
date 2019/01/22
function: 字符串按照UTF-8格式排序
"""
import time

def main():
    listkey = ['authTimespan','authTimeZone','country','lang','appCode','appVersion','deviceId','channel','deviceType','requestId','accessToken','uid']
    listkey.sort()
    print(listkey)
    strURL = "v1/private/CN/ZH_CN/d465c6d264bc9e3659d3fb8ac9dd33e3/global_e/1.0.0.6/c_huawei/1/user/login"
    listValue = strURL.split('/')
    print(listValue)
    strCode = "1538105560006"+listkey[0]+"="+str(int(round(time.time()*1000)))+listkey[1]+"=Asia/Shanghai"+"="+listkey[2]+"="+listValue[2]+listkey[3]+"="+listValue[3]+listkey[4]+"="+listValue[5]+listkey[5]+"="+listValue[6]+listkey[6]+"="+listValue[4]+listkey[7]+"="+listkey[8]+"="+listValue[5]+listkey[9]
    print(strCode)



if __name__ == '__main__':
    main()