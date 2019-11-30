# coding:utf-8
import unittest
import requests
from case.loginblog import Blog
from common.logger import Log


class Test(unittest.TestCase):
    log = Log()

    def setUp(self):
        s = requests.session()
        self.blog = Blog()

    def test_login(self):
        """测试登录用例"""
        self.log.info("------start!------")
        result = self.blog.login()
        self.log.info("调用登录结果： %s" % result)
        self.log.info("获取是否登录成功： %s" % result["success"])
        self.assertEqual(result["success"], True)
        self.log.info("------end!------")

