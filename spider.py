#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
import csv
from bs4 import BeautifulSoup

source = requests.get("https://tieba.baidu.com/p/6970036603").content.decode()
soup = BeautifulSoup(source, "lxml")
# print(soup)
# 获取帖子内容
info = soup.find(class_="p_postlist")

# 获取帖子内容
answer_list = info.find_all(class_=re.compile("l_post*"))

data = []
for answer in answer_list:
    name = answer.find(class_=re.compile("p_author_name*"))
    content = answer.find(class_=re.compile("d_post_content j_d_post_content*"))
    obj = {"name": name.text, "content": content.text}
    data.append(obj)
    # print("作者：%s，内容：%s" % (name.text, content.text))


# 写入CSV文件
with open('output/spider_result.csv', 'w', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "content"])
    writer.writeheader()
    writer.writerows(data)


