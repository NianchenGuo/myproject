# coding=utf-8
"""
作者：郭伟伟
简介：函数---导入整个模块
日期：2019-12-05
"""


def make_pizza(size, *toppings):
    """ 概述要制作的披萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("--" + topping)
