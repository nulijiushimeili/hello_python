# dictionary test curd
def dic_test1():
    scores = {"yase": 30, "anqila": 16, "xiangyu": 40}
    print(scores["yase"])
    print(scores["anqila"])
    for elem in scores:
        print("{}----{}".format(elem, scores[elem]))
    scores.update(yase=28, anqila=15)
    print(scores)
    if "sunwukong" in scores:
        print(scores["sunwufong"])
    print(scores.get("sunwukong"))
    print(scores.get("yase"))
    print(scores.popitem())
    print(scores)
    scores.pop("yase")
    print(scores)
    scores.clear()
    print(scores)


# add element to dictionary and change element value.
def dic_test02():
    stu = {"name": "yase", "age": 30, "gender": "male"}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())
    for elem in stu.items():
        print(elem)
        print(elem[0], elem[1])
    if "age" in stu:
        stu["age"] = 20
    print(stu)
    # 向字典中添加属性
    stu.setdefault("score", 60)
    print(stu)
    # 无法修改字典中的属性
    stu.setdefault("score", 100)
    print(stu)
    # 可以通过这种方法为字典中的属性重新赋值
    stu["score"] = 100
    print(stu)


# calc and get fibonacci list
def fibonacci(num):
    f = [1, 1]
    for i in range(2, num):
        f += [f[i - 1] + f[i - 2]]
    for val in f:
        print(val, end=" ")


# get max value and min value from list
def get_max_min_from_list():
    fruits = ["apple", "grape", "banana", "pitaya", "waxberry", "strawberry"]
    print(max(fruits))
    print(min(fruits))
    numbers = [2, 3, 4, 5, 6, 5, 3, 6, 7]
    max_value = min_value = numbers[0]
    for num in numbers:
        if max_value < numbers[num]:
            max_value = numbers[num]
        elif min_value > numbers[num]:
            min_value = numbers[num]
    print("max_value = {}".format(max_value))
    print("min_value = {}".format(min_value))


if __name__ == "__main__":
    # dic_test1()
    # dic_test02()
    # fibonacci(20)
    get_max_min_from_list()
