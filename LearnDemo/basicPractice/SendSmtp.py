"""
1、先导入smtplib库用来发送邮件，导入MIMEText库用来做纯文本的邮件模板
2、先准备几个跟发邮件相关的参数，每个邮箱的发件服务器都不一样，以163为例，百度搜到发件服务器为：smtp.163.com
"""
import smtplib
from email.mime.text import MIMEText

#------1、邮件发送相关的参数----
smtpserver = 'smtp.163.com'            #发件服务器
port = 0                               #断开
sender = 'zhangwenjingzzh@163.com'     #账号
pwd = "Zhangmin_728"                   #密码
receiver = '1045385131@qq.com'         #收件人

"""
4、接下来就是写邮件的主题和正文内容，正文这里用HTML格式的
5、最后调用发件服务
"""

#------编辑邮件的内容------
subject = "这个是主题163"
body = '<p>这个是发送的163邮件</p>'  #定义邮件正文为html格式
msg = MIMEText(body,'html','utf-8')
msg['from'] = sender
msg['to'] = receiver
msg['subject'] = subject

#------发送邮件------

smtp = smtplib.SMTP()
smtp.connect(smtpserver)                             #连接服务器
smtp.login(sender,pwd)                               #登录
smtp.sendmail(sender,receiver,msg.as_string())       #发送
smtp.quit()                                          #关闭

