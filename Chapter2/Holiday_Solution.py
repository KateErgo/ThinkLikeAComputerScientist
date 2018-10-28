# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:52:36 2018

@author: kate
"""

##########################################
#### Think Like A Computer Sciencitst ####
##########################################

### Chapter 2 ###

## Holiday ##

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

startingDay = input("\nWhat is they starting day of your vacation? ")
lengthStay = int(input("\nWhat is the length of your stay? "))

holiday = days.index(startingDay) + lengthStay

if holiday > 7:
    duration = holiday % 7
else:
    duration = holiday
    
print("You will return on: " + days[duration] + ".")