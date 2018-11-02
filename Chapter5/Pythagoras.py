# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 08:15:59 2018

@author: kate
"""

from math import sqrt

def pythagoras():
    
    a = int(input("\nLength of side a: "))
    b = int(input("\nLength of side b: "))
    
    c = sqrt(a ** 2 + b ** 2)
    
    return c

pythagoras()
    