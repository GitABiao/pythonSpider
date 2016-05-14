# -*- coding: utf-8 -*-
#本程序用来抓取网络上的图片，例子使用的是http://www.bz55.com上的桌面壁纸
import urllib
import re
import time
import os
import urlparse
import winsound
from bs4 import BeautifulSoup
x = 0
class Image(object):
  def __init__(self, name, url):
    self.name = name
    self.url = url
  def geturl(self):
    return self.url
#显示下载进度
def schedule(a,b,c):
  per = 100.0 * a * b / c
  if per > 100 :
    per = 100
  print '%.2f%%' % per
#获取url,这里的url需要更改下，只能识别个别网址
def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  return html
#获取图片链接
def getDownlink(downLink):
  reg = r'\/\w{6,10}\/\w{4,8}\/\d{4,8}\/\d{1,5}\-\w{9,15}\.jpg'
  imgre = re.compile(reg)
  imglist = re.findall(imgre, downLink)
  for imgurl in imglist:
    print "getDownlink:%s" %imgurl
#进入链接
def initLink(html,dir):
  soup = BeautifulSoup(html)
  reg= r'\/\w{7,11}\/\d{4}\/\d{2,5}\/\d{3,7}\.html'
  for link in soup.find_all(target="_blank"):
    if re.match(reg,link['href']):
      print "http://www.bz55.com"+link['href']
      print soup.name
      downUrl="http://www.bz55.com"+link['href']
      downLink=getHtml(downUrl)
      getDownlink(downLink)
      downloadImg(downLink,dir)
#下载图片,现在就差url的问题。怎么连接rul之间
def downloadImg(html,dirName):
  global x
  reg = r'\/\w{6,10}\/\w{4,8}\/\d{4,8}\/\d{1,5}\-\w{9,15}\.jpg'
  imgre = re.compile(reg)
  #findall返回的是图片的数量
  imglist = re.findall(imgre, html)
  #定义文件夹的名字
  t = time.localtime(time.time())
  dir = str(dirName)
  foldername = str(t.__getattribute__("tm_mon"))+"-"+str(t.__getattribute__("tm_mday"))
  print(foldername)
  picpath = 'D:\\ImageDownload\\%s\\%s' % (dir,foldername) #下载到的本地目录
  if not os.path.exists(picpath):   #路径不存在时创建一个
    os.makedirs(picpath)
  print imglist
  for imgurl in imglist:
    try:
      imageurl=urlparse.urljoin("http://www.bz55.com",imgurl)
      #print urlparse.urljoin("http://www.bz55.com",imgurl)
      target = picpath+'\\%s.jpg' % x
      #print(target)
      print 'Downloading image to location: ' + target + '\nurl=' + imageurl
      image = urllib.urlretrieve(imageurl, target)
      x=x+1
      print x
    except urllib.ContentTooShortError,e:
      print 'urllib.ContentTooShortError',e
  return image;
#Pictrue类的
if __name__ == '__main__':
  print '''*************************************
**	  Welcome to use Spider	       **
**	 Created on  2016-04-27	       **
**	   @author: biao		       **
*************************************'''
  urlList=["/qitabizhi/","/meinvbizhi/","/jieribizhi/","/chemobizhi/","/zhiwubizhi/"
           ,"/dongwubizhi/","/tiyubizhi/","/rilibizhi/","/wenzipic/"]
  for i in [0,1, 2, 3, 4, 5, 6, 7, 8]:
    imageurl="http://www.bz55.com"+urlList[i]
    print imageurl
    html = getHtml(imageurl)
    t = time.localtime(time.time())
    initLink(html,urlList[i])

  print "Download has finished."
