from random import randint
import math


# test if elif else
def test_if01():
    value = float(input("Please input length:"))
    unit = input("Please input unit:")
    if unit == "in":
        print("{}in = {}cm".format(value, value * 2.54))
    elif unit == "cm":
        print("{}cm = {}in".format(value, value / 2.54))
    else:
        print("Please input legitimate parameter!!!")


# test if 2
def test_if02():
    score = int(input("Please input your grade:"))
    grade = ""
    if score > 100 or score < 0:
        print("Please input legitimate parameter!!!")
    else:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "E"
    print("Your grade is : {}".format(grade))


# a game
def test_random():
    random_value = randint(1, 5)
    if random_value == 1:
        result = "Singing"
    elif random_value == 2:
        result = "Dancing"
    elif random_value == 3:
        result = "Say story"
    elif random_value == 4:
        result = "Jump 10 times"
    else:
        result = "Say 'wang! wang! wang! ' like a dog."
    print(result)


# make triangle
def calc_triangle():
    print("Please input triangle every side length and check: ")
    a = float(input("Please input a :"))
    b = float(input("Please input b :"))
    c = float(input("Please input c :"))
    if a + b > c and a + c > b and b + c > a:
        print("It is a triangle, and it's perimeter is : {}".format(a + b + c))
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("The area of this triangle is : {}".format(area))
    else:
        print("It is not a triangle.")


# login check
def check_login():
    username = input("Please input your username:")
    password = input("Please input your password:")
    if username is "admin" and password is "123456":
        print("Login success!")
    else:
        print("Username or password is wrong, please check them.")
        print("Login failed.")


if __name__ == "__main__":
    test_random()
    # test_if01()
    test_if02()
