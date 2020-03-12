"""
水仙花数：如果一个三位数各个位上的的立方之和是这个数字，那么这个数字被称为水仙花数，例如 1*1*1 + 5*5*5 + 3*3*3 = 153
create by Zoe 7.8
"""

def operateNumber():
     for i in range(100,1000):
         a = i//100
         b = (i-100*a)//10
         c = i%10
         list_i = [a,b,c]
         sum = a**3 + b**3 + c**3
         if sum == i:
             print("%s 是水仙花数 "%i)


def main():
    operateNumber()

if __name__ == '__main__':
    main()