"""
Script introduction: 
    从文本文件中读取数据

@Time :       2018-08-08 21:41
@Author :     nulijiushimeili
@Site :       
@File :       file1.py
@Software :   PyCharm
"""

import time


def func():
    # 一次性读取整个文件内容
    with open("example.csv", "r", encoding="utf-8") as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open("example.csv", mode="r") as f:
        for line in f:
            print(line, end="")
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open("example.csv") as f:
        lines = f.readlines()
    print(lines)


if __name__ == "__main__":
    func()
