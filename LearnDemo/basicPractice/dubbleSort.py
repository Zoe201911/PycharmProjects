"""
function：冒泡排序
author：Zoe
time:2019/7/8
"""

def dubbleSort(list1):
    print(list1)
    list2 = range(len(list1))[::-1]
    for i in list2:
        for j in range(i):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    print(list1)


def main():
    dubbleSort([3,2,1,9,7,92,4])


if __name__ == '__main__':
    main()