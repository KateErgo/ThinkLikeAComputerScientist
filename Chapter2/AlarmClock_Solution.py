# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:36:31 2018

@author: kate
"""

##########################################
#### Think Like A Computer Sciencitst ####
##########################################

### Chapter 2 ###

## Alarm Clock ##

currentTime = int(input("\nWhat time is it now (in hours)? "))
hoursToWait = int(input("\nIn how many hours do you want the alarm to go off? "))

alarmTime = currentTime + hoursToWait

if alarmTime > 24:
    alarm = alarmTime % 24
else:
    alarm = alarmTime

print("Current time: %dh -- Time until alarm: %dh" % (currentTime, hoursToWait))
print("The time on the clock will be " + str(alarm) + "h when the alarm goes off.")