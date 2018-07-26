from random import randint
import math

'''
面向对象版本的猜数字游戏
'''


class GuessMachine(object):
    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None

    def reset(self):
        self._answer = randint(1, 100)
        self._counter = 0
        self._hint = None

    def guess(self, your_answer):
        self._counter += 1
        if your_answer > self._answer:
            self._hint = "It is too big."
        elif your_answer < self._answer:
            self._hint = "It is too little."
        else:
            self._hint = "Congratulations! You get it."
            return True
        return False

    @property
    def counter(self):
        return self._counter

    @property
    def hint(self):
        return self._hint


"""
修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)
"""


class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius


# test GuessMachine class
def guess_machine_test():
    gm = GuessMachine()
    play_again = True
    while play_again:
        game_over = False
        gm.reset()
        while not game_over:
            your_answer = int(input("Please input your answer."))
            game_over = gm.guess(your_answer)
            print(gm.hint)
        if gm.counter > 7:
            print("Your are so stupid!!!")
        play_again = input("Please again? (Yes | No)") == "Yes"


# test circle
def circle_test():
    radius = float(input("Please input the radius of pool."))
    small = Circle(radius)
    big = Circle(radius + 3)
    print("The wall will take $ {} dollar.".format(big.perimeter * 115))
    print("The street will take $ {] dollar.".format((big.area - small.area) * 65))


if __name__ == "__main__":
    guess_machine_test()
