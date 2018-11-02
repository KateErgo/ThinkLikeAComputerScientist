# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 08:38:45 2018

@author: kate
"""

def findHypot(a,b):
    
    return (a * a + b * b) ** 0.5
    

def main():
    
    a = int(input("\nLength of side a: "))
    b = int(input("\nLength of side b: "))
    
    hypothenuse = findHypot(a,b)
    
    print("\nThe length of the hypothenuse for a = %d and b = %d, is %0.2f." %(a,b,hypothenuse))
    
main()