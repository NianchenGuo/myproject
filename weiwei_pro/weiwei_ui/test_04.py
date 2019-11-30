# coding = utf-8
"""
功能：云教学教师端批改作业
作者：郭伟伟
日期：20191121

"""

from selenium import webdriver

import time

browser = webdriver.Firefox()

browser.get("http://hd.ruizhiedu.com:8888/pallasa_cloudteach/teacher/index/index")

browser.maximize_window()  # 将浏览器最大化显示

browser.find_element_by_id("username").send_keys("01019992gww")  # 云教学教师web端输入用户名

browser.find_element_by_id("password").send_keys("123456")    # 云教学教师web端输入密码

browser.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form/div[4]/button").click()    # 点击登录按钮

time.sleep(3)

# 点击首页的批阅作业按钮
browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[4]/div[1]").click()

time.sleep(2)
# 点击首次作业的批阅按钮
browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div/"
                              "table/tbody/tr[1]/td[7]/div/a[3]/p").click()
time.sleep(1)
# 点击第一题的批阅按钮
browser.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[6]/a/img").click()

# 第一题给分
browser.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/div[1]/div[2]/"
 
                              "div/div[2]/div/div/label/label/div[1]/input").click()
time.sleep(2)
# 给分
browser.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/div[1]/div[2]/"
                              "div/div[2]/div/div/label/label/div[1]/div[3]/a[2]").click()
time.sleep(1)

# 下一题
browser.find_element_by_id("next").click()

time.sleep(1)
# 点击关闭按钮
browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/button/span").click()

time.sleep(1)
# 点击返回作业列表
# browser.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div[2]/div[1]/div/a").click()

time.sleep(1)

# 点击退出按钮
browser.find_element_by_id("cls-closepage").click()

time.sleep(1)

# 点击弹出窗的确定退出按钮
browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[3]/button[1]").click()

# 关闭浏览器
browser.quit()

