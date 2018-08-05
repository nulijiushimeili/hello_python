"""
Script introduction: 
    多重继承:
        -- 通过多继承可以给一个类的对象具备多方面的能力
        -- 这样在设计类的时候可以避免设计太多层次的复杂的继承关系
    多继承写在前面的父类在调用同名方法的时候会被先调用
        class Son(Monk,Father,Musician): 如果存在同名方法会先调用写在前面的


@Time :       2018-08-05 22:53
@Author :     nulijiushimeili
@Site :       
@File :       multi_extends.py
@Software :   PyCharm
"""


class Father(object):
    def __init__(self, name):
        self._name = name

    def gamble(self):
        print("{} 正在打麻将.".format(self._name))

    def eat(self):
        print("{} 正在大吃大喝.".format(self._name))


class Monk(object):
    def __init__(self, name):
        self._name = name

    def eat(self):
        print("{} 在吃斋.".format(self._name))

    def chant(self):
        print("%s 在念经." % self._name)


class Musician(object):
    def __init__(self, name):
        self._name = name

    def eat(self):
        print("%s 正在细嚼慢咽.")

    def play_piano(self):
        print("%s 正在谈钢琴." % self._name)


"""
多继承写在前面的父类在调用同名方法的时候会被先调用
class Son(Monk,Father,Musician):
class Son(Musician,Monk,Father):
"""


class Son(Father, Monk, Musician):
    def __init__(self, name):
        Father.__init__(self, name)
        Monk.__init__(self, name)
        Musician.__init__(self, name)


if __name__ == "__main__":
    son = Son("Wangsicong")
    son.gamble()
    # 调用Father的eat(),因为Father在多继承的类的前面
    son.eat()
    son.chant()
    son.play_piano()
