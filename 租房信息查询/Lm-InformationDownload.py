# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv
import re
import time
import random
import fake_useragent
import lxml

def url_func(dic,base_url,area_dic,page_num):
    if(dic["area"]!="全北京"):
        url_1=base_url+area_dic[dic["area"]]
    else:
        url_1=base_url
    lower_bound=dic["lower bound"] if int(dic["lower bound"])>0 else ""
    upper_bound=dic["upper bound"] if int(dic["upper bound"])>0 else ""
    url_2=url_1+'page='+str(page_num)+'%E4%BB%B7%E6%A0%BC%5B0%5D='+lower_bound+'&%E4%BB%B7%E6%A0%BC%5B1%5D='+upper_bound+'&query='
    return url_2


# TODO:加入一些参数：地区、租金、整套or单间、是否显示调试信息等
base_url = 'https://beijing.baixing.com/zhengzu'
area_dic={"朝阳":"/m7294/?","海淀":"/m7295/?","丰台":"/m7296/?","通州":"/m7297"}
ua = fake_useragent.UserAgent()  # 反爬措施1：使用随机User Agent

f = open(r"Offline/information.csv", 'w', encoding='utf-8', newline='')  # 加入newline=''防止出现多余空行

#传入格式：字典类型["area":"海淀","lower bound":"2000","upper bound":"4000"]
#         若价格不限或者为["area":"海淀","lower bound":"-1","upper bound":"-1"]

for page_num in range(1, 2):  # TODO:将搜索页数改成命令行参数
    # web_url=requests.get(base_url+'/?page=',params=page_num)
    #total_url = base_url + '/?page=' + str(page_num)
    dic={"area":"朝阳","lower bound":"-1","upper bound":"4000"}
    total_url=url_func(dic,base_url,area_dic,page_num)
    print(total_url)
    web_url = requests.get(total_url, headers={'User-Agent': ua.random})
    print(web_url.url)

    html_test = web_url.text
    soup = BeautifulSoup(html_test, features='lxml')
    #print(soup, type(soup))
    #print("===============================")
    #print(soup.span)
    #print("2===============================")
    #print(type(soup.a))
    # print(soup.a.get('ad-title'))


    csv_writer = csv.writer(f)

    house_name_list = soup.select(".ad-title")
    house_price_list = soup.select(".highlight")
    house_loc_list = soup.select(".ad-item-detail")
    flag=0;
    i=0
    for house, house_price in zip(house_name_list, house_price_list):
        house_name = house.get_text()  # 标题
        house_info_item =house_loc_list[i].get_text()
        house_loc_item = house_loc_list[i+1].get_text()
        i+=2
        house_url = house['href']  # 链接
        house_price_number = house_price.next[:-1]  # 价格。需去掉末尾“元”字

        '''
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
        '''
        houseInfo = [house_name,house_price_number,house_loc_item,house_info_item,house_url]
        #print("\n".join(houseInfo))
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
