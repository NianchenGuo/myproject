# coding=utf-8
"""
作者：郭伟伟
简介：
请创建一个Die 类，它包含一个名为sides 的属性，该属性的默认值为6。
编写一个名为roll_die() 的方法，它打印位于1和骰子面数之间的随机数。
创建一个6面 的骰子，再掷10次。
创建一个10面的骰子和一个20面的骰子，并将它们都掷10次。
日期：2019-12-10
"""

from random import randint


class Die():

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        x = randint(1, 6)
        self.sides = x
        print(self.sides)

    def roll_die10(self):
        """ 创建一个10面的骰子 """
        x = randint(1, 10)
        self.sides = x
        print(self.sides)

    def roll_die20(self):
        """ 创建一个20面的骰子 """
        x = randint(1, 20)
        self.sides = x
        print(self.sides)


die = Die()
print(die.sides)
print("6 sides")
for i in range(0, 10):
    die.roll_die()
print("10 sides")
for i in range(0, 10):
    die.roll_die10()
print("20 sides")
for i in range(0, 10):
    die.roll_die20()



