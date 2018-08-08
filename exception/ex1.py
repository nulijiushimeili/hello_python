"""
Script introduction: 
    异常机制 -- 处理程序在运行时可能发生的状态
@Time :       2018-08-08 21:20
@Author :     nulijiushimeili
@Site :       
@File :       ex1.py
@Software :   PyCharm
"""

input_again = True
while input_again:
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        print("{} / {} = {}".format(a, b, a / b))
        input_again = False
    except ValueError:
        print("请输入整数")
    except ZeroDivisionError:
        print("除数不能为0")

# 处理异常让代码不因为异常而崩溃是一方面
# 更重要的是可以通过对异常的处理让代码从异常中恢复过来
