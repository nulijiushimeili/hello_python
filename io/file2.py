"""
Script introduction: 
    读取圆周率文件判断其中是否包含自己的生日
@Time :       2018-08-08 21:48
@Author :     nulijiushimeili
@Site :       
@File :       file2.py
@Software :   PyCharm
"""

birth = input("请输入你的生日:")
with open("pi.txt") as f:
    lines = f.readlines()
    pi_string = ""
    for line in lines:
        pi_string += line.strip()
    if birth in pi_string:
        print("Bingo!!!")
    else:
        print("Not fond!")
