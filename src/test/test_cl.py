# coding:utf-8
'''
@author: hisenyuan
'''
import urllib2
import sys
from bs4 import BeautifulSoup

reload(sys)
# sys.setdefaultencoding('utf8')#解决写入文件乱码问题

BaseUrl = "http://cl.pclmm.org/"
j=1

for i in range(1, 100): #设置始末页码
    url = "http://cl.pclmm.org/thread0806.php?fid=22&search=&page="+ str(i)  #默认str会把字符串变成unicode，所以开头必须用sys来重置
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, from_encoding="gb18030")   #解决BeautifulSoup中文乱码问题
    print("reading page "+ str(i))
    counts = soup.find_all("td", class_="tal f10 y-style")

for count in counts:
    if int(count.string)>15:#选择想要的点击率
        videoContainer = count.previous_sibling.previous_sibling.previous_sibling.previous_sibling
        video = videoContainer.find("h3")
        print("Downloading link "+ str(j))
        line1 = (video.get_text())
        line2 = BaseUrl+video.a.get('href')
        line3 = "view **" + count.string + "** "
        print line1
        f = open('cao.md', 'a')
        f.write("\n"+"###"+" "+line1+"\n"+"<"+line2+">"+"\n"+line3+ "  "+ "page"+str(i)+"\n")
        f.close()
        j+=1