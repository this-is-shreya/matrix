# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:50:08 2020

@author: shreya
"""
#DATA COMPRESSION
import numpy #arrays

from PIL import Image

im=Image.open('jin-2.jpg')
pixelMap=im.load()
I=numpy.asanyarray(Image.open('jin-2.jpg'))
img=Image.new(im.mode,im.size)
pixelNew=img.load()
for i in range(img.size[0]):
    
    for j in range(img.size[1]):
        if (pixelMap[i,j]>=0 and pixelMap[i,j]<=31):
            pixelNew[i,j]=1
        elif (pixelMap[i,j]>=32 and pixelMap[i,j]<=63):
            pixelNew[i,j]=2
        elif (pixelMap[i,j]>=64 and pixelMap[i,j]<=95):
            pixelNew[i,j]=3
        elif (pixelMap[i,j]>=96 and pixelMap[i,j]<=127):
            pixelNew[i,j]=4
        elif (pixelMap[i,j]>=128 and pixelMap[i,j]<=159):
            pixelNew[i,j]=5
        elif (pixelMap[i,j]>=160 and pixelMap[i,j]<=191):
            pixelNew[i,j]=6
        elif (pixelMap[i,j]>=192 and pixelMap[i,j]<=223):
            pixelNew[i,j]=7
        else:
            pixelNew[i,j]=8
img.save('jin-3.jpg')
J=numpy.asanyarray(Image.open('jin-3.jpg'))
