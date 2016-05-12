# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup

def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  #print(html)
  return html

def initLink(html):
  soup = BeautifulSoup(html)
  print(soup.prettify())
if __name__ == '__main__':
  print '''*************************************
**	  Welcome to use Spider	       **
**	 Created on  2016-04-27	       **
**	   @author: biao		       **
*************************************'''
  url="http://www.bz55.com/dongwubizhi/"
  html = getHtml(url)
  initLink(html)
