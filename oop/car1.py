"""

属性的使用
    - 访问器/修改器/删除器
    - 使用__slots__对属性加以限制

@Time :       2018-08-05 17:24
@Author :     nulijiushimeili
@Site :       
@File :       car1.py
@Software :   PyCharm
"""


class Car(object):
    __slots__ = ("_brand", "_max_speed")

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @brand.deleter
    def brand(self):
        del self._brand

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError("Invalid max speed for car")
        self._max_speed = max_speed

    def __str__(self):
        return "Car: [brand=%s,max_speed=%d]" % (self._brand, self._max_speed)


if __name__ == "__main__":
    car = Car("QQ", 120)
    print(car)
    car._brand = "Benz"
    car._max_speed = 320
    print(car)

    # 使用了__slot__限制属性之后,下面的代码将会产生异常
    # car.current_speed = 160

    # 如果提供了删除器,可以执行下面的代码
    del car.brand
    # 属性的实现
    print(Car.brand)
    print(Car.brand.fget)
    print(Car.brand.fset)
    print(Car.brand.fdel)
