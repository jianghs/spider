#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
import io
import sys
from bs4 import BeautifulSoup


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main(page):
    url = "https://movie.douban.com/top250?start=" + str(page)
    html = request_dangdang(url)
    if html is None:
        return

    grid = html.find(class_="grid_view")
    movie_list = grid.find_all("li")

    # 解析过滤我们想要的信息
    items = parse_result(movie_list)
    for item in items:
        # print(item)
        write_item_to_file(item)


def request_dangdang(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # response.encoding = "GB18030"
            html = BeautifulSoup(response.text, "lxml")
            return html
    except requests.RequestException:
        return None


def parse_result(lis):
    for li in lis:
        item = li.find(class_="item")

        quote = ""
        if item.find(class_="info").find(class_="bd").find(class_="quote"):
            quote = item.find(class_="info").find(class_="bd").find(class_="quote").span.text

        yield {
            'no': item.find(class_="pic").em.text,
            'image': item.find(class_="pic").a.img["src"],
            'title': item.find(class_="info").find(class_="hd").a.span.text,
            'content': item.find(class_="info").find(class_="bd").p.text,
            'rate': item.find(class_="info").find(class_="bd").find(class_="rating_num").text,
            'pingjia': item.find(class_="info").find(class_="bd").find(class_="star").find_all("span")[3].text,
            'quote': quote
        }


def write_item_to_file(item):
    with open('output/movie.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


if __name__ == "__main__":
    for i in range(0, 275, 25):
        main(i)
