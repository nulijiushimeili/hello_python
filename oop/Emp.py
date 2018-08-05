"""
Script introduction: 
    抽象类 / 方法重写 / 多态
    实现一个工资结算系统 公司有三种类型的员工
        - 部门经理固定月薪12000元/月
        - 程序员按本月工作小时数每小时100元
        - 销售员1500元/月的底薪加上本月销售额5%的提成
    输入员工的信息 输出每位员工的月薪信息

@Time :       2018-08-05 22:31
@Author :     nulijiushimeili
@Site :       
@File :       Emp.py
@Software :   PyCharm
"""

from abc import ABCMeta, abstractmethod


class Emp(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Emp):

    def __init__(self, name):
        super().__init__(name)

    def get_salary(self):
        return 12000


class Programmer(Emp):
    def __init__(self, name):
        super().__init__(name)

    def set_working_hour(self, working_hour):
        self._working_hour = working_hour

    def get_salary(self):
        return 100 * self._working_hour


class Salesman(Emp):
    def __init__(self, name):
        super().__init__(name)

    def set_sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1500 + self._sales * 0.05


if __name__ == "__main__":
    emps = [Manager("Mayun"), Programmer("Leihuoming"), Salesman("taobao")]
    for emp in emps:
        if isinstance(emp, Programmer):
            working_hour = int(input("Please input {}'s work time:".format(emp.name)))
            emp.set_working_hour(working_hour)
        elif isinstance(emp, Salesman):
            sales = int(input("Please input {}'s sales:".format(emp.name)))
            emp.set_sales(sales)
        print("{} current salaries is {} dollar.".format(emp.name, emp.get_salary()))
