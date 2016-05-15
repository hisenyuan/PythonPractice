# coding:utf-8
'''
Created on 2016年5月15日

@author: Administrator
'''
input = open("tumblr.txt", "r").read()
output = open("b.txt", "w+")
start = 0
patterns = set()
#遍历文件，添加每一行到set
for line in input.split("\n"):
    patterns.add(line+"\n")
    start+=1

end = 0;
#遍历set，写出到文件b.text
for url in patterns:
    output.write(url)
    end+=1
output.close()
print "去除重前:"+str(start)+"条\n去除重后:"+str(end)+"条"