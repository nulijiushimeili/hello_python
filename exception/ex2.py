"""
Script introduction: 
    异常处理
@Time :       2018-08-08 21:30
@Author :     nulijiushimeili
@Site :       
@File :       ex2.py
@Software :   PyCharm
"""

input_again = True
while input_again:
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        print("{} / {} = {}".format(a, b, a / b))
        input_again = False
    except(ValueError, ZeroDivisionError) as msg:
        print(msg)
