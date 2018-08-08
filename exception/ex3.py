"""
Script introduction: 
    异常处理
@Time :       2018-08-08 21:34
@Author :     nulijiushimeili
@Site :       
@File :       ex3.py
@Software :   PyCharm
"""

import time
import sys

filename = input("请输入文件名:")
try:
    with open(filename) as f:
        lines = f.readlines()
except FileNotFoundError as fnfe:
    print("无法打开文件:", filename)
    print(fnfe)
except UnicodeDecodeError as ude:
    print("非文本文件无法解码")
    sys.exit()
else:
    for line in lines:
        print(line.rstrip())
        time.sleep(0.5)
finally:
    # 此处最适合做善后工作
    print("不管发生什么都会执行.")
