"""
另一种创建对象的方式
"""


def bar(self, name):
    self._name = name


def foo(self, course_name):
    print("{} is studying {} now.".format(self._name, course_name))


def student_test02():
    Student = type('Student', (object,), dict(__init__=bar, study=foo))
    stu1 = Student('xiaoqiang')
    stu1.study('Python programing')


if __name__ == "__main__":
    student_test02()
