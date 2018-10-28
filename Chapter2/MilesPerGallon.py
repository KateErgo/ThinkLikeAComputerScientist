# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:37:06 2018

@author: kate
"""

##########################################
#### Think Like A Computer Sciencitst ####
##########################################

### Chapter 2 ###

## MPG ##

def MPG():
    
    miles = int(input("\nEnter number of miles: "))
    gallons = int(input("\nEnter number of gallons: "))
    
    mpg = miles / gallons
    
    return mpg

milesPerGallon = MPG()
print("Miles per gallon: %d." %(milesPerGallon))