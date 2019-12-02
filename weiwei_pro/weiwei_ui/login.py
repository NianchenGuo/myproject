# coding = utf-8
"""
功能：云教学教师端新建课堂
作者：郭伟伟
日期：20191112

"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import userinfo

# 登录模块
# source = open("C:\\my\\github\\weiwei_pro\\username.txt")
# un = source.read()
# source.close()
#
# source2 = open("C:\\my\\github\\weiwei_pro\\password.txt")
# pw = source2.read()
# source2.close()

# 通过2个变量，来接收调用函数获得用户名和密码
us, pw = userinfo.fun()

# 打印2个变量
print(us, pw)


def login(self):

    driver = self.driver
    driver.maximize_window()

    driver.maximize_window()  # 将浏览器最大化显示

    driver.find_element_by_id("username").clear()

    driver.find_element_by_id("username").send_keys(us)  # 云教学教师web端输入用户名

    driver.find_element_by_id("password").clear()

    driver.find_element_by_id("password").send_keys(pw)    # 云教学教师web端输入密码

    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form/div[4]/button").click()    # 点击登录按钮

    time.sleep(3)

