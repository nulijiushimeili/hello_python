"""
Script introduction:
    引发异常和异常栈
@Time :       2018-08-08 21:39
@Author :     nulijiushimeili
@Site :       
@File :       ex4.py
@Software :   PyCharm
"""


def f1():
    raise AssertionError("发生异常")


def f2():
    f1()


def f3():
    f2()


f3()
