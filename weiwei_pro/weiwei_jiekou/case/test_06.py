# coding = utf-8
"""
云教学教师端布置作业功能
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

browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/div[4]/div[3]").click()  # 点击布置作业按钮

time.sleep(1)
# 添加学生按钮
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[4]/div[2]/div[2]/div[2]/div/div/div").click()

# 选择班级
browser.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div[1]/div/div[1]/div[1]/div[1]/div[2]/ul"
                              "/li[4]/div[1]").click()
time.sleep(1)
# 点击确认按钮
browser.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div[2]/button[1]").click()

time.sleep(1)
# 点击添加题目按钮
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[4]/div[2]/div[2]/div[1]/div[3]/div/div").click()

# 点击我的题库
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[4]/div[2]/div[2]/div[5]/div[1]/button[1]").click()

time.sleep(2)
# 点击添加题库
browser.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div/div/div[2]/div[2]/div/div/"
                              "table/tbody/tr[1]/td[6]/a[2]").click()
time.sleep(2)
# 点击关闭弹框
browser.find_element_by_xpath("/html/body/div[8]/div/div/div[1]/button/span").click()

time.sleep(1)
# 输入作业名称
browser.find_element_by_xpath('//*[@id="homeworkName"]').send_keys("20191112新建作业")


# 发送时间选择
browser.find_element_by_xpath('//*[@id="sendTime"]').send_keys("2019/11/12 14:00")

# 截止时间选择
browser.find_element_by_xpath('//*[@id="endTime"]').send_keys("2019/11/30 14:00")

# 限时时间长
browser.find_element_by_xpath('//*[@id="hw_limitminutes"]').send_keys("60")


# 备注信息输入
browser.find_element_by_xpath('//*[@id="remark"]').send_keys("把握时间及时完成，批改后返还答案")

time.sleep(3)
# 查看老师批改情况
browser.find_element_by_xpath('//*[@id="returnremark"]').click()

# 点击发送作业
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[4]/div[1]/table/tbody/tr[13]/td/div/a[1]").click()