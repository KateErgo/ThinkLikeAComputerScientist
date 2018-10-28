# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:27:49 2018

@author: kate
"""

##########################################
#### Think Like A Computer Sciencitst ####
##########################################

### Chapter 2 ###

## Area Of Circle ##

import math

def areaCircle():
    
    r = int(input("\nPlease enter the radius (r) of the circle: "))
    
    area = (r ** 2) * math.pi
    
    return area

AC = areaCircle()
print("The area of the cirlce is: %dm²." %(AC))