"""
Script introduction: 
    写文本文件
        将100以内的素数写入到文件中
@Time :       2018-08-08 22:01
@Author :     nulijiushimeili
@Site :       
@File :       file3.py
@Software :   PyCharm
"""

from math import sqrt


def is_prime(n):
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
        return True


with open("prime.txt", "w") as f:
    for num in range(2, 100):
        if is_prime(num):
            f.write(str(num) + "\n")
print("写入完成!")
