#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演示类的权限
"""


class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


lisi = Student("李四", 22)
lisi.set_name("王五")
lisi.set_age(30)
print(lisi.get_name(), lisi.get_age())
