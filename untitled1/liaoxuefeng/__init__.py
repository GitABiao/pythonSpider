# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  return html
if __name__ == '__main__':
    url1 = "http://www.12306.cn/mormhweb/"
    html = getHtml(url1)
    soup = BeautifulSoup(html)
    print soup.prettify()
    print soup.title.string