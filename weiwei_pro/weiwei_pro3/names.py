# coding=utf-8
"""
作者：郭伟伟
功能：测试函数
日期：2019-12-11
"""

from name_function import get_formated_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formated_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")

