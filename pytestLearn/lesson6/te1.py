import requests

"""
post请求参数一部分在URL里，另一部分在body里

常见的有四种，并不是只有四种

1、第一种：Content-Type:application/json:{"key1":"value1","key2":"value2"} 
json = 

2、第二种：Content-Type:application/x-www-form-urlencoded:name1=value1&name2=value2
data=

3、第三种：Content-Type:multipart/form-data：这一种是表单格式的（文件上传file=，图片上传等混合式）
data=

4、第四种：Content-Type:octets/stream(文件下载）
data=

5、Content-Type:text/xml
data = 

注意：如果是Content-Type:application/json就用json= ，其他的都用data=

"""


url = "http://httpbin.org/post"

body = {
    "key1":"value1",
    "key2":"value2"
}

#如果key的值是一样的，这个时候不能用字典，可以用list或者tuple代替

body1 = (("key1","value1"),
         ("key1","value2")
         )

r = requests.post(url,data = body1) # body可以传json=body ，也可以传data =body