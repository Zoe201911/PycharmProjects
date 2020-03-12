#-*- coding:UTF-8 -*-
"""
计算三角形的面积
"""
a = float(input('输入三角形第一个边长'))
b = float(input('输入三角形第二个边长'))
c = float(input('输入三角形第三个边长'))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print('三角形面积为%0.2f' %area)