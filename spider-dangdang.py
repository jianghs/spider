#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
import io
import sys
from bs4 import BeautifulSoup
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb2312')


def main(page):
    url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-" + str(page)
    # html = request_dangdang(url)

    response = requests.get(url)
    response.encoding = "gb2312"
    print(response.text)
    html = BeautifulSoup(response.text, "lxml")
    book = html.find(class_="bang_list clearfix bang_list_mode")
    book_list = book.find_all("li")
    print(book_list[0])

    # # 解析过滤我们想要的信息
    # items = parse_result(html)
    #
    # for item in items:
    #     print(item)
    #     # write_item_to_file(item)


def request_dangdang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    pattern = re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }


def write_item_to_file(item):
    pass


main(1)
