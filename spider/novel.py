#! usr/bin/env python
# -*- coding:utf-8 -*-

"""
Mainly for downloading Novals.
Study to use class/ urllib/ requests/ BeautifulSoup/ chardet, ect.

author:zzg
date:2018.3.30

"""

from urllib.request import urlopen
import requests, sys
from bs4 import BeautifulSoup
import chardet



class downloader(object):
    """下载小说"""

    def __init__(self):
        """属性"""
        self.server = 'http://www.booktxt.net/'                      #小说网站
        self.target = 'http://www.booktxt.net/2_2219/'              #小说目录
        self.charset = ''                                                #网站编码
        self.name = []                                                    #章节名称
        self.urls = []                                                    #章节链接
        self.nums = 0                                                     #章节数

    def get_charset(self):
        """利用chardet 获取网站编码 chaeset """
        html = urlopen(self.target).read()
        self.charset = chardet.detect(html)['encoding']

    def get_urls(self):
        """获取小说各章节的下载链接"""
        num = 0                                                           #小说第一章开始位置

        r = requests.get(url=self.target)
        r.encoding = self.charset
        html = r.text
        div_bf = BeautifulSoup(html, 'lxml')                            #创建div BeautifulSoup
        div = div_bf.find_all('div', id='list')
        #获取每章节的链接
        a_bf = BeautifulSoup(str(div[0]), 'lxml')
        a = a_bf.find_all('a')

        for k in range(len(a)):                                        #获取第一章所在位置
            if '第一章' in a[k].string:
                num = k
                break

        self.nums = len(a[num:])

        for i in a[num:]:
            self.name.append(i.string)
            self.urls.append(self.server + i.get('href'))
        #for i in a[11:]:
        #    print(i.string, self.server + i.get('href'))


    def get_content(self, url):
        """获取小说每章节的内容"""
        r = requests.get(url)
        r.encoding = self.charset
        html = r.text
        bf = BeautifulSoup(html, 'lxml')
        div_bf = bf.find_all('div', id='content')
        content = div_bf[0].text.replace('\xa0'*4, '')                #剔除空格和其他标签
        #print(content)
        return content

    def writer(self, content):
        """写入文件"""
        with open('H://code//spider//圣墟.txt', 'a', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    dl = downloader()
    dl.get_charset()
    urls = dl.get_urls()
    #print(type(urls))
    #print(urls)
    print('开始下载《圣墟》：')
    for i in range(dl.nums):
        print(dl.name[i])
        dl.writer(dl.name[i])
        dl.writer('\n')
        dl.writer(dl.get_content(dl.urls[i]))
    print('《圣墟》下载完成。')
    #print(dl.get_urls())
    #print(len(dl.get_urls()))