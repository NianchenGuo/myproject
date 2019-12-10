# coding=utf-8
"""
作者：郭伟伟
简介：导入单个类
日期：2019-12-10
"""
# 从一个模块中导入多个类
from car import Car, ElectricCar
my_beetle = Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "roadster", 2017)
print(my_tesla.get_descriptive_name())


# 导入整个模块
import car

my_beetle = car.Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar("tesla", "roadster", 2017)
print(my_tesla.get_descriptive_name())