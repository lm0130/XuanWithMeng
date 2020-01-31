# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv
import re
import time
import random
import fake_useragent

# TODO:加入一些参数：地区、租金、整套or单间、是否显示调试信息等
base_url = 'https://beijing.baixing.com/zhengzu'
ua = fake_useragent.UserAgent()  # 反爬措施1：使用随机User Agent

f = open(r"Offline/information.csv", 'w', encoding='utf-8', newline='')  # 加入newline=''防止出现多余空行

for page_num in range(1, 3):  # TODO:将搜索页数改成命令行参数
    # web_url=requests.get(base_url+'/?page=',params=page_num)
    total_url = base_url + '/?page=' + str(page_num)
    web_url = requests.get(total_url, headers={'User-Agent': ua.random})
    print(web_url.url)

    html_test = web_url.text
    soup = BeautifulSoup(html_test, features='lxml')
    print(soup, type(soup))
    print("===============================")
    print(soup.span)
    print("2===============================")
    print(type(soup.a))
    # print(soup.a.get('ad-title'))


    csv_writer = csv.writer(f)

    house_name_list = soup.select(".ad-title")
    house_price_list = soup.select(".highlight")
    for house, house_price in zip(house_name_list, house_price_list):
        house_name = house.get_text()  # 标题
        house_url = house['href']  # 链接
        house_price_number = house_price.next[:-1]  # 价格。需去掉末尾“元”字

        # 获取经纬度（打开页面，页面内部将写出。格式为 lng = 116.46125350856, lat = 39.879178775689）
        # 返回值为[经度，纬度]，查找失败则为['','']
        location = ['', '']

        locationStr = requests.get(house_url, headers={'User-Agent': ua.random})
        if locationStr:
            locationStr = locationStr.text
            locationStr = re.search(r'lng = \d*\.\d*, lat = \d*\.\d*', locationStr)  # 找到对应字符串
            if locationStr:
                location = re.findall(r'\d*\.\d*', locationStr.group())  # 取出对应的数字

        # TODO:完善一些信息：整套or单间，房间大小，房源添加日期，房源信息等
        houseInfo = [house_name, location[0], location[1], house_price_number, house_url]
        print("\n".join(houseInfo))
        csv_writer.writerow(houseInfo)
        time.sleep(random.randrange(500, 2000) / 1000)  # 反爬虫破解2：随机休息时间

    time.sleep(random.randrange(1500, 3000) / 1000)

f.close()
'''
    print("3===============================")
    for house_price in house_price_list:
        print(house_price.next)
        house_price_number=house_price.next
        print(house_price)
'''
