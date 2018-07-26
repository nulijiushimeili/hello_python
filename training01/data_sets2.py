from random import randrange, randint, sample
import os
import time


# show the balls number
def display(balls):
    """
    show those ball numbers from list:
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print("|", end="")
        print("%02d" % ball, end=" ")
    print()


# get random numbers
def random_select():
    """
    get random numbers list.
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    for _ in range(6):
        index = randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index]
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


# This is a process call. Running from here.
def double_color_ball_test():
    n = int(input("Please input you selected times:"))
    for _ in range(n):
        display(random_select())


# marque test 跑马灯
def marque_test():
    string = 'Welcome to python world!         '
    while True:
        print(string)
        time.sleep(0.2)
        string = string[1:] + string[0:1]
        # for Windows use os.system('cls') instead
        os.system('clear')


# input student grade and show scores table.
def show_student_grade_table():
    names = ["Guanyu", "Zhangfei", "Zhaoyun", "Machao", "Huangzhong"]
    subjs = ["Chanese", "math", "English"]
    scores = [[0] * 3] * 5
    for row, name in enumerate(names):
        print("Please input %s's grade." % name)
        for col, subj in enumerate(subjs):
            scores[row][col] = float(input(subj + ": "))
    print(scores)


# test set
def set_test():
    set1 = {1, 2, 4, 4, 5, 6, 6}
    print(set1)
    print("The length of set is : {}".format(len(set1)))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(3)
    set1.add(4)
    set1.add(5)
    print(set1)
    set2.update([11, 12])
    print(set2)
    # 丢弃操作,丢弃集合中的某个元素
    set2.discard(5)
    print(set2)
    # remove 的元素如果不存在会抛异常(keyError)
    if 4 in set2:
        set2.remove(4)
    print(set2)
    for elem in set2:
        print(elem ** 2, end=" ")
    print()
    # 将元祖转换成集合
    t = (3, 4, 5, 66, 7)
    set3 = set(t)
    print(set3.pop())
    print(set2)


# set集合的交集,并集,差集
def set2_test():
    set1 = set(range(1,7))
    print(set1)
    set2 = set(range(2,11,2))
    print(set2)
    set3 = set(range(1,5))
    print(set3)
    # 交集
    print(set1 & set2)
    # 并集
    print(set1 | set2)
    # 差集
    print(set1 - set2)
    # 各自独有的元素组成的集合
    print(set1 ^ set2)

    print(sum(set1))
    print(sum(set2))
    print(sum(set3))

    print(set2 <= set1)
    print(set3 <= set1)
    print(set1 >= set2)
    print(set1 >= set3)


if __name__ == "__main__":
    # marque_test()
    # show_student_grade_table()
    # set_test()
    set2_test()
