# coding=utf-8
"""
作者：郭伟伟
功能：测试单个函数
日期：2019-12-11
"""

import unittest

from city_functions import national_city_name


class CityName(unittest.TestCase):

    def test_city_country(self):
        national_name = national_city_name('santiago', 'chile')
        self.assertEqual(national_name, "Santiago Chile")

    def test_city_country_population(self):
        national_name = national_city_name('santiago', 'chile', "5000000")
        self.assertEqual(national_name, "Santiago 5000000 Chile ")


unittest.main()
