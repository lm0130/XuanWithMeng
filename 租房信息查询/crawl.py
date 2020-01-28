from bs4 import BeautifulSoup
import requests
import csv
import time
import argparse
import random
import os


# 从网站中下载离线网页用于分析
def DownloadOffline(args):
    urlelems = {'page': 1,  # 当前页数
                'minprice': 4000,
                'maxprice': 6000, }
    urlFormat = 'https://beijing.baixing.com/zhengzu/?page={page}'
    dirname = 'Offline'  # 存放的文件夹名字
    pageCount = 100  # 爬取的页数

    if os.path.exists(dirname) == False:
        os.mkdir(dirname)

    for page in range(pageCount):
        url = urlFormat.format(**urlelems)
        print(url)

        response = requests.get(url)
        if (response):
            f = open(os.path.join(dirname, str(urlelems['page']) + '.html'), 'wb+')
            print(os.path.join(dirname, str(urlelems['page']) + '.html'))

            f.write(response.content)
            f.close()

        urlelems['page'] += 1
        time.sleep(random.randrange(1000, 2000, 1) / 1000)  # 等待随机时间，减少被阻止概率

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='租房信息爬虫')
    parser.add_argument('-m', '--mode')  # 运行模式
    args = parser.parse_args()
    print(args)

    if args.mode == 'DownloadOffline':
        DownloadOffline(args)
    else:
        print('Not support')
