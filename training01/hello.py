import math


# python hello world!
def show():
    print('hello world!')
    print("hello", "world!")
    print('hello', 'world', sep=", ", end="!")
    print('goodbay world!', end='\n')


# test input from console
def change_wendu():
    f = float(input("请输入华氏温度:"))
    c = (f - 32) / 1.8
    print("%.f华氏度 = %.f摄氏度" % (f, c))


# test math
def calc_circle():
    radius = float(input("Please input the circle radius"))
    perimeters = 2 * math.pi * radius
    area = math.pi * radius * radius
    print("The circle's perimeter is : {}".format(perimeters))
    print("The circle's area is : {}".format(area))


# test is leap (闰年)
def check_year():
    year = int(input("Please input the year:"))
    is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
    print(is_leap)


# test perator
def calc():
    a, b, c, d, e = 5, 10, 3, 4, 5
    a += b
    print("a = {}".format(a))
    a -= c
    print("a = {}".format(a))
    a *= d
    print("a = {}".format(a))
    a /= e
    print("a = {}".format(a))
    flag1 = 3 > 2
    flag2 = 2 < 1
    flag3 = flag1 and flag2
    flag4 = flag1 or flag2
    flag5 = not flag2
    print("flag1 = {}")
    print("flag2 = {}")
    print("flag3 = {}")
    print("flag4 = {}")
    print("flag5 = {}")
    print(flag1 is True)
    print(flag1 is not False)


# test string
def operator_string():
    str1 = "hello world !"
    print("The string's length is {}".format(len(str1)))
    print("The title of string is {}".format(str1.title()))
    print("To upper case the string, and is {}".format(str1.upper()))
    print("The string is upper? ---- {}".format(str1.isupper()))
    print("The string is start with 'hello'? ---- {}".format(str1.startswith("hello")))
    print("The string is end with 'hello'? ---- {}".format(str1.endswith("hello")))
    str2 = "Aa"
    print(str2)
    str3 = str1.title() + " " + str2.lower()
    print(str3)


# test virable
def test_variable():
    print("Input two numbers and calc them.")
    a = int(input("Please input a number:"))
    b = int(input("Please input another number:"))
    print("{} + {} = {}".format(a, b, (a + b)))
    print("{} - {} = {}".format(a, b, (a - b)))
    print("{} / {} = {}".format(a, b, (a / b)))
    print("{} // {} = {}".format(a, b, (a // b)))
    print("{} * {} = {}".format(a, b, (a * b)))
    print("{} ** {} = {}".format(a, b, (a ** b)))
    print("{} % {} = {}".format(a, b, (a % b)))


# test type
def test_type():
    a, b, c, d, e, f, g = 100, 10000000000, 12.253, 1 + 5j, 'A', "hello,world!", True
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))
    print(type(g))
