"""
Script introduction: 
    继承的应用
        - 抽象类
        - 抽象方法
        - 方法的冲写
        - 多态

@Time :       2018-08-06 00:02
@Author :     nulijiushimeili
@Site :       
@File :       shape.py
@Software :   PyCharm
"""

from abc import ABCMeta, abstractmethod
from math import pi


class Shape(object, metaclass=ABCMeta):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def perimeter(self):
        return 2 * pi * self._radius

    def area(self):
        return pi * self._radius ** 2

    def __str__(self):
        return "This is a circle."


class Rect(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimeter(self):
        return 2 * self._width * self._height

    def area(self):
        return self._width * self._height

    def __str__(self):
        return "This is a rectangle."


if __name__ == "__main__":
    shapes = [Circle(5), Circle(10), Rect(4, 3)]
    for shape in shapes:
        print(shape)
        print("Perimeter:", shape.perimeter())
        print("Area:", shape.area())
