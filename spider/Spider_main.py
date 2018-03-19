# -*- coding utf-8 -*-
#!/usr/bin/env python3

'''
spider_main.py上面爬虫流程图中的【调度器】
面向对象写法，调度器负责循环从UrlManager获取爬取链接，然后交给HTMLDownloader下载，然后把下载内容交给HtmlParser解析，然后把有价值数据输出给HTMLOutput进行应用。
爬取百度百科 Andriod 关键词相关词及简介并输出为一个 HTML tab网页
'''
from spider import url_manager, html_downloader, html_parser, html_output

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.out_put = html_output.HtmlOutput()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d: %s" % (count, new_url))
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"
                }
                html_content = self.downloader.download(new_url, retry_count=2, headers=headers)
                new_urls, new_data = self.parser.parse(new_url, html_content, "utf-8")
                self.urls.add_new_urls(new_urls)
                self.out_put.collect_data(new_data)
                if count >= 30:
                    break
                count = count + 1
            except Exception as e:
                print("craw failed!\n"+str(e))
        self.out_put.output_html()

if __name__ == "__main__":
    rootUrl = "http://baike.baidu.com/item/android"
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)