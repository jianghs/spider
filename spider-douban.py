#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
import xlwt
import io
import sys
from bs4 import BeautifulSoup


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main(page, excel_sheet):
    url = "https://movie.douban.com/top250?start=" + str(page*25)
    html = request_douban(url)
    if html is None:
        return

    grid = html.find(class_="grid_view")
    movie_list = grid.find_all("li")

    # 解析过滤我们想要的信息
    save(movie_list, excel_sheet)


def request_douban(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # response.encoding = "GB18030"
            html = BeautifulSoup(response.text, "lxml")
            return html
    except requests.RequestException:
        return None


def save(lis, save_sheet):
    for li in lis:
        item = li.find(class_="item")
        no = item.find(class_="pic").em.text
        image = item.find(class_="pic").a.img["src"]
        title = item.find(class_="info").find(class_="hd").a.span.text
        content = item.find(class_="info").find(class_="bd").p.text
        # content = ""
        rate = item.find(class_="info").find(class_="bd").find(class_="rating_num").text
        pingjia = item.find(class_="info").find(class_="bd").find(class_="star").find_all("span")[3].text
        quote = ""
        if item.find(class_="info").find(class_="bd").find(class_="quote"):
            quote = item.find(class_="info").find(class_="bd").find(class_="quote").span.text

        # print(no, image, title, content, rate, pingjia, quote)
        save_sheet.write(int(no), 0, no)
        save_sheet.write(int(no), 1, image)
        save_sheet.write(int(no), 2, title)
        save_sheet.write(int(no), 3, content)
        save_sheet.write(int(no), 4, rate)
        save_sheet.write(int(no), 5, pingjia)
        save_sheet.write(int(no), 6, quote)


if __name__ == "__main__":
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    sheet.write(0, 0, '序号')
    sheet.write(0, 1, '图片')
    sheet.write(0, 2, '名称')
    sheet.write(0, 3, '作者')
    sheet.write(0, 4, '评分')
    sheet.write(0, 5, '评价数量')
    sheet.write(0, 6, '简介')

    for i in range(0, 10):
        main(i, sheet)

    # 保存为excel
    book.save(u'豆瓣最受欢迎的250部电影.xls')
