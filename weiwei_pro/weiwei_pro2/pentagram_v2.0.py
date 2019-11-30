"""
作者：郭伟伟
功能：绘制五角星
版本号：V1.0
日期：2019/11/27
新增功能：添加循环可以进行重复绘制五角星
"""
import turtle


def draw_pentagram(size):
    """
    # 绘制五角星的功能
    """
    # 计数器
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def main():
    """
    # 主函数
    """
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor("red")
    size = 100
    while size <= 200:
        # 调用函数
        draw_pentagram(size)
        size += 10
    turtle.exitonclick()


if __name__ == '__main__':
    main()
