# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import json
def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  return html
class value:
    x = 0.000000
    y = 120.338225
if __name__ == '__main__':

    while value.x<360.000000:
        url1 = "http://maps.googleapis.com/maps/api/geocode/json?latlng=%.6f,%.6f"%(value.x,value.y)
        value.x = value.x+1.000000
        #value.x = value.x + 1.000000
        html = getHtml(url1)
        s = json.loads(html)
        if not s:
            break
        else:
            print s["results"][0]["formatted_address"]
    #print soup.prettify()
    #print soup.p

    #print s["results"]["formatted_address"]
