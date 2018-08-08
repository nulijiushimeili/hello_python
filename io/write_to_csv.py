"""
Script introduction: 
    Write data to csv file.
@Time :       2018-08-07 21:44
@Author :     nulijiushimeili
@Site :       
@File :       write_to_csv.py
@Software :   PyCharm
"""

import csv


class Teacher(object):
    def __init__(self, name, age, title):
        self.__name = name
        self.__age = age
        self.__title = title
        self.__index = -1

    def name(self):
        return self.__name

    def age(self):
        return self.__age

    def title(self):
        return self.__title


filename = "teacher.csv"
teachers = [Teacher("Mashibing",36,"high-teacher"),Teacher("Likaifu",50,"S")]