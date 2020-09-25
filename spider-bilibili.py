#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

if __name__ == "__main__":
    driver_url = r"D:\software\edgedriver_win64\msedgedriver.exe"
    browser = webdriver.Edge(executable_path=driver_url)
    browser.get("https://www.bilibili.com/")
    WAIT = WebDriverWait(browser, 10)
    # 关键词输入框
    input_button = WAIT.until(ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/form/input")))
    # 搜索按钮
    submit = WAIT.until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/form/div/button")))
    # 模拟搜索
    input_button.send_keys('蔡徐坤 篮球')
    submit.click()

    print("跳转到新的窗口")
    # 所有的tab页数量
    all_h = browser.window_handles
    # 浏览器切换到第二个tab
    browser.switch_to.window(all_h[1])
    # 搜索结果
    WAIT.until(ec.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul")))

    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    video_list = soup.find_all(class_="video-item matrix")

    for video in video_list:
        url = video.a["href"]
        title = video.find(class_="headline clearfix").a["title"]
        watch_num = video.find(class_="headline clearfix").find(class_="so-icon watch-num").text
        danmu_num = video.find(class_="headline clearfix").find(class_="so-icon hide").text
        up_time = video.find(class_="headline clearfix").find(class_="so-icon time").text
        uper = video.find(class_="headline clearfix").find(class_="so-icon").a.text
        print(url, title, watch_num, danmu_num, up_time, uper)
