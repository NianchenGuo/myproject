# coding=utf-8
"""
作者：郭伟伟
功能：测试函数
日期：2019-12-11
"""
import unittest
from name_function import get_formated_name

class NamesTestCase(unittest.TestCase):
    """ 测试name_function.py """
    def test_first_last_name(self):
        """ 能够正确处理像Janis Joplin这样的"""