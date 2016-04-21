# coding:utf-8
'''
Created on 2016年4月21日
@author: hisenyuan
'''
class HtmlOutputer(object):
    def __init__(self):
        self.datas =[]
        
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_heml(self):
        fout = open('output.html','w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write('<a href="http://yhx.wiki/" target="_blank"><h3>http://yhx.wiki<h3></a>')
        fout.write('<table border="1px" cellspacing="0px" cellpadding="5">')
        fout.write('<tr>')
        fout.write('<td>标题</td>')
        fout.write('<td>摘要</td>')
        fout.write('<td>链接</td>')
        fout.write('</tr>')
        
        # ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['url'])
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()
    
    
    
    



