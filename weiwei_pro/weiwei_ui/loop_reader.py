# coding=utf-8
import userinfo

info = userinfo.zidian()

for us, pw in info.items():
    print(us)
    print(pw)