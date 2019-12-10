# coding=utf-8
"""
作者：郭伟伟
简介：类
日期：2019-12-09

"""


class Dog():
    """  定义一个狗类 """
    def __init__(self, name, age):
        """ 初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """ 模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """ 模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over ! ")


my_dog = Dog("willie", 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()


class Restaurant():
    """ 建立一个名为Restaurant的类 """
    def __init__(self, restaurant_name, cuisine_type):
        """ 初始化属性restaurant_name / cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(" This is a restaurant called " + self.restaurant_name.title() + ".")
        print(" The " + self.cuisine_type + " is mainly young people.")

    def open_restaurant(self):
        print(" The " + self.restaurant_name + " is open now. ")


my_restaurant = Restaurant("Lou wai lou", "The young man")
print(" My restaurant name is " + my_restaurant.restaurant_name.title() + ".")
print(" My restaurant " + my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant("Hot pot", "sichuang")
your_restaurant.describe_restaurant()


class User():
    """ 创建一个名为User的类 """
    def __init__(self, first_name, last_name):
        """ 包含的属性有"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name + "." + self.last_name + " height is 168 and his weight is 60kg.")

    def greet_user(self):
        print("Hello," + self.first_name + "." + self.last_name + " nice to meet you.")


My_uncle = User("Browning", "le")
My_uncle.describe_user()
My_uncle.greet_user()


class Car():
    """ 一次模拟汽车的简单尝试 """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 20

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + "miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """ 电动车的独特之处"""

    def __init__(self, make, model, year):
        """ 初始化父类的属性 """
        super().__init__(make, model, year)
        # 新增属性self.battery_size
        self.battery_size = 70

    # 添加一个名为describe_battery() 的方法
    def describe_battery(self):
        """ 打印一条描述电瓶容量的消息 """
        print(" This car has a " + str(self.battery_size) + "-kwh battery.")

    def fill_gas_tank(self):
        """ 电动汽车没有油箱 """
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()




