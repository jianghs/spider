#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演示函数相关
"""
val = '张三'
print('%s个思恋，年终奖%s元' % ('牛牛', '10万'))


# 定义函数
def calAge(age):
    if age >= 18:
        print("成年人")
    else:
        print("未成年人")


# 调用函数
calAge(20)

# 演示 list
L = ["马波", "牛波", "羊波", "皮波", "水波"]
result = L[1:5]
print(result)
