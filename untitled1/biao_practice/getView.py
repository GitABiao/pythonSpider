# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import time

def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  #print(html)
  return html

def initLink(html):
  soup = BeautifulSoup(html)
  print soup.prettify()
  #print soup.body.contents
  #print soup.body.children

  #for string in soup.stripped_strings:
   # print string
  #print soup.head.meta.attrs


def getCurrentTime():
  pass


if __name__ == '__main__':
  print '''*************************************
**	  Welcome to use Spider	       **
**	 Created on  2016-04-27	       **
**	   @author: biao		       **
*************************************'''
  url="http://www.ui.cn/"
  html = getHtml(url)
  initLink(html)
  print (getCurrentTime())

def getCurrentTime(self):
  return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))
