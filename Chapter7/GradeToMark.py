# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 08:29:25 2018

@author: kate
"""

def grade_to_mark(grade):
    
    if grade >= 90:
        return 'A'
    elif 80 >= grade < 90:
        return 'B'
    elif 70 >= grade < 80:
        return 'C'
    elif 60 >= grade < 70:
        return 'D'
    elif grade < 60:
        return 'F'
    
def main():
    grade = int(input("\nPlease enter the grade you received: "))
    
    mark = grade_to_mark(grade)
    
    print("\nYour mark is: " + mark + ".")
    
main()