"""
学生管理系统
项目计划：
1、完成数据模型类StudentModel
2、创建逻辑控制类：StudentManagerController
3、完成数据：学生列表 __stu_list
4、行为：获取列表stu_list,添加学生 add_student
5、添加学生方法 add_student
6、根据编号删除学生信息remove_student
7、根据编号修改学生信息modify_student
"""
class StudentModel:
    """
    学生信息模型
    """
    def __init__(self,name="",id=0,age=0,scores=0):#给出默认值，该变量赋值时可给可不给，不给时使用默认值
        """
        创建学生对象
        :param id: 对象的唯一标识
        :param name: 学生名称
        :param age: 学生年龄
        :param scores: 学生分数
        """

        self.name = name
        self.id = id
        self.age = age
        self.scores = scores

    # def get_id(self):
    #     return self.__id
    # id = property(get_id,None)

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if age >28 or age <10:
            raise ValueError('该学生年龄数值有误')
        else:
            self.__age = age

    @property
    def scores(self):
        return self.__scores
    @scores.setter
    def scores(self,scores):
        if scores < 0 or scores >100:
            raise ValueError('错误分值')
        else:
            self.__scores = scores



class StudentManagerController:
    """
    学生管理控制器，负责业务逻辑处理

    """
    __init_id =1000 # 类变量，如果有多个conroller类，该值只有一个,表示初始编号
    def __init__(self):
        self.__stu_list = []#不希望类的外面能修改该变量，只读属性，private类型

    @property
    def stu_list(self):
        """
        学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list
    def add_student(self,stu_info):
        """
        添加一个新学生
        :param stu_info: 没有编号的学生信息
        :return:
        """

        stu_info.id = self.generate_id(stu_info)
        self.stu_list.append(stu_info)

    def generate_id(self, stu_info):
        """
        生成一个学生id
        :param stu_info: 学生信息对象
        :return: 学生ID
        """
        StudentManagerController.__init_id += 1
        stu_info.id = StudentManagerController.__init_id
        return stu_info.id

    def remove_student(self,id):
        """
        删除学生信息
        :param id: 学生ID
        :return:
        """
        for item in self.stu_list:
            if item.id == id:
                self.stu_list.remove(item)
                return True#表示移除成功
        return False#表示移除失败

    def update_student(self,stu_info):
        for item in self.stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.scores = stu_info.scores
                return True
        return False



class StudentManagerView:
    """
    学生管理器视图
    界面功能：
    1）添加学生信息
    2）显示学生信息
    3）删除学生信息
    4）修改学生信息
    5）按学生成绩低到高显示学生信息
    请选择：1
    """

    def __init__(self):#把生成对象放在构造函数中，因为构造函数在类调用中只做一次
        self.__manager = StudentManagerController()#该变量

    def __display_menu(self):
        """
        展示学生信息
        :return:
        """

        print("1）添加学生信息")
        print("2）显示学生信息")
        print("3）删除学生信息")
        print("4）修改学生信息")
        print("5）按学生成绩低到高显示学生信息")

    def __select_menu(self):
        """
        用户输入信息
        :return:
        """
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == '2':
            self.__output_student(self.__manager.stu_list)
        elif item == '3':
            self.__delete_students()
        elif item == '4':
            self.__modify_student()
        elif item == '5':
            print(self.__sort_scores(self.__manager.stu_list))


    def main(self):
        """
        程序逻辑入口
        :return:
        """

        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        """
        输入学生信息
        :return:
        """
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        score = int(input("请输入学生成绩:"))
        stu = StudentModel(name,age = age,scores=score)
        self.__manager.add_student(stu)

    def __output_student(self,output_list):
        """
        显示学生信息
        :param output_list:
        :return:
        """
        for item in output_list:
            print(item.id,item.name,item.age,item.scores)

    def __delete_students(self):
        """
        删除学生信息
        :return:
        """
        while True:
            id = int(input("请输入要删除的id:"))
            if self.__manager.remove_student(id):
                print('删除成功')
                return
            else:
                print('删除失败')

    def __modify_student(self):
        id  = int(input("请输入学生ID："))
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        score = int(input("请输入学生成绩:"))
        stu = StudentModel(name, id=id,age=age, scores=score)
        self.__manager.update_student(stu)

    def __sort_scores(self,stu_list):
        list_socre = []
        for item in stu_list:
            list_socre.append(item.scores)
        self.__operate_sort(list_socre)
        return list_socre

    def __operate_sort(self,list_score):
        count = len(list_score)
        for i in range(count):
            for j in range(i+1,count):
                if list_score[i]>list_score[j]:
                    list_score[i] , list_score[j] = list_score[j],list_score[i]







view = StudentManagerView()
view.main()



manager = StudentManagerController()
s01 =  StudentModel('kitty',age=18)#有默认值的参数可以不传，但是如果传参的话需要给出指定名称
s02 =  StudentModel('kkk',age=18)
manager.add_student(s01)
manager.add_student(s02)
s03 = StudentModel('Zoe',1001,age=18,scores=100)
print(manager.update_student(s03))
print(manager.remove_student(1005))
for item in manager.stu_list:
    print(item.id,item.scores,item.name)






