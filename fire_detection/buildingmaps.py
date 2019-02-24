#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 00:15:13 2019

@author: abhijithneilabraham
"""

import osgeo.gdal as gdal
import osgeo.osr as osr
import numpy as np
from numpy import ma

def maFromGDAL(filename):
    dataset = gdal.Open(filename, gdal.GA_ReadOnly)

    if dataset is None:
        raise Exception()

    # Get the georeferencing metadata.
    # We don't need to know the CRS unless we want to specify coordinates
    # in a different CRS.
    #projection = dataset.GetProjection()
    geotransform = dataset.GetGeoTransform()

    # We need to know the geographic bounds and resolution of our dataset.
    if geotransform is None:
        dataset = None
        raise Exception()

    # Get the first band.
    band = dataset.GetRasterBand(1)
    # We need to nodata value for our MaskedArray later.
    nodata = band.GetNoDataValue()
    # Load the entire dataset into one numpy array.
    image = band.ReadAsArray(0, 0, band.XSize, band.YSize)
    # Close the dataset.
    dataset = None

    # Create a numpy MaskedArray from our regular numpy array.
    # If we want to be really clever, we could subclass MaskedArray to hold
    # our georeference metadata as well.
    # see here: http://docs.scipy.org/doc/numpy/user/basics.subclassing.html
    # For details.
    masked_image = ma.masked_values(image, nodata, copy=False)
    masked_image.fill_value = nodata

    return masked_image, geotransform

def pixelToMap(gt, pos):
    return (gt[0] + pos[0] * gt[1] + pos[1] * gt[2],
            gt[3] + pos[0] * gt[4] + pos[1] * gt[5])

# Reverses the operation of pixelToMap(), according to:
# https://en.wikipedia.org/wiki/World_file because GDAL's Affine GeoTransform
# uses the same values in the same order as an ESRI world file.
# See: http://www.gdal.org/gdal_datamodel.html
def mapToPixel(gt, pos):
    s = gt[0] * gt[4] - gt[3] * gt[1]
    x = (gt[4] * pos[0] - gt[1] * pos[1] + gt[1] * gt[5] - gt[4] * gt[2]) / s
    y = (-gt[3] * pos[0] + gt[0] * pos[1] + gt[3] * gt[2] - gt[0] * gt[5]) / s
    return (x, y)

def valueAtMapPos(image, gt, pos):
    pp = mapToPixel(gt, pos)
    x = int(pp[0])
    y = int(pp[1])

    if x < 0 or y < 0 or x >= image.shape[1] or y >= image.shape[0]:
        raise Exception()

    # Note how we reference the y column first. This is the way numpy arrays
    # work by default. But GDAL assumes x first.
    return image[y, x]

try:
    image, geotransform = maFromGDAL('test.tiff')
    val = valueAtMapPos(image, geotransform, (10.0, 9.0))
    print(val)
except:
    print('Something went wrong.')
    
import cv2
import numpy as np
img = cv2.imread("map22.jpg")
frame = img[100:900, 100:900]
lower_range = np.array([0,0,0])
upper_range =np.array([255,115,255])
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

ret, thresh_img = cv2.threshold(gray,170,255,cv2.THRESH_BINARY)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
frame1 = cv2.resize(frame,(1000,1000))


cv2.imwrite("Test.jpg",frame)
img2 = cv2.imread("Test.jpg")
mask = cv2.inRange(img2, lower_range, upper_range)

contours =  cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
'''
img2, contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
'''
cv2.drawContours(img2, contours, -1, (0,255,0), 3)
cv2.imwrite("Test2.jpg",img2)
