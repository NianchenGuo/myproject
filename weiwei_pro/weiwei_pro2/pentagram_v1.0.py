"""
作者：郭伟伟
功能：绘制五角星
版本号：V1.0
日期：2019/11/27
"""
import turtle


def main():
    """
    主函数
    """
    # 计数器
    count = 1

    while count <= 5:
        turtle.forward(100)
        turtle.right(144)
        count = count + 1
    turtle.exitonclick()


if __name__ == '__main__':
    main()
