"""
购物车，体会重构
2048算法，体会降为思想，锻炼逻辑思维
面向对象
概述：
   面向过程：关注过程（细节，"干活），例如：购物车
           选择菜单--》购买--》打印商品信息--》创建订单
           --》结算
   面向对象：关心解决问题的人（过程，"找"）
   类与对象：
        类：类别，类名，数据成员，行为成员。类与类的区别：行为不同
        对象：对象与对象区别，数据不同

"""
map = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2],
]
list_merge = None
def move_right():
    """
    向右移动：将二维列表中每行（从右向左）交给merge函数进行合并
    :return:
    """
    for line in map:
        global list_merge
        #从右向左取出数据，形成新列表
        list_merge = line[::-1]#把切片赋值给某个变量时会生成一个新的列表
        merge()
        #从右向左接受 合并后的数据
        line[::-1] = list_merge #把一个列表赋值给一个切片，不会生成一个新的列表，把list_merge里的元素从后往前放置在切片中,起到定位置的作用



def merge():
    """
    先将中间的零元素移到末尾
    再合并相邻相同元素
    :return:
    """
    zero_to_end()
    for i in range(len(list_merge)-1):
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] += list_merge[i+1]
            del list_merge[i+1]
            list_merge.append(0)

def zero_to_end():
    pass

