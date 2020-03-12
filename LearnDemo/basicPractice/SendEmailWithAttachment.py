"""
MIMEText只能发送正文，无法带附件，发送带附件的需要导入另外一个模块MIMEMultipart
先读取要发送文件的内容，filePath是路径的参数名
filename = "test_report.html"
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(sender ,pwd,smtpServer,smtpPort,filePath,receiver):
    # -----编辑邮件内容-----
    #读文件
    with open(filePath, "rb") as fp:
        mail_body = fp.read()


    subject = "report data"
    msg = MIMEMultipart()
    msg['from'] = sender
    msg['to'] = ";".join(receiver)  #发送给多个人，msg["to"]这个参数不能用list了，得先把receiver参数转化成字符串
    msg['subject'] = subject

    #正文
    body =  MIMEText(mail_body,'html','utf-8')
    msg.attach(body)

    #附件
    att = MIMEText(mail_body,"html","utf-8")
    att['Content-Type'] = "application/octet-stream"
    att['Content-Disposition'] = 'attachment;filename = "report.html"'
    msg.attach(att)


    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpServer)
        smtp.login(sender,pwd)

    except:
        smtp = smtplib.SMTP_SSL(smtpServer,smtpPort)
        smtp.login(sender,pwd)

    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()


def main():
    sendEmail("1045385131@qq.com","kyvtjvqrjmkrbced","smtp.qq.com",465,"test_report.html",["zhangwenjingzzh@163.com","zoe.zhang@tineco.com"])


if __name__ == '__main__':
    main()


"""
邮件收不到的几种原因：
1，subject和正文内容都不要用hello，Hehe，test等单词
2、from和to不要为空，不然会被认为是垃圾邮件
3、找不到的话可以先看一下垃圾信箱
4、如果前几次可以收到，后来收不到了，需该下subject内容（因为每次都是一个subject，系统也会拒收，把subject内容设置为动态的是最好的）
5、部分邮箱是SSL加密的，所以无法发送，例如：qq，（需要用授权码登录）
"""