# coding:utf-8
'''
Created on 2016年4月21日
@author: hisenyuan
'''
from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    
    
    def craw(self, root_url):
        count = 1
        # 把根链接添加进待爬链接列表
        self.urls.add_new_url(root_url)
        # 判断是存在待爬取的链接
        while self.urls.has_new_url():
            try:
                # 获取一个待爬取的链接
                new_url = self.urls.get_new_url()
                # 输出每次获取的链接
                print 'craw %d : %s' % (count, new_url)
                # 获取单个链接的网页内容
                html_cont = self.downloader.download(new_url)
                # 获取链接里面的url，以及标题和摘要
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 把刚刚获取的url添加到待爬取的列表
                self.urls.add_new_urls(new_urls)
                # 把数据收集起来
                self.outputer.collect_data(new_data)
                # 控制循环次数
                if count == 100:
                    break
                count = count + 1
            except:
                print 'craw faied'
                
        self.outputer.output_heml()
        
    


# 第一次写这个，main旁边少写了下划线，检查了好久~
if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
