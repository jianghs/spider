#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
import requests
import io
import sys
from bs4 import BeautifulSoup
import chardet

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='GB18030')


def main(page):
    url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-" + str(page)
    html = request_dangdang(url)

    book = html.find(class_="bang_list clearfix bang_list_mode")
    book_list = book.find_all("li")

    # 解析过滤我们想要的信息
    items = parse_result(book_list)
    for item in items:
        # print(item)
        write_item_to_file(item)


def request_dangdang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response.encoding = "GB18030"
            html = BeautifulSoup(response.text, "lxml")
            return html
    except requests.RequestException:
        return None


def parse_result(items):
    for item in items:
        author = ""
        if item.find_all(class_="publisher_info")[0].a:
            author = item.find_all(class_="publisher_info")[0].a.text
        else:
            author = item.find_all(class_="publisher_info")[0].text

        yield {
            'range': item.find(class_="list_num").text,
            'image': item.find(class_="pic").a.img["src"],
            'title': item.find(class_="name").a.text,
            'recommend': item.find(class_="star").find(class_="tuijian").text,
            'author': author,
            'times': item.find(class_="biaosheng").span.text,
            'price': item.find(class_="price").find(class_="price_n").text.replace("¥", "")
        }


def write_item_to_file(item):
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


if __name__ == "__main__":
    for i in range(1, 26):
        main(i)
