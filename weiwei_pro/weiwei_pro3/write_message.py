# coding=utf-8
"""
作者：郭伟伟
功能：写入文件
日期：2019-12-11
"""

# 写入空文件
filename = "programing.txt"
with open(filename, "w") as file_object:
    file_object.write(" l love python !\n")
    file_object.write(" l love creating new games. \n")

# 附加到文件
filename = "programing.txt"
with open(filename, "a") as file_object:
    file_object.write(" l also love finding meaning in large datasets.\n")
    file_object.write(" l love creating apps that can run in a browser.\n")


