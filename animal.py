#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演示类的继承
"""


class Animal(object):
    def run(self):
        print("animal is running ...")


class Dog(Animal):
    def run(self):
        print("dog is running ...")


class Cat(Animal):
    pass


try:
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()
except BaseException as e:
    print("异常:", e)
finally:
    print("finally")
