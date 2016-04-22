# coding:utf-8
'''
Created on 2016年4月22日
@author: hisenyuan
爬取慕课网的图片:利用了正则表达式+urllib2
'''
import urllib2
import re

# 打开网页
req = urllib2.urlopen("http://www.imooc.com/course/list")
# 读取网页内容
buf = req.read()
# 查找所有的图片链接
listurl = re.findall(r'http://.+\.jpg', buf)

i=0

# 存储图片
for url in listurl:
    f=open(str(i)+'.jpg','w')
    req = urllib2.urlopen(url)
    buf=req.read()
    f.write(buf)
    i+=1