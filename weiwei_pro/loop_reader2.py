# coding=utf-8
import csv
# 获取本地CSV文件
my_file = "C:\\my\\github\\weiwei_pro\\userinfo.csv"

data = csv.reader(filter(my_file, "rb"))

# 循环输出每一行信息
for user in data:
    print(user[0])



