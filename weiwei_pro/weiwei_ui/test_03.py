# coding = utf-8
"""
功能：云教学教师端新建课堂
作者：郭伟伟
日期：20191112

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

# 点击课表管理
browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/div[3]/div[1]").click()

time.sleep(1)
# 点击创建临时课堂
browser.find_element_by_xpath("/html/body/div[4]/div/div/div[4]/div/div[2]/div"
                              "/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[9]").click()

time.sleep(3)

# 点击绑定资源的选择课件按钮
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[5]/div[2]/div[2]/div[6]/div[1]/a").click()

# 点击添加资源按钮
browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div/div/div[2]/div[2]/"
                              "div/div/table/tbody/tr[1]/td[5]/a[2]").click()

# 点击关闭添加课件页面
browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/button/span").click()

time.sleep(2)

# 点击添加学生按钮
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[5]/div[2]/div[2]/div[1]/div[3]/div/div").click()

# 点击添加图标
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[5]/div[2]/div[2]/div[2]/div[1]/div/div").click()

time.sleep(2)
# 选择班级
browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/"
                              "div/table/tbody/tr[1]/td[1]/input").click()

# 点击确认按钮
browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div[2]/button[1]").click()

# 点击保存按钮
browser.find_element_by_xpath('//*[@id="setiainfo-btn"]').click()


# 点击课中按钮
browser.find_element_by_xpath('//*[@id="dropdownClassMd"]').click()

# 点击课堂选择
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ul/li[1]/a").click()

# 选择第一节课
browser.find_element_by_xpath("/html/body/div[5]/div/div/table/tbody/tr/td/div[1]").click()

time.sleep(3)
# 进入课堂，点击确定按钮
browser.find_element_by_xpath("/html/body/div[3]/div/div/div[11]/div/div/div[2]/button").click()