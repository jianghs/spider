#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
猜数字游戏
"""


def try_to_guess(name, answer):
    # 尝试的次数，初始化为0
    try_times = 0
    while try_times < 10:
        input_content = input("请输入一个数字：")
        guess_answer = int(input_content)
        if guess_answer < answer:
            print("你输入的数字比正确答案小！")
        elif guess_answer == answer:
            print("回答正确！")
            break
        else:
            print("你输入的数字比正确答案大！")
        try_times += 1
    else:
        print("猜错次数太多，失败！")


# 开始游戏
try_to_guess("", 50)


