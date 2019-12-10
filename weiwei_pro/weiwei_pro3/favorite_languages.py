# coding=utf-8
"""
作者：郭伟伟
简介：python标准库
日期：2019-12-10
"""

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"

for name, language in favorite_languages.items():
    print(name.title() + " 's favorite language is " + language.title() + ".")
