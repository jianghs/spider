#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver

if __name__ == "__main__":
    driver_url = r"D:\software\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(executable_path=driver_url)
    driver.get("https://www.baidu.com/")

    input_button = driver.find_element_by_css_selector('#kw')
    input_button.send_keys("马波")

    button = driver.find_element_by_css_selector('#su')
    button.click()
