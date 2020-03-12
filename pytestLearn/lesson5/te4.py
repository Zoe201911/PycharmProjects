import requests

url = "http://v.juhe.cn/weather/index"

pars = {
    "city":"苏州",
    "key":"80b4d4e1d870d257d3344fcf2d08f64a",
    "dtype":"xml",
    "format":2
}

r = requests.get(url,params=pars)

# rea = r.text["reason"]

#print(rea)


#不是所有的返回都是有json格式
print(r.text)
print(r.url)  #urlencode格式，所以中文不能正常显示
print(r.encoding)
print(r.cookies)
print(r.content)
print(r.raise_for_status())

