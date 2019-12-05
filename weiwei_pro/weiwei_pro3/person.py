# coding=utf-8
"""
作者：郭伟伟
简介：函数返回字典
日期：2019-12-03
"""


def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {"first": first_name, "last": last_name}
    return person


musician = build_person("jimi", "hendrix")
print(musician)
