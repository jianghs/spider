#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演示文件的读取与写入
"""
# 读取文件
with open("C:\\Users\\jianghs430\\Desktop\\新建文本文档.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        print(line.strip())

# 写入文件（覆盖）
with open('C:\\Users\\jianghs430\\Desktop\\text.txt', 'w', encoding="utf-8") as f:
    f.write('你好！')  

# 写入文件（文件末尾追加）
with open('C:\\Users\\jianghs430\\Desktop\\text.txt', 'a', encoding="utf-8") as f:
    f.write('你好！')
