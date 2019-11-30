# coding:utf-8
# 博客园cookie 绕过验证码登录
import requests
import urllib3
import re

urllib3.disable_warnings()
# 先打开登录首页，获取部分cookie
url = "https://passport.cnblogs.com/user/signin"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
}  # get 方法其它加个 ser-Agent 就可以了

s = requests.session()
r = s.get(url, headers=headers, verify=False)
print(s.cookies)

# 添加登录需要的两个 cookie
c = requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie', '8A678C0982517938DB2B6D3B96A429E0654ECC60E279521F2C1C965DC'
                        '731C9883DCECAEEC5DF76B2E42C48A24870DC36099B27DA4D05CF5A1B77'
                        'BE9FFDE6A6CD2962B1382BE6DA860046DC14F9F95A5DD8D60D6E')  # 填上面抓包内容
c.set('.Cnblogs.AspNetCore.Cookies', 'CfDJ8DeHXSeUWr9KtnvAGu7_dX9C0emicIHZv1f8a83J2V'
                                     'aOrWzbQEeqmBOwFoRLoZNvBNEaa-nrC9JsYoKD0__WRTbk'
                                     'FK69VXftNcfJaSX2CJiCM_mdPL8-7wIK4ekilHBb0WmW9nJ'
                                     'vbVjU2BV5fcb8pQOMFxsY3AOhCYstjV0KjxSlwXffAdeYhFr'
                                     'J86f0-SqoJvkVoZWUX2F25xVLSJpCZKomS58mG0vUgjKuoLg'
                                     'QxjiHkPWrI-sgh_lh_Ax1Kuo03FGpUw3Uxt160kVnITSZbES'
                                     'LP64y26ROpjQyuXYfnKQ6PkAINX2xUeoXMSFcXvKRFjbuka_Pg5dU'
                                     '72_TJ0otm-ipcwZ9okL1GAyF4gPtZIlSaJ3OHFvnAeDOMVtMQGUMEN'
                                     'nrNN1y002N6SfCyo2PHlFHNjxrscWBpmM6MjW63M5P8PjlfrRpa9NBn'
                                     'VG3YTX1QCttSAWrDmdlmHDC6w3ChRib6Y-dDFwdR1qO5LWfZAaIRJ2P'
                                     'I1HZ5jmxx0jGK5I2p65KRcBkCiMEMUyJO2pivrpBrB-fFQohqp0alOMj'
                                     'COJWon9Oiyr7_u2IBM_tYgSXew')  # 填上面抓包内容
c.set('AlwaysCreateItemsAsActive', "True")
c.set('AdminCookieAlwaysExpandAdvanced', "True")
s.cookies.update(c)
print(s.cookies)

# 登录成功后保存编辑内容
r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers, verify=False)
# 保存草稿箱
url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "FE27D343",
        "Editor$Edit$txbTitle": "这是guoweiwei",
        "Editor$Edit$EditorBody": "<p>这里guoweiwei： "
                                 "https://www.cnblogs.com/weiwei0304/</p>",
        "Editor$Edit$Advanced$ckbPublished": "on",
        "Editor$Edit$Advanced$chkDisplayHomePage": "on",
        "Editor$Edit$Advanced$chkComments": "on",
        "Editor$Edit$Advanced$chkMainSyndication": "on",
        "Editor$Edit$Advanced$txbEntryName": "",
        "Editor$Edit$Advanced$txbExcerpt": "",
        "Editor$Edit$Advanced$tbEnryPassword": "",
        "Editor$Edit$lkbDraft": "存为草稿",
        }
r2 = s.post(url2, data=body, verify=False)
print(r2.url)

# 第三步：正则提取需要的参数值
postid = re.findall(r"postid=(.+?)&", r2.url)
print(postid)
# 提取为字符串
print(postid[0])

# 第四步：删除草稿箱
url3 = "https://i.cnblogs.com/post/delete"
json3 = {"postId": postid[0]}
r3 = s.post(url3, json=json3, verify=False)
print(r3.json())