# -*- coding: utf-8 -*-
import urllib
import re
import time
import os
import requests
from bs4 import BeautifulSoup
def schedule(a,b,c):
  '''''
  a:已经下载的数据块
  b:数据块的大小
  c:远程文件的大小
   '''
  per = 100.0 * a * b / c
  if per > 100 :
    per = 100
  print '%.2f%%' % per
#获取url,这里的url需要更改下，只能识别个别网址
def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  #print(html)
  return html

def getDownlink(downLink):
  downSoup = BeautifulSoup(downLink)
  print(downSoup.body)
  for link in downSoup.find_all(target="_blank"):
    print "ImageSrc", link['src']

#进入链接
def initLink(html):
  soup = BeautifulSoup(html)
  #reg=r''
  for link in soup.find_all(target="_blank"):
    print "Found the URL:", link['href']
    print("http://www.bz55.com"+link['href'])
    downUrl="http://www.bz55.com"+link['href']
    downLink=getHtml(downUrl)
    downloadImg(downLink)
#下载图片，需要判断在哪里下在的图片，保存到不同的目录下（直接保存到服务器的目录下）
def downloadImg(html):
  #img=r'http:\"?(.*?)(\"|>|\\s+)'
  #reg = r'http://.\.hiphotos.baidu.com/image/\w%\dD\d\d\d\/sign=\w+\/\w+\.jpg'
  reg = r''
  imgre = re.compile(reg)
  #findall返回的是图片的数量
  imglist = re.findall(imgre, html)
  #定义文件夹的名字
  t = time.localtime(time.time())
  foldername = str(t.__getattribute__("tm_year"))+"-"+\
               str(t.__getattribute__("tm_mon"))+"-"+str(t.__getattribute__("tm_mday"))
  print(foldername)
  picpath = 'D:\\ImageDownload\\%s' % (foldername) #下载到的本地目录
  if not os.path.exists(picpath):   #路径不存在时创建一个
    os.makedirs(picpath)
  x = 0
  for imgurl in imglist:
    print(imgurl)
    target = picpath+'\\%s.jpg' % x
    print(target)
    print 'Downloading image to location: ' + target + '\nurl=' + imgurl
    image = urllib.urlretrieve(imgurl, target, schedule)
    x += 1
    print(x)
  return image;