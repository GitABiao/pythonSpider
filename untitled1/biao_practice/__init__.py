# -*- coding: utf-8 -*-
from PIL import Image
img=Image.open("D:/ImageDownload/chemobizhi/5-18/264.jpg")
w,h=img.size
img.thumbnail((w//4, h//4))
img.save("D:/ImageDownload/chemobizhi/264.jpg")