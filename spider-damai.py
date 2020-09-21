#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
import csv
from bs4 import BeautifulSoup

source = requests.get("https://search.damai.cn/search.htm").content.decode()
soup = BeautifulSoup(source, "lxml")
# print(soup)
# 所有演出信息
item_box = soup.find_all(class_="item__box")

# 获取演出列表
items = item_box.find_all(class_="items")

data = []
for item in items:
    title = item.find(class_="items__txt__title")
    time = item.find_all(class_="items__txt__time")
    people = time[0]
    address = time[1]
    date = time[2]
    price = item.find_all(class_="items__txt__price")

    obj = {"title": title.text, "people": people.text, "address": address.text, "date": date.text, "price": price.text}
    data.append(obj)

print(data)

#
# # 写入CSV文件
# with open('output/spider_result.csv', 'w', encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=["name", "content"])
#     writer.writeheader()
#     writer.writerows(data)
#
#
