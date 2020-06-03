"""
[
{
    "name":name,
    "age":age,
    "score":score,
    "sex":sex
}
]
1、创建学生类（数据：姓名，年龄，成绩，性别
            行为：打印个人信息）
2、在控制台中循环录入学生信息，如果名称是空，退出录入
3、在控制台中输出每个学生信息（调用打印学生类的打印方法）
4、打印第一个学生信息

"""
class Student:

    def __init__(self,name,age,scores,sex):
        self.name = name
        self.age = age
        self.scores = scores
        self.sex = sex

    def print_self_info(self):
        print("%s的年龄是%d，成绩是%d,性别是%s" % (self.name,self.age,self.scores,self.sex))


if __name__ == '__main__':
    list_student_info = []
    while True:
        name = input("请输入姓名:")
        if name == "":
            break
        age = int(input("请输入年龄："))
        scores = int(input("请输入成绩："))
        sex = input("请输入性别：")
        stu = Student(name,age,scores,sex)
        list_student_info.append(stu)
    for stu in list_student_info:
        stu.print_self_info()
    # info = list_student_info[0]
    # info.print_self_info()
