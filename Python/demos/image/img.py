#coding=utf-8

#urllib模块提供了读取Web页面数据的接口
import urllib
#txt wirte read
import io
#re模块主要包含了正则表达式
import re
#定义一个getHtml()函数
def getHtml(url):
    page = urllib.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    return html

def getImg(html):
    reg = r'http://.[^\s]+?.jpg|http://.[^\s]+?.png'    #正则表达式，得到图片地址
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0
    f = open("test.txt","a")
    for imgurl in imglist:
        #urllib.urlretrieve(imgurl,'/Users/liutong/Desktop/zhitu-des/%s.jpg' % x)
        f.writelines(imgurl+"\n")
        x+=1
    f.close()
    
    f2 = open('/Users/liutong/Desktop/test.txt')
    lines = f2.readlines()

    for urllist in lines:
        imgFile = '/Users/liutong/Desktop/zhitu-des/%s' % urllist.split('/')[-1] 
        urllib.urlretrieve(urllist,imgFile[:-1])


html = getHtml("http://www.rxsjy.com/index")
print getImg(html)