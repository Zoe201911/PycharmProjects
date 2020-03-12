"""
date  2019-04-18
function if character is number
isdigit()方法检测字符串是否由数字组成
isnumeric()方法检测字符串是否只由数字组成
"""
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass

    return False

def transfer(s):
    try:
        x = eval(s)
        while type(x) == int:
            break
    except:
        pass
    print("十进制数为：",s)
    print("转换为二进制：",bin(s))
    print("转换为八进制：",oct(s))
    print("转换为十六进制：",hex(s))

if __name__ == '__main__':
    print(is_number('foo'))
    print(is_number('1'))
    print(is_number('1.3'))
    print(is_number('.'))
    print(is_number('四'))
    s = input("请输入十进制数字:")
    transfer(eval(s))