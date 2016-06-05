# -*- coding: utf-8 -*-
#spider1.1 last-time 2016-05-19
#详细的图片下载器


import urllib
import re
import time
import os
import urlparse
import winsound
import glob ,os
from PIL import Image
from bs4 import BeautifulSoup
import MySQLdb
y = 0
x = 0
z = 0
def changImage():
    for files in glob.glob("D:/ImageDownload/chemobizhi/*.jpg"):
        filepath, filename = os.path.split(files)
        filterame, exts = os.path.splitext(filename)
        # 输出路径
        opfile = r'D:/ImageDownload/chemobizhi/'
        # 判断opfile是否存在，不存在则创建
        if (os.path.isdir(opfile) == False):
            os.mkdir(opfile)
        im = Image.open(files)
        w, h = im.size
        im_ss = im.resize((int(w * 0.12), int(h * 0.12)))
        im_ss.save(opfile + filterame + '.jpg')
def Mysql(name,imageurl,leibie,FLAG):

  imagename=name
  imageurl1=imageurl
  leibie1=leibie
  conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='biao',
    passwd='314125',
    db='user',
    charset="utf8"
  )
  cur = conn.cursor()
  if FLAG==0:
    select = "select * from imageinfor"
    cur.execute(select)
    for row in cur:
      print "id=%s,name=%s,url=%s,type=%s" % row
    print cur.rowcount
  elif FLAG==1:
    value=[imagename,imageurl1,leibie1]
    print value
    cur.execute("insert imageinfor values(null,%s,%s,%s)",value)
    print "已经添加信息到mysql"
    print cur.rowcount
  conn.commit()
  cur.close()
  conn.close()
#获取url,这里的url需要更改下，只能识别个别网址
def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  return html
#获取图片链接
def getImageInfor(downLink,leibie):
  global y
  soup = BeautifulSoup(downLink)
  print "所有的img标签："
  for tar in soup.find_all('img'):
    print tar
  reg = r'\/\w{6,10}\/\w{4,8}\/\d{4,8}\/\d{1,5}\-\w{9,15}\.jpg'
  imgre = re.compile(reg)
  imglist = re.findall(imgre, downLink)
  for imgurl in imglist:
    y=y+1
    print '获取Image的链接'
    imgLink=urlparse.urljoin("http://www.bz55.com", imgurl)
    print "getDownlink:%s" %imgLink
    #Mysql(y,imgLink,leibie,1)

#进入链接
def initLink(html,dir,leibie):
  count=0
  soup = BeautifulSoup(html)
  print "下载的图片类型"
  print soup.title.string
  print "我们需要的东西："
  print "body.children"
  #for child in soup.body.children:
   # print child
  print "所有链接："
  for test in soup.find_all(target="_blank"):
      print test['href']
  reg1 = r'\/\w{0,11}\/\d{0,7}\.html'
  reg2 = r'\/\w{0,11}\/\d{0,4}\/\d{0,5}\/\d{0,7}\.html'
  if leibie==1 or leibie==6 or leibie==7 or leibie==8:
    reg=reg1
  else:
    reg=reg2
  for link in soup.find_all(target="_blank"):
    if re.match(reg,link['href']):
      count=count+1
      print"第%d个链接"%count
      print "http://www.bz55.com"+link['href']
      downUrl="http://www.bz55.com"+link['href']
      downLink=getHtml(downUrl)
      getImageInfor(downLink,leibie)
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
  picpath = 'D:/Program Files/Apache24/htdocs/image%s%s/' % (dir,foldername) #下载到的本地目录
  if not os.path.exists(picpath):   #路径不存在时创建一个
    os.makedirs(picpath)
  print imglist
  for imgurl in imglist:
    try:
      imageurl=urlparse.urljoin("http://www.bz55.com",imgurl)
      #print urlparse.urljoin("http://www.bz55.com",imgurl)
      target = picpath+'%s.jpg' % x
      #print(target)
      print 'Downloading image to location: ' + target + '   nurl=' + imageurl
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

  print "0:其他壁纸\n1:美女壁纸\n2:节日壁纸\n3:车模壁纸\n4:植物壁纸\n5:动物壁纸\n6:体育壁纸\n7:日历壁纸\n8:文字壁纸\n"
  link = input('请输入你想下载的图片类型')
  urlList=["/qitabizhi/","/meinvbizhi/","/jieribizhi/","/chemobizhi/","/zhiwubizhi/"
           ,"/dongwubizhi/","/tiyubizhi/","/rilibizhi/","/wenzipic/"]
  imageurl = "http://www.bz55.com" + urlList[link]
  html = getHtml(imageurl)
  print"下载地址"
  print imageurl
  initLink(html, urlList[link],link)
  print "Download has finished."
  #Mysql(x,y,link,0)
  #changImage()

