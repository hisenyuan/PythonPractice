# coding:utf-8
'''
Created on 2016年5月2日

@author: hisenyuan
'''
from bs4 import BeautifulSoup
import urllib2
import urllib
import cookielib
import re
import json
from pip._vendor import requests

URL_BAIDU_INDEX = u'http://www.baidu.com/';
# https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=true 也可以用这个
URL_BAIDU_TOKEN = 'https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&class=login';
URL_BAIDU_LOGIN = 'https://passport.baidu.com/v2/api/?login';

# 设置用户名、密码
username = '梦殇国际';  #
password = 'www.714.hk';  #

# 设置cookie，这里cookiejar可自动管理，无需手动指定
cj = cookielib.CookieJar();
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
urllib2.install_opener(opener);
reqReturn = urllib2.urlopen(URL_BAIDU_INDEX);

# 获取token,
tokenReturn = urllib2.urlopen(URL_BAIDU_TOKEN);
matchVal = re.search(u'"token" : "(?P<tokenVal>.*?)"', tokenReturn.read());
tokenVal = matchVal.group('tokenVal');


# 构造登录请求参数，该请求数据是通过抓包获得，对应https://passport.baidu.com/v2/api/?login请求
postData = {
'username' : username,
'password' : password,
'u' : 'https://passport.baidu.com/',
'tpl' : 'pp',
'token' : tokenVal,
'staticpage' : 'https://passport.baidu.com/static/passpc-account/html/v3Jump.html',
'isPhone' : 'false',
'charset' : 'UTF-8',
'callback' : 'parent.bd__pcbs__ra48vi'
};
postData = urllib.urlencode(postData);


# 发送登录请求
loginRequest = urllib2.Request(URL_BAIDU_LOGIN, postData);
loginRequest.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8');
loginRequest.add_header('Accept-Encoding', 'gzip,deflate,sdch');
loginRequest.add_header('Accept-Language', 'zh-CN,zh;q=0.8');
loginRequest.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36');
loginRequest.add_header('Content-Type', 'application/x-www-form-urlencoded');
sendPost = urllib2.urlopen(loginRequest);


# 查看贴吧个人主页 ，测试是否登陆成功，由于cookie自动管理，这里处理起来方便很多
# http://tieba.baidu.com/home/main?un=XXXX&fr=index 这个是贴吧个人主页，各项信息都可以在此找到链接

# 获取我喜欢的贴吧页数，一页20个
def getnum():
    url_forum = 'http://tieba.baidu.com/i/68449687/forum'
    r2 = requests.get(url_forum)
    search = re.findall(ur'forum_name":"(.+?)"', r2.text)
    num_forum = len(search)
    if num_forum % 20 != 0:
        num_forum = num_forum / 20 + 1
    return num_forum




#获取我喜欢的贴吧信息
def getinfo(num):
    start = 1;
    print '吧名\t\t贴吧fid\t\t等级\t\t经验\t贴吧链接';
    while(start <= num):
        teibaUrl = 'http://tieba.baidu.com/f/like/mylike?&pn=' + str(start);
        start = start + 1;
        content = urllib2.urlopen(teibaUrl).read();
        content = content.decode('gbk').encode('utf8');
        # 打印个人贴吧网页内容
        # print content;
        
        # 解析数据，用的BeautifulSoup4，感觉没有jsoup用的爽
        soup = BeautifulSoup(content, 'html.parser');
        list = soup.findAll('tr');
        list = list[1:len(list)];
        # careTeibalist = [];
        for elem in list:
            soup1 = BeautifulSoup(str(elem), 'html.parser');
            # 获取fid的前缀网址，等号后面跟贴吧名字的URL编码
            url1 = 'http://tieba.baidu.com/f/commit/share/fnameShareApi?ie=utf-8&fname=';
            # /f?kw=%D3%A2%D0%DB%C1%AA%C3%CB 截取后面的%D3%A2%D0%DB%C1%AA%C3%CB
            name = soup1.find('a')['href'].split('=')[1];
            # 解析json
            fidconnect = urllib2.urlopen(url1 + name).readline();
            fid = json.loads(fidconnect)['data']['fid'];
            print soup1.find('a')['title'] + '\t\t' + '%d' % fid + '\t\t' + soup1.find('a', {'class', 'like_badge'})['title'] + '\t\t' + soup1.find('a', {'class', 'cur_exp'}).get_text() + '\t' + 'http://tieba.baidu.com' + soup1.find('a')['href'];

#获取页数
num = getnum();
#获取信息
getinfo(num)




