# 这里介绍全局和局部变量的使用
'''
全局变量：在当前.py文件内，都随意地方都可以调用，例如函数内部调用全局变量
局部变量：局部变量一般定义在函数体内部，只能当前这个函数调用，超过这个范围，其他无权访问
这个局部变量
'''
 
x = 6


def printFuc():
    y = 8
    z = 9
    print(y + z)
    print(x)  # 函数内部可以调用局部变量


printFuc()
# print(y)  提示y没有定义，这个地方调用局部变量会报错
