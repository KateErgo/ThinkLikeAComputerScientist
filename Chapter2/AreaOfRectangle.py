# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:34:46 2018

@author: kate
"""

##########################################
#### Think Like A Computer Sciencitst ####
##########################################

### Chapter 2 ###

## Area Of Rectangle ##

def areaRectangle():
    
    w = int(input("\nPlease enter the width of the rectangle: "))
    h = int(input("\nPlease enter the heigth of the rectangle: "))
    
    area = w * h
    
    return area

AR = areaRectangle()
print("The area of the cirlce is: %dm²." %(AR))