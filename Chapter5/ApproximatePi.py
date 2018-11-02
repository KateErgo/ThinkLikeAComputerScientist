# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 08:26:44 2018

@author: kate
"""

import math

def approximate_pi(rank):
    value = 0
    for k in range(1, 2*rank+1, 2):
        sign = -(k % 4 - 2)
        value += float(sign) / k
    return 4 * value

print(math.pi)
print(approximate_pi(10))
