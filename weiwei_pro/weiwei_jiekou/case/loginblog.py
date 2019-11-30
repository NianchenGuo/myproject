# coding:utf-8
import requests
from common.logger import Log
import urllib3
# 禁用安全请求警告
urllib3.disable_warnings()
import re


class Blog():
    s = requests.session() # 全局参数
    log = Log

    def __int__(self, s):
        self.s = s

    def login(self):
        """ 登录接口 """
        url = "https://passport.cnblogs.com/user/signin"
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                "Chrome/78.0.3904.70 Safari/537.36",
                  "Accept": "application/json, text/javascript, */*; q=0.01",
                  "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                  "Accept-Encoding": "gzip, deflate, br",
                  "Content-Type": "application/json; charset=utf-8",
                  "VerificationToken": "CfDJ8DeHXSeUWr9KtnvAGu7_dX_SboXjD_7IZDiSBweBEUVtWF3aPebkObHmG-evQURU_hWEyfUI22C"
                                       "b-McyXSImjCAo5MBHy9CeU1pPL9x-HRjV9-PRY1EKnxGLNdPqud6iTlXSn1BqkoVEVc4JzaEzbCE",
                  "Cookie": "_ga=GA1.2.1008511749.1572505058; _gid=GA1.2.259306577.1572505058; .Cnblogs.Account.Antifor"
                            "gery=CfDJ8DeHXSeUWr9KtnvAGu7_dX-PdiKTrtduzBmF6WkkqzwUbAWdflIImRN5V7wxJyW75ZWBjSGzhobjYo3Z"
                            "gMOy8sEUsiE08zXBM6IxmMlMfpxvg88F4bP-YzrPdbtSyVG4yekz_uCvuAUgtd-9_fv2Fgg; .Cnblogs.Account."
                            "Session=CfDJ8DeHXSeUWr9KtnvAGu7%2FdX%2B4d11fbNQ4LolGWxEn8o6KPI0SGnwcC2rg6oHAP9aTUBC3xCQXX"
                            "JHwcgevEagaMu7DELI7jXXU1hS4jYFmzalAGyUa1ZBQVe0YXt8dV%2BMec4KSoUpmAezIrKqezSUhVh%2BAP5wat3"
                            "cJKRdCyGmtSrYh; SERVERID=cbef8bde39e0b32efe96ab20d8e56145|1572505212|1572505062",
                  "X-Requested-With": "XMLHttpRequest",
                  "Connection": "keep-alive",
                  "Content-Length": "385"
                  }
        json_data = {"LoginName": "GuoWWEI",
                     "Password": "nianchen_0727",
                     "remember": True}
        res = self.s.post(url, headers=header, json=json_data, verify=False)
        result1 = res.content  # 字节输出
        print(result1)
        return res.json()

    def save(self, title, body):
        """保存草稿箱：
        参数 1：title  # 标题
        参数 2：body   # 中文"""
        url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
        d = {"__VIEWSTATE": "",
             "__VIEWSTATEGENERATOR": "FE27D343",
             "Editor$Edit$txbTitle": title,
             "Editor$Edit$EditorBody": "<p>%s</p>" % body,
             "Editor$Edit$Advanced$ckbPublished": "on",
             "Editor$Edit$Advanced$chkDisplayHomePage": "on",
             "Editor$Edit$Advanced$chkComments": "on",
             "Editor$Edit$Advanced$chkMainSyndication": "on",
             "Editor$Edit$lkbDraft": "存为草稿",
             }
        r2 = self.s.post(url2, data=d, verify=False)  # 保存草稿箱
        print(r2.url)
        return r2.url

    def get_postid(self, r2_url):
        """正则表达式提取"""
        postid = re.findall(r"postid=(.+?)&", r2_url)
        print(postid)  # 这里是 list []
        #  提取为字符串
        print(postid[0])
        return postid[0]

    def del_tie(self, postid):
        """删除帖子"""
        del_json = {"postId": postid}
        del_url = "https://i.cnblogs.com/post/delete"
        r3 = self.s.post(del_url, json=del_json, verify=False)
        print(r3.json()["isSuccess"])
        return r3.json()


if __name__ == "__main__":
    s = requests.session()
    Blog.login()

