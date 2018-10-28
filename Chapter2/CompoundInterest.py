# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:15:41 2018

@author: kate
"""

##########################################
#### Think Like A Computer Sciencitst ####
##########################################

### Chapter 2 ###

## Compound Interest ##

def compoundInterest():
   
    P = 10000
    n = 12
    r = 0.08
    
    t = int(input("\nEnter number of years: "))
    
    A = P * ((1 + (r/n))) ** (n*t)
    
    return A

CI = compoundInterest()
print("Compount interest: %.2f" %(CI))