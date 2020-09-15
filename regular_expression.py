#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.*  表示贪婪模式，获取最长的满足条件的字符串
.*? 表示非贪婪模式，获取最短的满足条件的字符串
"""
import re

content = """
邮箱密码是：12pass。
QQ密码是：kkk。
银行密码是：谢谢谢谢。
手机密码是：也一样。
"""
# re.S 标识忽略换行符，返回的是一个list
password1 = re.findall("：(.*?)。", content, re.S)
print(password1)

# 返回第一个元素后就停止后面的检索
password2 = re.search("：(.*?)。", content, re.S)
print(password2.group(1))


