# coding=utf-8
"""
作者：郭伟伟
功能：测试函数
日期：2019-12-11
"""
import unittest  # 导入了模块unittest
from name_function import get_formatted_name  # 导入要测试的函数get_formatted_name()
# from formatted_name import get_formatted_names


class NamesTestCase(unittest.TestCase):    # 创建了一个名为NamesTestCase 的类，继承unittest.TestCase 类
    """ 测试name_function.py """
    def test_first_last_name(self):
        """ 能够正确处理像Janis Joplin这样的姓名吗？ """
        # 使用实参'janis' 和'joplin' 调用get_formatted_name() ，并将结果存储到变量formatted_name 中
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfwang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfwang Amadeus Mozart')


unittest.main()

