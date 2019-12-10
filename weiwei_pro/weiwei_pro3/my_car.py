# coding=utf-8
"""
作者：郭伟伟
简介：导入单个类
日期：2019-12-10
"""

from car import Car

my_new_car = Car("AUDI", "A4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()