# coding:utf-8
'''
Created on 2016年5月3日

@author: Administrator
'''
import re
pattern = re.compile(r'/f?kw=(.*)')
res = pattern.match('f?kw=%BF%D5%BC%E4%CB%D8%B2%C4')
print res

s = 'f?kw=%BF%D5%BC%E4%CB%D8%B2%C4'
a = s.split('=')
print a[1]