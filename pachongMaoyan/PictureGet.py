
from urllib import  request

#非结构化数据抓取
url = 'https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i4/2200676434400/O1CN01GxKrQv1iNFHN0Oji5_!!2200676434400.jpg_430x430q90.jpg'

res = request.urlopen(url)#向网站发送请求并获取地址对象

html = res.read()

with open('ifloor.jpg','wb') as f :
    f.write(html)



#OS模块使用创建本地文件夹，不存在的文件夹自动创建
import os

directory = '/Users/mac-pc/Documents/Ddd/lll'

if not os.path.exists(directory):

    os.makedirs(directory)


