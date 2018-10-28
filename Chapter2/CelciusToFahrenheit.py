# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:42:04 2018

@author: kate
"""

##########################################
#### Think Like A Computer Sciencitst ####
##########################################

### Chapter 2 ###

## Celcius To Fahrenheit ##

def toFahrenheit():
    
    C = int(input("\nEnter degrees in Celcius: "))
    
    F = (C * 1.8) + 32
    print("%.0f degrees in Celcius equals %.0f degrees in Fahrenheit." %(C,F))

toFahrenheit()