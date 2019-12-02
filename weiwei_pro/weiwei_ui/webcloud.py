# coding=utf-8
"""
作者：郭伟伟
功能：云教学教师端
版本号：V1.0
日期：2019/11/27
"""
from selenium import webdriver

import unittest
import time
import login
import assign_homework


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://hd.ruizhiedu.com:8888"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/pallasa_cloudteach/teacher/index/index")
        driver.maximize_window()
        # 登录
        login.login(self)

        time.sleep(3)

    def test_assign_homework(self):
        driver = self.driver
        driver.get(self.base_url + "/pallasa_cloudteach/teacher/index/index")
        driver.maximize_window()
        # 登录
        login.login(self)
        assign_homework.assign_homework(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


