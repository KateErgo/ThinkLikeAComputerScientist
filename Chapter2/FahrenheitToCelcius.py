# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:48:04 2018

@author: kate
"""

##########################################
#### Think Like A Computer Sciencitst ####
##########################################

### Chapter 2 ###

## Fahrenheit To Celcius ##

def toCelcius():
    
    F = int(input("\nEnter degrees in Fahrenheit: "))
    
    C = (F - 32) / 1.8
    print("%.0f degrees in Fahrenheit equals %d degrees in Celcius." %(F,C))

toCelcius()