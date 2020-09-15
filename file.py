#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演示文件的读取与写入
"""
import csv

# 写入文件（覆盖）
with open('output\\text.txt', 'w', encoding="utf-8") as f:
    f.write('你好！')
    f.write('\n你好！')
    f.write('\n你好！')

# 写入文件（文件末尾追加）
with open('output\\text.txt', 'a', encoding="utf-8") as f:
    f.write('\n你好！')

# 读取文件
with open("output\\text.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        print(line.strip())

# 写入CSV文件
data = [{"name": "宝宝", "sex": "女", "age": "18"},
        {"name": "嘻嘻", "sex": "女", "age": "18"},
        {"name": "哈哈", "sex": "女", "age": "18"}]

with open('output\\input.csv', 'w', encoding="GBK") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "sex", "age"])
    writer.writeheader()
    writer.writerows(data)

# 读取CSV文件
with open("output\\input.csv", "r", encoding="GBK") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line)
