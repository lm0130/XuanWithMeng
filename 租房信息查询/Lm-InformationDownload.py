from bs4 import BeautifulSoup
import requests

base_url="https://beijing.baixing.com/zhengzu"
page_num=1
#web_url=requests.get(base_url+'/?page=',params=page_num)
str_page_num=str(page_num)
total_url=base_url+'/?page='+str_page_num
web_url=requests.get(total_url)
print(web_url.url)
