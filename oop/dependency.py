"""
Script introduction: 
    对象中间的依赖关系和运算符重载

@Time :       2018-08-05 21:46
@Author :     nulijiushimeili
@Site :       
@File :       dependency.py
@Software :   PyCharm
"""


class Car(object):
    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def brand(self):
        return self._brand

    def accelerate(self, delta):
        self._current_speed += delta
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed

    def brake(self):
        self._current_speed = 0

    def __str__(self):
        return "{} current speed {}".format(self._brand, self._current_speed)


class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    # The student uses the car, Student dependency Car
    def drive(self, car):
        print("{} drive {} running on the road.".format(self._name, self._age))
        car.accelerate(30)
        print(car)
        car.accelerate(50)
        print(car)
        car.accelerate(50)
        print(car)

    def study(self, course_name):
        print("{} is studying {} now.".format(self._name, course_name))

    def watch_mv(self):
        if self._age < 18:
            print("{} just can watch <Bear Appear>".format(self._name))
        else:
            print("{} is watching action romance.".format(self._name))

    # 重载大于(>)运算符
    def __gt__(self, other):
        return self._age > other._age

    # 重载小于(<)运算符
    def __lt__(self, other):
        return self._age < other._age


if __name__ == "__main__":
    stu1 = Student("Andy", 23)
    stu1.study("Python programing")
    stu1.watch_mv()
    stu2 = Student("Xiaoming", 15)
    stu2.study("English 'Hello word.'")
    stu2.watch_mv()
    car = Car("QQ", 120)
    stu2.drive(car)
    print(stu1 > stu2)
    print(stu1 < stu2)
