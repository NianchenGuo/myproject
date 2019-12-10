# coding=utf-8
"""
作者：郭伟伟
简介：导入单个类
日期：2019-12-10
"""

from car import ElectricCar

my_tesla = ElectricCar("tesla", " model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()