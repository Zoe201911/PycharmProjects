import re
from urllib import parse

a = 'https://i.cnblogs.com/PostDone.aspx?postid=11186065&actiontip=%e5%ad%98%e4%b8%ba%e8%8d%89%e7%a8%bf%e6%88%90%e5%8a%9f'
#固定公式，：知道前后取中间
postid = re.findall('postid=(.+?)&',a)
print(postid[0])

b = 'https://i.cnblogs.com/PostDone.aspx?postid=11186065'
#如果后面没有了
postid = re.findall('postid=(.+?)$',b)
print(postid[0])

# 3.如果前面没有
c = '11186065&actiontip=%e5%ad%98%e4%b8%ba%e8%8d%8'
postid = re.findall('^(.+?)&',c)
print(postid[0])

#urlencode转换成正常的中文
h = parse.unquote(a)
print(h)

text = re.findall('actiontip=(.+?)$',h)
print(text[0])

assert text[0] == "存为草稿成功"
