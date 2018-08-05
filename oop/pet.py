"""
Script introduction: 

@Time :       2018-08-05 23:35
@Author :     nulijiushimeili
@Site :       
@File :       pet.py
@Software :   PyCharm
"""
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def say(self):
        pass


class Dog(Pet):
    def say(self):
        print("%s : 汪汪汪..." % self._nickname)


class Cat(Pet):
    def say(self):
        print("%s : 喵喵喵..." % self._nickname)


if __name__ == "__main__":
    pets = [Dog("Wangcai"), Cat("Keity"), Dog("Dahuang")]
    for pet in pets:
        pet.say()
