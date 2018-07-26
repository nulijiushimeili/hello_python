def _foo():
    print("test")


class Student(object):
    # __init__ 是一个特殊的方法用于创建对象的时候初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age连个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("{} studying {} now.".format(self.name, course_name))

    # PEP8 要求标识符的名字全部用小写多个单词使用_ 进行拼接
    def watch_av(self):
        if self.age < 18:
            print("{} just can watch <bear out>.".format(self.name))
        else:
            print("{} is watch movies of love topic.".format(self.name))


# 定义一个矩形类
class Rect(object):
    def __init__(self, width=0, height=0):
        # 构造器
        self.__width = width
        self.__height = height

    # 计算周长的方法
    def perimeter(self):
        return (self.__width * self.__height) * 2

    # 计算面积
    def area(self):
        return self.__width * self.__height

    # 矩形对象的字符串表达式
    def __str__(self):
        return "矩形[{},{}]".format(self.__width, self.__height)

    # 析构器,销毁对象
    def __del__(self):
        print("destroy this object")


def student_test():
    stu1 = Student("xiaoming", 15)
    stu1.study("xiyangyang and huitailang")
    stu1.watch_av()
    stu2 = Student("xiaogang", 25)
    stu2.study("python programing design")
    stu2.watch_av()


def rect_test():
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(4, 5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())


if __name__ == "__main__":
    student_test()
    rect_test()
