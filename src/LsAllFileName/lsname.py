# coding:utf-8
'''
Created on 2016年7月6日

@author: Administrator
'''
import os
 
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList
 
list = GetFileList('D:\\download\\video', [])
for e in list:
    print e