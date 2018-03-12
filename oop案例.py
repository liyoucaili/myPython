'''
定义一个学生类，用来形容学生

'''
#定义一个空类
class Student():
    pass
#定义一个对象
mingyue = Student()
class pythonstudent():
    name = None
    age = 18
    course = "python"
    def dohomework(self):
        print("I 在做作业")
        #推荐函数末尾使用return
        return None

#实例化一个叫做月月的学生
#实例化一个叫做月月的学生
yueyue = pythonstudent()
print(yueyue.name)
print(yueyue.age)
yueyue.dohomework()
#obj.__dict__\检查对象所有属性
#classname.__dict__检查类所有属性
yueyue.__dict__
pythonstudent.__dict__