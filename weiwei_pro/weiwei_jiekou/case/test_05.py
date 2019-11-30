# coding = utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()

browser.get("http://hd.ruizhiedu.com:8888/pallasa_cloudteach/teacher/index/index")

browser.maximize_window()  # 将浏览器最大化显示

browser.find_element_by_id("username").send_keys("01019992gww")  # 云教学教师web端输入用户名

browser.find_element_by_id("password").send_keys("123456")    # 云教学教师web端输入密码

browser.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form/div[4]/button").click()    # 点击登录按钮


browser.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[2]/div[4]/div[2]/img").click()    # 点击课堂选择按钮

browser.find_element_by_class_name("classname").click()    # 点击第一堂课

time.sleep(3)
browser.find_element_by_xpath("/html/body/div[3]/div/div/div[11]/div/div/div[2]/button").click()  # 点击确定按钮

time.sleep(3)
browser.find_element_by_xpath("/html/body/div[3]/div/div/div[16]/div[1]").click()   # 点击右侧扩展栏按钮

time.sleep(1)
browser.find_element_by_class_name('right-nav-stopcourse').click()  # 点击结束课堂图标

browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[3]/button[1]").click()  # 点击确定按钮

time.sleep(1)

browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/div[1]").click()  # 点击右侧扩展栏

browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/ul/li[4]/img").click()  # 点击菜单按钮

browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/div[2]/div[2]/img[1]").click()  # 点击首页按钮

time.sleep(2)
browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/div[4]/div[3]/div").click()  # 点击布置作业按钮


time.sleep(3)
# 点击添加学生
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[4]/div[2]/div[2]/div[2]/div/div/div").click()

# 点击班级
browser.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div[1]/div/div[1]/div[1]/"
                              "div[1]/div[2]/ul/li[4]/div[1]").click()

# 点击添加学生确认按钮
browser.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div[2]/button[1]").click()

#  点击添加习题按钮
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[4]/div[2]/div[2]/div[1]/div[3]/div/div").click()

# 点击我的题库
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[4]/div[2]/div[2]/div[5]/div[1]/button[1]").click()

time.sleep(3)
# 选择题库点击添加按钮
browser.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div/div/div[2]/"
                              "div[2]/div/div/table/tbody/tr[1]/td[6]/a[2]").click()

time.sleep(2)
# 关闭添加题库页面
browser.find_element_by_xpath("/html/body/div[8]/div/div/div[1]/button/span").cilck()

time.sleep(3)
# 新建作业名称输入
browser.find_element_by_xpath('//*[@id="homeworkName"]').send_keys("20191111新建作业")

time.sleep(2)
# 发送时间选择默认时间
browser.find_element_by_xpath('//*[@id="sendTime"]').send_keys("2019/11/11 16:00")

# 截止时间输入
browser.find_element_by_xpath('//*[@id="endTime"]').send_keys("2019/11/30 16:00")

# 限时时间输入
browser.find_element_by_xpath('//*[@id="hw_limitminutes"]').send_keys("60")

time.sleep(1)
# 备注信息输入
browser.find_element_by_xpath('//*[@id="remark"]').send_keys("本次作业限时60分钟，把握时间及时完成")

time.sleep(2)

# 勾选批阅后查看批阅图片
browser.find_element_by_xpath('//*[@id="returnremark"]').click()


# 点击布置作业按钮
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[4]/div[1]/table/tbody/tr[13]/td/div/a[1]").click()








# browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/div[2]/div[2]/img[2]").click()  # 点击退出按钮

# browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[3]/button[1]").click()  # 点击确定按钮


browser.quit()