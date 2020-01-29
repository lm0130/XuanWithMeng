# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import lxml
import csv
import  re

base_url='https://beijing.baixing.com/zhengzu'
page_num=2
#web_url=requests.get(base_url+'/?page=',params=page_num)
str_page_num=str(page_num)
total_url=base_url+'/?page='+str_page_num
web_url=requests.get(total_url)
print(web_url.url)

html_test=web_url.text
soup=BeautifulSoup(html_test,'lxml')
print(soup,type(soup))
print("===============================")
print(soup.span)
print("2===============================")
print(type(soup.a))
#print(soup.a.get('ad-title'))

house_name_list=soup.select(".ad-title")
house_price_list=soup.select(".highlight")
f=open(r"C:\Users\User\Desktop\information.csv",'w',encoding='utf-8')
csv_writer=csv.writer(f)

for house,house_price in zip(house_name_list,house_price_list):
    house_name=house.get_text()
    house_url=house['href']
    house_price_number = house_price.next
    print(house_price_number)
    print(house.get_text())
    print(house['href'])
    csv_writer.writerow([house_name,house_price_number,house_url])

f.close()
'''
print("3===============================")
for house_price in house_price_list:
    print(house_price.next)
    house_price_number=house_price.next
    print(house_price)
'''
