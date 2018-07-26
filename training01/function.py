"""
Python常用模块
- 运行时服务相关模块: copy / pickle / sys / ...
- 数学相关模块: decimal / math / random / ...
- 字符串处理模块: codecs / re / ...
- 文件处理相关模块: shutil / gzip / ...
- 操作系统服务相关模块: datetime / os / time / logging / io / ...
- 进程和线程相关模块: multiprocessing / threading / queue
- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
- Web编程相关模块: cgi / webbrowser
- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...
"""
import time
import shutil
import os


# test os command
def exec_on_linux():
    shutil.copy('/Users/Hao/hello.py', '/Users/Hao/Desktop/first.py')
    os.system('ls -l')
    os.chdir('/Users/Hao')
    os.system('ls -l')
    os.mkdir('test')


# test time
def usage_model_test():
    seconds = time.time()
    print(seconds)
    localtime = time.localtime(seconds)
    print(localtime)
    print(localtime.tm_year)
    print(localtime.tm_mon)
    print(localtime.tm_mday)
    asc_time = time.asctime(localtime)
    print(asc_time)
    format_time = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    print(format_time)
    parse_time = time.strptime("2017-1-1", "%Y-%m-%d")
    print(parse_time)


# A function tack return value
def f1(a, b=5, c=10):
    return a + b * 2 + c * 3


# mutable args
def f2(*args):
    sum_value = 0;
    for num in args:
        sum_value += num
    return sum_value


# **kw
def f3(**kwargs):
    if "name" in kwargs:
        print("Welcome! {}!".format(kwargs["name"]))
    elif "age" in kwargs:
        print("You age is {}".format(kwargs["age"]))
    else:
        print("Without you info!")


def my_filter(mystr):
    return len(mystr) == 6


def my_test_local_function():
    print(len("hello"))
    print(sum(range(1, 5)))
    print(abs(-10))
    print(round(10.5))
    print(pow(2, 3))
    fruits = ["orange", "peach", "durian", "watermelon"]
    print(fruits[slice(1, 3)])
    fruits2 = list(filter(my_filter, fruits))
    print(fruits)
    print(fruits2)


# 求最大公约数
def gcd(x, y):
    if x > y:
        x, y = y, x
    # 从x递减,两个数分别对循环中的数取模,当取模为0时,得到的就是最大公约数
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


# 和最小公倍数
def lcm(x, y):
    return x * y // gcd(x, y)


# 计算阶乘
def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


if __name__ == "__main__":
    # usage_model_test()
    my_test_local_function()

    # 求最大公约数和最小公倍数
    print(gcd(15, 27))
    print(lcm(15, 27))
