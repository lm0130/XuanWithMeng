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
    if args.__contains__('dir') and args.dir != None:# 存放的文件夹名字
        dirname = args.dir
    else:
        dirname = 'Offline'
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

#解析页面并生成csv
def ParsePage(args):
    if args.__contains__('dir') and args.dir != None and \
            os.path.exists(args.dir) and os.listdir():# 存放的文件夹名字


        BeautifulSoup.encode()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='租房信息爬虫')
    parser.add_argument('-m', '--mode')  # 运行模式
    parser.add_argument('-d','--dir')  # 工作目录
    args = parser.parse_args()
    print(args)

    if args.mode == 'DownloadOffline':
        DownloadOffline(args)
    elif args.mode == 'ParsePage':
        ParsePage(args)
    else:
        print('Not support')
