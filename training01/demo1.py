import time
import math
import random
from random import randint

"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""


def get_perfect_number():
    start = time.clock()
    for num in range(1, 10000):
        sum_value = 0
        for factor in range(1, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                sum_value += factor
                # if factor > 1 and num / factor != factor:
                if 1 < factor != num / factor:
                    sum_value += num / factor
        if sum_value == num:
            print(num)
    end = time.clock()
    print("Tack time:", (end - start), "s")


"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
"""


def get_palindrome_number():
    num = int(int("Please input a unsigned integer:"))
    temp = num
    num2 = 0
    while temp > 0:
        num2 *= 10
        num2 += temp % 10
        temp //= 10
    if num == num2:
        print("{} is palindrome.".format(num))
    else:
        print("{} is not palindrome.".format(num))


"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
"""


def get_lily_number():
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 2 + high ** 3:
            print(num)


"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""


def guess_number():
    answer = random.randint(1, 100)
    counter = 0
    while True:
        number = int(input("Please input a number : "))
        counter += 1
        if number > answer:
            print("It is too big, please guess again.")
        elif number < answer:
            print("It si too little , please guess agagin.")
        else:
            print("Congratulations! You get it.")
            break
    print("You guess it total %d times." % counter)
    if counter > 7:
        print("You are so stupid.")


"""
斐波那契数列
"""


def fibonacci():
    number = int(input("请输入你要查看的是斐波那契数列的几位数字:"))
    a, b = 0, 1
    for _ in range(number):
        a, b = b, (a + b)
        print(a)


"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""


def gamble():
    money = 1000
    while money > 0:
        print('你的总资产为:', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注: '))
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True

        while needs_go_on:
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜')
                money -= debt
                needs_go_on = False
            elif current == first:
                print('玩家胜')
                money += debt
                needs_go_on = False

    print('你破产了, 游戏结束!')


"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只
"""


def calc_chicken():
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if x * 5 + y * 3 + z / 3 == 100:
                print("公鸡:{}\t母鸡:{}\t小鸡:{}".format(x, y, z))


if __name__ == "__main__":
    # fibonacci()
    # guess_number()
    calc_chicken()
