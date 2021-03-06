"""
Script introduction:
    实例方法和类方法的应用

@Time :       2018-08-06 00:15
@Author :     nulijiushimeili
@Site :       
@File :       triangle.py
@Software :   PyCharm
"""

from math import sqrt


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 静态方法
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    # 实例方法
    def perimeter(self):
        return self._a + self._b + self._c

    # 实例方法
    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


if __name__ == "__main__":
    # 用字符串的split方法将字符串拆分成一个列表
    # 再通过map函数对列表中的每个字符串进行映射成小数\
    a, b, c = map(float, input("Please input triangle three side length:").split())
    # 先判断给定的三角形的三条边是否能构成一个三角形
    # 如果能才构建三角形对象
    if Triangle.is_valid(a, b, c):
        triangle = Triangle(a, b, c)
        print("Perimeter: ", triangle.perimeter())
        print("Perimeter: ", triangle.area())
        # 如果传入对象作为方法参数也可以通过类调用实例方法
        # print('周长:', Triangle.perimeter(tri))
        # print('面积:', Triangle.area(tri))
        # 看看下面的代码就知道其实二者本质上是一致的
        # print(type(triangle.perimeter))           # <class 'method'>
        # print(type(Triangle.perimeter))           # <class 'function'>
    else:
        print('Not a triangle.')
