import urllib.request

#urlopen()： 向URL发请求，返回响应对象
response =  urllib.request.urlopen('http://www.baidu.com/')
#提取响应内容
html = response.read().decode('utf-8')
# print(html)
#返回实际数据URL地址
url = response.geturl()
code = response.getcode()
# print(url,code)

url = "http://httpbin.org/get"
res = urllib.request.urlopen(url)
print(res.read().decode())