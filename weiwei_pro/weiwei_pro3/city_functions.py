# coding=utf-8
"""
作者：郭伟伟
功能：测试函数
日期：2019-12-11
"""


def national_city_name(city, country, population=""):
    """ 编写一个函数接受2个形参，一个城市名和一个国家名 National_name"""
    if population:

        national_name = city + " " + population + " " + country
    else:
        national_name = city + " " + country

    return national_name.title()
