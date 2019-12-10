# coding=utf-8
"""
作者：郭伟伟
简介：
从文件中读取数据
日期：2019-12-10
"""
with open("pi_digits.txt") as file_object:
    """ 函数open() 接受一个参数：要打开的文件的名称 """
    contents = file_object.read()

    print(contents.rstrip())


# 绝对路径读取文件
file_path = "C:\\my\\MyProject\\myproject\\weiwei_pro\\weiwei_pro3\\pi_digits.txt"
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 　逐行读取
filename = "pi_digits.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

