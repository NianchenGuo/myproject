# coding=utf-8
"""
作者：郭伟伟
功能：测试函数
日期：2019-12-11
"""


def get_formatted_name(first, last, middle=""):
    """ Generate a neatly formatted full name """
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last

    return full_name.title()


