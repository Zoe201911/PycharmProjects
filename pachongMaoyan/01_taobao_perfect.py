from urllib import request
import time
import random
from useragents import ua_list

class taobaoSpider(object):
    def __init__(self):
        self.url = ''

    #功能函数1：获取响应内容
    def get_html(self):
        headers = {'User-Agent':random.choice(ua_list)}
    #功能函数2：解析提取数据
    def re_func(self):
        pass