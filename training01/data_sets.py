"""
输出10行的杨辉三角 - 二项式的n次方展开系数
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
... ... ...
"""


def yanghui_triangle():
    num = int(input("Number of rows : "))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end="\t")
        print()


# tuple test
def tuple_test():
    t = ("hello", 23, True, "New York")
    print(t)
    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])
    # show all elements
    for member in t:
        print(member)
    # flush tuple value
    t = ("world", 26, False, "China")
    print(t)
    person = list(t)
    print(person)
    person[0] = "Jack"
    person[1] = 28
    print(person)
    fruits_list = ["apple", "banana", "orange"]
    fruits_tuple = tuple(fruits_list)
    print(fruits_list)
    print(fruits_tuple)


# curd in list
def list_test():
    fruits = ["grape", "apple", "strawberry", "waxberry"]
    print(fruits)
    print(fruits[0])
    print(fruits[1])
    print(fruits[-1])
    print(fruits[-2])
    fruits[3] = "banana"
    print(fruits)
    fruits.append("pitaya")
    fruits.insert(0, "apple")
    print(fruits)
    del fruits[1]
    print(fruits)
    fruits.pop()
    print(fruits)
    fruits.pop(0)
    print(fruits)
    fruits.remove("apple")
    print(fruits)


# list slice
# 分片操作只是创建了索引,并没有复制出新的对象
# 切片操作中间的都是前开后闭的,包含起始位置,不包含终止位置
def list2_test():
    fruits = ["grape", "apple", "strawberry", "waxberry"]
    fruits += ["pitaya", "pear", "mango"]
    # foreach list
    for fruit in fruits:
        print(fruit.title(), end="")
    print()
    # list slice
    fruits2 = fruits[1:4]
    print(fruits2)
    # 并没有创建新的列表,只是创建了引用
    fruits3 = fruits[:]
    print(fruits3)
    # 从倒数第三个开始不包含倒数第一个
    fruits4 = fruits[-3:-1]
    print(fruits4)
    fruits5 = fruits[::-1]
    print(fruits5)


# fibonacci 数列生成器
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


# generate list
def generate_list():
    list1 = list(range(1, 11))
    print(list1)
    list2 = [x * x for x in range(1, 11)]
    print(list2)
    list3 = [m + n for m in "ABCDEFG" for n in "12345"]
    print(list3)
    print(len(list3))
    # generator (节省空间,但是生成下一个数值的时候需要花费时间)
    gen = (m + n for m in "abcdefg" for n in "12345")
    print(list(gen))
    for elem in gen:
        print(elem, end=" ")
    print()
    gen = fibonacci(20)
    print(list(gen))
    for elem in gen:
        print(elem, end="")
    print()


if __name__ == "__main__":
    # tuple_test()
    # list_test()
    # list2_test()
    # print(list(fibonacci(20)))
    generate_list()
