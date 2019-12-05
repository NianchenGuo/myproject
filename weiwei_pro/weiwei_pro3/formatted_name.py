# coding=utf-8
"""
作者：郭伟伟
简介：函数返回值
日期：2019-12-03
"""


def get_formatted_name(first_name, last_name):
    """
    返回简洁的姓名
    """
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("guo", "weiwei")
print(musician)


def get_formatted_names(first_name, last_name, middle_name=""):
    """
    返回简洁的姓名
    """
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_names("jimi", "hendrix")
print(musician)