# coding=utf-8
"""
作者：郭伟伟
简介：函数---位置实参
日期：2019-12-02
"""


def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("hamster", "harry")
describe_pet("dog", "willie")
describe_pet(animal_type="cat", pet_name="jerry")  # 关键字实参


def describe_pets(pet_name, animal_type="dog"):
    """
    形参默认值

    """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pets("jerry")


def make_shirt(size, written_characters):
    """
    # 8-3 T恤 恤 ：编写一个名为make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。
    # 这个函数应打印一个句子，概要地说明T恤的尺码和字样。 使用位置实参调用这个函数来制作一件T恤；
    # 再使用关键字实参来调用这个函数。
    """
    print("The size of this T-shirt is " + size + " and it is printed with the name " + written_characters)


make_shirt("M", "China Linning")  # 位置实参

make_shirt(size="L", written_characters="Adidas")  # 关键字实参


def make_shirts(size, written_characters="'I love Python'"):
    print("A no." + size + " T-shirt emblazoned with the words " + written_characters + ".")


make_shirts("XL")


def describe_city(city_name, city_country="Iceland"):
    """
    编写一个名为describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。
    这个函数应打印一个简单的句子，如Reykjavik is in Iceland 。给用于存储国家的形参指定默认值。
    为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
    """
    print(city_name + " is in " + city_country)


describe_city("Reykjavik")
describe_city("Akureyri")
describe_city("NewYork", "America")






