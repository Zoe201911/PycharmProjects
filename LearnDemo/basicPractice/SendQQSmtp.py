"""
QQ邮箱是需要SSL认证的，这种邮箱跟163有点不一样
QQ邮箱POP3和SMTP服务器地址设置如下：邮箱qq.com，POP3服务器（端口110)pop.qq.com，SMTP服务器（端口25）smtp.qq.com
1）SMTP服务器需要身份验证
2）如果是设置POP3和SMTP的SSL加密方式，则端口如下：
1））POP3服务器（端口995）
2））SMTP服务器（端口465或587）
找到QQ邮箱授权码，打开QQ邮箱--设置--账号POP3开启服务---开启（如果已经开启了，不知道授权码，就点温馨提示里的'生成授权码'）
生成授权码"kyvtjvqrjmkrbced" 生成的授权码要当做邮箱密码

"""
import smtplib
from email.mime.text import MIMEText

smtpserver = 'smtp.qq.com'
port = 465
sender = "1045385131@qq.com"
receiver = 'zhangwenjingzzh@163.com'
pwd = 'kyvtjvqrjmkrbced'

subject = "这是主题QQ"
body = "<p>这是发送的QQ邮件</p>"
msg = MIMEText(body,'html','utf-8')
msg['from'] = sender
msg['to'] = receiver
msg['subject'] = subject

smtp = smtplib.SMTP_SSL(smtpserver,port)
smtp.login(sender,pwd)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
