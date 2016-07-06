# coding:utf-8
'''
Created on 2016年7月6日

@author: hisenyuan
'''
import os

#dir 传入的目录(纯英文路径才行)
#fileList 传入一个数组
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