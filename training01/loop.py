from math import sqrt


# test while
def test_while():
    sum_add = 0
    num = 3
    while num <= 100:
        sum_add += num
        num += 3
    print(sum_add)


# test for
def test_for01():
    sum_for = 0
    for x in range(1, 101):
        if x % 2 == 0:
            sum_add += x
    print(sum_for)


# test for 2
def test_for02():
    sum_for2 = 0
    for i in range(1, 100, 5):
        sum_for2 += i
    print(sum_for2)


# test for 3 , calc factorial
def test_factorial():
    n = int(input("Please input a integer: "))
    res = 1
    for i in range(1, n + 1):
        res *= i
    print("{}! = {}".format(n, res))


# 根据输入的数判断是否为素数 prime number
def check_prime_number():
    num = int(input("Please input a unsigned integer:"))
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print("{} is prime number.".format(is_prime))
    else:
        print("{} is not a prime number.".format(is_prime))


# 计算输入的两个正整数的最大公约数和最小公倍数
def test05():
    x = int(input("Please input the first number:"))
    y = int(input("Please input another number:"))
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print("{} and {} 的最大公约数是:{}".format(x, y, factor))
            print("{} and {} 的最小公倍数是:{}".format(x, y, x * y // factor))
            break


"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""


def show_shape():
    row = 5
    for i in range(row):
        for _ in range(i + 1):
            print("*", end="")
        print()

    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(" ", end="")
            else:
                print("*", end="")
        print()

    for i in range(row):
        for _ in range(row - i - 1):
            print(" ", end="")
        for _ in range(2 * i + 1):
            print("*", end="")
        print()


# 九九乘法表
def print_table99():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{}*{}={}".format(j, i, i * j), end="\t")
        print()


if __name__ == "__main__":
    print_table99()
